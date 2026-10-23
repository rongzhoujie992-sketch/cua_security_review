#!/usr/bin/env python3
"""Project the verified supplementary ledgers into the public release schema."""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows({field: row.get(field, "") for field in fields} for row in rows)


def project_row(row: dict[str, str], fields: list[str], aliases: dict[str, str] | None = None) -> dict[str, str]:
    aliases = aliases or {}
    out: dict[str, str] = {}
    for field in fields:
        source = aliases.get(field, field)
        out[field] = row.get(source, "")
    return out


def source_text_path(locator: str) -> str:
    match = re.search(r"(?:^|\|\s*)(source_text/[^:|]+)", locator)
    return match.group(1) if match else ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", type=Path)
    parser.add_argument("supplement", type=Path)
    args = parser.parse_args()
    repo, supplement = args.repo, args.supplement
    data = repo / "data"
    sup_data = supplement / "data"

    candidate_fields, candidates = read_csv(data / "final_candidate_ledger.csv")
    eligibility_fields, eligibility = read_csv(data / "final_eligibility_ledger.csv")
    hpat_fields, hpats = read_csv(data / "final_hpat_ledger.csv")
    relation_fields, relations = read_csv(data / "final_relation_ledger.csv")
    artifact_fields, artifacts = read_csv(data / "evidence_artifacts.csv")
    candidates = [r for r in candidates if not r.get("final_candidate_id", "").startswith("SUP-")]
    eligibility = [r for r in eligibility if not r.get("decision_id", "").startswith("SUP-")]
    hpats = [r for r in hpats if not r.get("hpat_id", "").startswith("HPAT-SUP-")]
    relations = [r for r in relations if not r.get("decision_id", "").startswith("REL-SUP-")]
    artifacts = [r for r in artifacts if not r.get("evidence_artifact_id", "").startswith("EV-SUP-")]
    sup_candidates = read_csv(sup_data / "final_candidate_ledger.csv")[1]
    sup_eligibility = read_csv(sup_data / "final_eligibility_ledger.csv")[1]
    sup_hpats = read_csv(sup_data / "final_hpat_ledger.csv")[1]
    sup_relations = read_csv(sup_data / "final_relation_ledger.csv")[1]
    sup_artifacts = read_csv(sup_data / "evidence_artifacts.csv")[1]
    matching = read_csv(supplement / "provenance" / "matching_inventory.csv")[1]
    adjudications = read_csv(supplement / "provenance" / "adjudication_ledger.csv")[1]
    source_manifest = read_csv(supplement / "prisma" / "source_manifest.csv")[1]

    hpat_by_unit = {row["canonical_unit_id"]: row for row in sup_hpats}
    hpat_by_id = {row["hpat_id"]: row for row in sup_hpats}
    match_by_unit = {row["canonical_unit_id"]: row for row in matching}
    candidate_adjudication = {
        row["canonical_unit_id"]: row for row in adjudications
        if row["record_layer"] == "Candidate" and row["target_field"] == "candidate_status"
    }
    pdf_by_study = {row["study_id"]: row["relative_path"] for row in source_manifest}
    relation_by_artifact = {row["evidence_artifact_id"]: row for row in sup_relations if row.get("evidence_artifact_id")}
    artifact_by_id = {row["evidence_artifact_id"]: row for row in sup_artifacts}

    candidate_aliases = {
        "final_candidate_id": "canonical_unit_id", "canonical_group_id": "canonical_unit_id",
        "match_type": "mapping_type",
        "first_candidate_operation_ids": "first_candidate_operation_ids",
        "second_candidate_operation_ids": "second_candidate_operation_ids",
        "first_candidate_operation_id": "first_candidate_operation_ids",
        "second_candidate_operation_id": "second_candidate_operation_ids",
        "q1_concrete_operation": "q1_gate", "q2_consequentiality": "q2_gate",
        "q3_model_mediation": "q3_gate", "q4_privilege_basis": "q4_gate",
        "q5_operation_capability_link": "q5_gate", "final_eligibility": "hpat_eligibility",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
    }
    for row in sup_candidates:
        out = project_row(row, candidate_fields, candidate_aliases)
        match = match_by_unit.get(row["canonical_unit_id"], {})
        adjudication = candidate_adjudication.get(row["canonical_unit_id"], {})
        out["hpat_id"] = hpat_by_unit.get(row["canonical_unit_id"], {}).get("hpat_id", "")
        out["match_confidence"] = ""
        out["adjudication_disposition"] = "SOURCE_ADJUDICATED"
        out["source_coder"] = ";".join(coder for coder, key in (("first_coder", "first_candidate_operation_ids"), ("second_coder", "second_candidate_operation_ids")) if match.get(key))
        out["first_candidate_operation_id"] = adjudication.get("first_candidate_operation_id", "")
        out["second_candidate_operation_id"] = adjudication.get("second_candidate_operation_id", "")
        out["source_excerpt"] = match.get("source_observation", "")
        out["source_text_path"] = source_text_path(match.get("source_locator", ""))
        out["source_locator"] = match.get("source_locator", "")
        out["first_source_locator"] = adjudication.get("first_source_locator", "")
        out["second_source_locator"] = adjudication.get("second_source_locator", "")
        out["disposition_reason_class"] = adjudication.get("adjudication_reason_class", "")
        out["disposition_rationale"] = adjudication.get("adjudication_rationale", "")
        out["supporting_excerpt_or_source_note"] = adjudication.get("supporting_excerpt_or_source_note", "")
        out["adjudication_rationale"] = adjudication.get("adjudication_rationale", "")
        out["adjudicator"] = adjudication.get("adjudicator", row.get("adjudicator", ""))
        out["unitization_status"] = ""
        out["unitization_stable"] = ""
        candidates.append(out)

    eligibility_aliases = {
        "decision_id": "canonical_unit_id", "final_candidate_id": "canonical_unit_id",
        "canonical_group_id": "canonical_unit_id", "first_candidate_operation_id": "first_candidate_operation_ids",
        "second_candidate_operation_id": "second_candidate_operation_ids", "q1_concrete_operation": "q1_gate",
        "q2_consequentiality": "q2_gate", "q3_model_mediation": "q3_gate", "q4_privilege_basis": "q4_gate",
        "q5_operation_capability_link": "q5_gate", "hpat_eligibility": "hpat_eligibility",
        "first_eligibility": "", "second_eligibility": "",
        "source_excerpt": "source_locator", "unitization_status": "",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
    }
    for row in sup_eligibility:
        out = project_row(row, eligibility_fields, eligibility_aliases)
        out["first_eligibility"] = ""
        out["second_eligibility"] = ""
        out["source_locator"] = row.get("source_locator", "")
        out["source_excerpt"] = ""
        out["unitization_status"] = ""
        out["adjudication_reason"] = ""
        out["adjudication_disposition"] = ""
        out["disposition_reason_class"] = ""
        out["disposition_rationale"] = ""
        out["adjudication_rationale"] = ""
        out["adjudicator"] = row.get("adjudicator", "")
        eligibility.append(out)

    hpat_aliases = {
        "candidate_operation_id": "canonical_unit_id",
        "source_candidate_operation_ids": "candidate_operation_ids", "canonical_group_id": "canonical_unit_id",
        "review_status": "relation_status",
        "final_eligibility": "eligibility_status", "coder": "adjudicator",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
    }
    for row in sup_hpats:
        out = project_row(row, hpat_fields, hpat_aliases)
        if not out["source_candidate_operation_ids"]:
            out["source_candidate_operation_ids"] = (
                row.get("candidate_operation_ids", "")
                or row.get("second_candidate_operation_ids", "")
                or row.get("adjudicated_operation_id", "")
            )
        match = match_by_unit.get(row["canonical_unit_id"], {})
        out["source_text_path"] = source_text_path(match.get("source_locator", ""))
        out["source_hpat_id"] = ""
        out["source_excerpt"] = match.get("source_observation", "")
        hpats.append(out)

    relation_aliases = {
        "decision_id": "relation_record_id", "record_scope": "relation_name",
        "target_record_id": "hpat_id", "evidence_status": "relation_status",
        "evidence_artifacts": "evidence_artifact_id", "source_locator": "source_locator", "decision_reason": "decision_reason",
        "coverage_qualifier": "coverage_qualifier", "final_coverage_qualifier": "coverage_qualifier",
        "claim_support_ceiling": "claim_support_ceiling", "codebook_version": "codebook_version",
        "coder": "adjudicator", "review_status": "adjudication_reason_class",
        "canonical_group_id": "canonical_unit_id", "final_candidate_id": "canonical_unit_id",
        "first_evidence_status": "first_relation_status", "second_evidence_status": "second_relation_status",
        "first_source_locator": "first_source_locator", "second_source_locator": "second_source_locator",
        "adjudication_reason_class": "adjudication_reason_class", "adjudication_rationale": "adjudication_rationale",
        "adjudicator": "adjudicator",
        "adjudication_date": "adjudication_date", "source_text_path": "source_locator",
    }
    for row in sup_relations:
        out = project_row(row, relation_fields, relation_aliases)
        out["record_scope"] = "transition_field"
        out["target_record_type"] = "hpat_transition"
        out["target_record_id"] = row.get("hpat_id", "")
        out["hpat_id"] = row.get("hpat_id", "")
        out["source_pdf"] = pdf_by_study.get(row["study_id"], "")
        out["source_text_path"] = source_text_path(row.get("source_locator", ""))
        out["evidence_provenance"] = ""
        artifact = artifact_by_id.get(row.get("evidence_artifact_id", ""), {})
        out["supporting_excerpt_or_source_note"] = artifact.get("faithful_excerpt_or_paraphrase", "")
        relations.append(out)

    artifact_aliases = {
        "candidate_operation_id": "candidate_operation_id", "hpat_id": "hpat_id",
        "field_name": "relation_name",
        "source_locator": "source_locator", "faithful_excerpt_or_paraphrase": "faithful_excerpt_or_paraphrase",
        "scope_and_condition": "scope_and_condition", "evidence_role": "evidence_role",
        "coder_id": "coder_id", "codebook_version": "codebook_version",
    }
    status_by_artifact = {r["evidence_artifact_id"]: r["relation_status"] for r in sup_relations if r.get("evidence_artifact_id")}
    for row in sup_artifacts:
        out = project_row(row, artifact_fields, artifact_aliases)
        source_hpat = hpat_by_id.get(row["hpat_id"], {})
        out["candidate_operation_id"] = source_hpat.get("adjudicated_operation_id", "")
        out["source_extraction_unit_id"] = source_hpat.get("source_extraction_unit_id", "")
        out["supports_record_type"] = "hpat_transition"
        out["evidence_type"] = ""
        out["observation_mode"] = ""
        out["evidence_status"] = status_by_artifact.get(row["evidence_artifact_id"], "")
        out["artifact_provenance"] = ""
        artifacts.append(out)

    write_csv(data / "final_candidate_ledger.csv", candidate_fields, candidates)
    write_csv(data / "final_eligibility_ledger.csv", eligibility_fields, eligibility)
    write_csv(data / "final_hpat_ledger.csv", hpat_fields, hpats)
    write_csv(data / "final_relation_ledger.csv", relation_fields, relations)
    write_csv(data / "evidence_artifacts.csv", artifact_fields, artifacts)


if __name__ == "__main__":
    main()
