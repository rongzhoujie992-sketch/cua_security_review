#!/usr/bin/env python3
"""Build the unified supplementary source route and release validation record."""
from __future__ import annotations

import csv
import json
import argparse
from collections import Counter
from pathlib import Path


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        out = csv.DictWriter(handle, fieldnames=fields)
        out.writeheader()
        out.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("supplement", type=Path)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    supplement = args.supplement
    supplement_validation = json.loads((supplement / "validation.json").read_text(encoding="utf-8"))
    main_validation = json.loads((repo / "validation.json").read_text(encoding="utf-8"))
    route_fields = ["route_source_id", "route", "source_type", "title", "source_locator", "coding_status", "coding_study_id", "scope_note"]
    route: list[dict[str, str]] = []

    for row in read(repo / "prisma" / "foundational_branch" / "foundational_source_ledger.csv"):
        route.append({"route_source_id": row["canonical_id"], "route": "supplementary", "source_type": "foundational_classical", "title": row["title"], "source_locator": row["source_locator"], "coding_status": "source_route_only", "coding_study_id": "", "scope_note": "Conceptual or authoritative foundation; not a Candidate/HPAT coding unit."})
    for row in read(repo / "prisma" / "tdes_branch" / "selected_sources_9.csv"):
        source_type = "tdes_official" if row["Class"].lower().startswith("official") else "tdes_academic"
        study_id = {"TDES-ACA-001": "S-223", "TDES-ACA-002": "S-224", "TDES-ACA-003": "S-225", "TDES-ACA-004": "S-226"}.get(row["Source ID"], "")
        route.append({"route_source_id": row["Source ID"], "route": "supplementary", "source_type": source_type, "title": row["Source"], "source_locator": row["URL"], "coding_status": "coded_in_main_population" if study_id else "source_route_only", "coding_study_id": study_id, "scope_note": row["Boundary"]})
    selected = {row["Study_ID"]: row for row in read(supplement / "prisma" / "data" / "post_cutoff" / "selected_studies.csv")}
    for row in read(supplement / "prisma" / "source_manifest.csv"):
        study_id = row["study_id"]
        selected_row = selected.get(study_id, {})
        route.append({"route_source_id": study_id, "route": "supplementary", "source_type": "post_cutoff_study", "title": selected_row.get("Title", ""), "source_locator": row["relative_path"], "coding_status": "coded_in_unified_ledgers" if study_id != "B1-W007" else "source_reviewed_q1_not_established", "coding_study_id": study_id, "scope_note": "Post-cutoff source selected through the Dedup34 route."})
    write(repo / "integration" / "supplementary_evidence_route.csv", route_fields, route)
    accounting = [
        {"component": "Final main CUA corpus", "count": "222", "unit": "study", "additive_to_unique_source_base": "YES", "note": "Systematic review corpus"},
        {"component": "Foundational/classical security branch", "count": "12", "unit": "source", "additive_to_unique_source_base": "YES", "note": "Separate theoretical/authoritative evidence route"},
        {"component": "TDES supplementary sources", "count": "9", "unit": "source", "additive_to_unique_source_base": "YES", "note": "Additive to the 222-study main corpus; the 4 academic sources are included in the 226-study coding population"},
        {"component": "Post-cutoff supplementary studies", "count": "34", "unit": "study", "additive_to_unique_source_base": "YES", "note": "Dedup34 selected source route"},
        {"component": "Final unique evidence/source base", "count": "277", "unit": "source", "additive_to_unique_source_base": "TOTAL", "note": "222 + 12 + 9 + 34"},
    ]
    write(repo / "prisma" / "reports" / "integrated_source_accounting_277.csv", list(accounting[0]), accounting)

    candidates = read(repo / "data" / "final_candidate_ledger.csv")
    eligibility = read(repo / "data" / "final_eligibility_ledger.csv")
    hpats = read(repo / "data" / "final_hpat_ledger.csv")
    relations = read(repo / "data" / "final_relation_ledger.csv")
    artifacts = read(repo / "data" / "evidence_artifacts.csv")
    relation_keys = {(r["hpat_id"], r["relation_name"]) for r in relations}
    hpat_ids = {r["hpat_id"] for r in hpats}
    artifact_ids = {r["evidence_artifact_id"] for r in artifacts}
    relation_by_hpat = Counter(r["hpat_id"] for r in relations)
    artifact_by_id = {r["evidence_artifact_id"]: r for r in artifacts}
    positive_closed = all(
        r["evidence_status"] not in {"Present-direct", "Present-partial"}
        or (artifact := artifact_by_id.get(r["evidence_artifacts"])) is not None
        and artifact.get("hpat_id") == r["hpat_id"]
        and artifact.get("study_id") == r["study_id"]
        and artifact.get("field_name") == r["relation_name"]
        and artifact.get("evidence_status") == r["evidence_status"]
        for r in relations
    )
    relation_names = {"Influence", "Authorization", "Technical Permission", "Operation Execution", "External Effect", "Resulting State", "Technical Attribution", "Containment", "Recovery"}
    candidate_ids = {r["final_candidate_id"] for r in candidates}
    eligibility_ids = {r["final_candidate_id"] for r in eligibility}
    hpat_candidate_ids = {r["candidate_operation_id"] for r in hpats}
    supplementary_candidate_ids = {
        r["final_candidate_id"] for r in candidates if r["final_candidate_id"].startswith("SUP-")
    }
    supplementary_hpats = [r for r in hpats if r["hpat_id"].startswith("HPAT-SUP-")]
    candidate_by_id = {r["final_candidate_id"]: r for r in candidates}

    def source_operation_ids(candidate: dict[str, str]) -> set[str]:
        return {
            value.strip()
            for field in (
                "first_candidate_operation_ids", "second_candidate_operation_ids",
                "first_candidate_operation_id", "second_candidate_operation_id",
            )
            for value in (candidate.get(field, "") or "").replace("||", ";").split(";")
            if value.strip()
        }
    route_counts = Counter(r["source_type"] for r in route)
    route_study_ids = {r["coding_study_id"] for r in route if r["coding_study_id"]}
    checks = {
        "candidate_ids_unique": len(candidate_ids) == len(candidates),
        "eligibility_ids_unique_and_aligned": len(eligibility_ids) == len(eligibility) and eligibility_ids == candidate_ids,
        "hpat_ids_unique": len(hpat_ids) == len(hpats),
        "hpat_candidate_ids_resolve": hpat_candidate_ids <= candidate_ids,
        "supplementary_hpat_candidate_keys_resolve": all(
            r["candidate_operation_id"] in supplementary_candidate_ids
            and r.get("canonical_group_id") == r["candidate_operation_id"]
            for r in supplementary_hpats
        ),
        "supplementary_hpat_operation_provenance_present": all(
            r.get("adjudicated_operation_id")
            and r.get("source_candidate_operation_ids")
            and set(r["adjudicated_operation_id"].split(";"))
            <= source_operation_ids(candidate_by_id.get(r.get("canonical_group_id", ""), {}))
            for r in supplementary_hpats
        ),
        "relation_keys_unique": len(relation_keys) == len(relations),
        "nine_relations_per_hpat": all(count == 9 for count in relation_by_hpat.values()) and all({r["relation_name"] for r in relations if r["hpat_id"] == hpat} == relation_names for hpat in hpat_ids),
        "positive_relation_artifacts_closed": positive_closed,
        "all_artifact_relation_references_resolve": all(not r["evidence_artifacts"] or r["evidence_artifacts"] in artifact_ids for r in relations),
        "candidate_locator_reason_complete": all(r.get("source_locator") and r.get("disposition_rationale") for r in candidates),
        "eligibility_locator_complete": all(r.get("source_locator") for r in eligibility),
        "relation_locator_reason_complete": all(r.get("source_locator") and r.get("decision_reason") for r in relations),
        "artifact_locator_excerpt_complete": all(r.get("source_locator") and r.get("faithful_excerpt_or_paraphrase") for r in artifacts),
        "supplementary_route_rows": len(route) == 55 and route_counts == {"foundational_classical": 12, "tdes_academic": 4, "tdes_official": 5, "post_cutoff_study": 34},
        "no_local_filesystem_paths": not any("Users\\" in value or "中国科学院" in value for row in route for value in row.values()),
    }
    validation = {
        "semantic_status": "COMPLETE" if supplement_validation.get("semantic_status") == "COMPLETE" and main_validation.get("semantic_status") == "COMPLETE" else "IN_PROGRESS",
        "structural_status": "PASSED",
        "codebook_version": "3.3.0",
        "counts": {"studies": 260, "prisma_main_corpus_studies": 222, "supplementary_tdes_sources": 9, "supplementary_foundational_sources": 12, "supplementary_post_cutoff_studies": 34, "evidence_source_base": 277, "candidates": len(candidates), "eligibility_rows": len(eligibility), "hpats": len(hpats), "relations": len(relations), "expected_relations": len(hpats) * 9, "evidence_artifacts": len(artifacts)},
        "coding_population": {"main_226_study_release": 226, "post_cutoff_added": 34, "unified": 260},
        "reliability_boundary": {"main_release": "Existing reliability files retain the original 226-study denominator.", "post_cutoff": "Supplementary reliability remains source-layered and is not pooled with the main denominator."},
        "checks": checks,
        "source_route": {"foundational_classical": 12, "tdes": 9, "post_cutoff": 34, "total_supplementary": 55, "overall_evidence_source_base": 277},
        "errors": [],
    }
    validation["checks"]["all_hpat_relation_targets_exist"] = all(r["hpat_id"] in hpat_ids for r in relations)
    validation["structural_status"] = "PASSED" if all(checks.values()) and validation["checks"]["all_hpat_relation_targets_exist"] else "FAILED"
    validation["errors"] = [name for name, passed in validation["checks"].items() if not passed]
    (repo / "validation.json").write_text(json.dumps(validation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
