#!/usr/bin/env python3
"""Project the verified supplementary ledgers into the public release schema."""
from __future__ import annotations

import argparse
import csv
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

    hpat_by_unit = {row["canonical_unit_id"]: row for row in sup_hpats}
    hpat_by_id = {row["hpat_id"]: row for row in sup_hpats}

    candidate_aliases = {
        "final_candidate_id": "canonical_unit_id", "canonical_group_id": "canonical_unit_id",
        "match_type": "mapping_type",
        "first_candidate_operation_ids": "first_candidate_operation_ids",
        "second_candidate_operation_ids": "second_candidate_operation_ids",
        "first_candidate_operation_id": "first_candidate_operation_ids",
        "second_candidate_operation_id": "second_candidate_operation_ids",
        "source_coder": "adjudication_rationale",
        "q1_concrete_operation": "q1_gate", "q2_consequentiality": "q2_gate",
        "q3_model_mediation": "q3_gate", "q4_privilege_basis": "q4_gate",
        "q5_operation_capability_link": "q5_gate", "final_eligibility": "hpat_eligibility",
        "adjudication_disposition": "decision_reason", "disposition_reason_class": "decision_reason",
        "disposition_rationale": "decision_reason", "first_source_locator": "source_locator",
        "second_source_locator": "source_locator", "adjudicator": "adjudicator",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
        "supporting_excerpt_or_source_note": "decision_reason", "adjudication_rationale": "decision_reason",
        "hpat_id": "canonical_unit_id",
    }
    for row in sup_candidates:
        out = project_row(row, candidate_fields, candidate_aliases)
        out["hpat_id"] = hpat_by_unit.get(row["canonical_unit_id"], {}).get("hpat_id", "")
        out["match_confidence"] = "source_adjudicated"
        out["adjudication_disposition"] = "SOURCE_ADJUDICATED"
        out["unitization_status"] = "stable_source_native_unit" if row.get("canonical_unit_id") in hpat_by_unit else "source_native_unit_retained"
        out["source_coder"] = "first_coder;second_coder"
        if "||" in out["first_candidate_operation_id"]:
            out["first_candidate_operation_id"] = ""
        if "||" in out["second_candidate_operation_id"]:
            out["second_candidate_operation_id"] = ""
        out["source_excerpt"] = row.get("decision_reason", "")
        out["source_text_path"] = f"source://{row['study_id']}.txt"
        candidates.append(out)

    eligibility_aliases = {
        "decision_id": "canonical_unit_id", "final_candidate_id": "canonical_unit_id",
        "canonical_group_id": "canonical_unit_id", "first_candidate_operation_id": "first_candidate_operation_ids",
        "second_candidate_operation_id": "second_candidate_operation_ids", "q1_concrete_operation": "q1_gate",
        "q2_consequentiality": "q2_gate", "q3_model_mediation": "q3_gate", "q4_privilege_basis": "q4_gate",
        "q5_operation_capability_link": "q5_gate", "hpat_eligibility": "hpat_eligibility",
        "first_eligibility": "", "second_eligibility": "",
        "source_excerpt": "decision_reason", "unitization_status": "source_unit_type",
        "adjudication_reason": "decision_reason", "adjudication_disposition": "adjudicator",
        "disposition_reason_class": "decision_reason", "disposition_rationale": "decision_reason",
        "adjudication_rationale": "decision_reason", "adjudicator": "adjudicator",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
    }
    for row in sup_eligibility:
        out = project_row(row, eligibility_fields, eligibility_aliases)
        out["first_eligibility"] = ""
        out["second_eligibility"] = ""
        out["source_locator"] = row.get("source_locator", "")
        eligibility.append(out)

    hpat_aliases = {
        "candidate_operation_id": "candidate_operation_ids", "source_hpat_id": "hpat_id",
        "source_candidate_operation_ids": "candidate_operation_ids", "canonical_group_id": "canonical_unit_id",
        "source_text_path": "source_locator", "review_status": "relation_status",
        "final_eligibility": "eligibility_status", "coder": "adjudicator",
        "adjudication_date": "adjudication_date", "codebook_version": "codebook_version",
    }
    for row in sup_hpats:
        out = project_row(row, hpat_fields, hpat_aliases)
        out["source_text_path"] = f"source://{row['study_id']}.txt"
        hpats.append(out)

    relation_aliases = {
        "decision_id": "relation_record_id", "record_scope": "relation_name",
        "target_record_type": "relation_name", "target_record_id": "hpat_id", "evidence_status": "relation_status",
        "evidence_artifacts": "evidence_artifact_id", "evidence_provenance": "adjudication_reason_class",
        "source_pdf": "source_locator", "source_locator": "source_locator", "decision_reason": "decision_reason",
        "coverage_qualifier": "coverage_qualifier", "final_coverage_qualifier": "coverage_qualifier",
        "claim_support_ceiling": "claim_support_ceiling", "codebook_version": "codebook_version",
        "coder": "adjudicator", "review_status": "adjudication_reason_class",
        "canonical_group_id": "canonical_unit_id", "final_candidate_id": "canonical_unit_id",
        "first_evidence_status": "first_relation_status", "second_evidence_status": "second_relation_status",
        "first_source_locator": "first_source_locator", "second_source_locator": "second_source_locator",
        "adjudication_reason_class": "adjudication_reason_class", "adjudication_rationale": "adjudication_rationale",
        "supporting_excerpt_or_source_note": "adjudication_rationale", "adjudicator": "adjudicator",
        "adjudication_date": "adjudication_date", "source_text_path": "source_locator",
    }
    for row in sup_relations:
        out = project_row(row, relation_fields, relation_aliases)
        out["record_scope"] = "transition_field"
        out["target_record_type"] = "hpat_transition"
        out["target_record_id"] = row.get("hpat_id", "")
        out["hpat_id"] = row.get("hpat_id", "")
        relations.append(out)

    artifact_aliases = {
        "candidate_operation_id": "candidate_operation_id", "hpat_id": "hpat_id",
        "source_extraction_unit_id": "source_locator", "supports_record_type": "relation_name",
        "field_name": "relation_name", "evidence_type": "evidence_role",
        "observation_mode": "evidence_role",
        "source_locator": "source_locator", "faithful_excerpt_or_paraphrase": "faithful_excerpt_or_paraphrase",
        "scope_and_condition": "scope_and_condition", "evidence_role": "evidence_role",
        "coder_id": "coder_id", "codebook_version": "codebook_version",
    }
    status_by_artifact = {r["evidence_artifact_id"]: r["relation_status"] for r in sup_relations}
    for row in sup_artifacts:
        out = project_row(row, artifact_fields, artifact_aliases)
        out["evidence_status"] = status_by_artifact.get(row["evidence_artifact_id"], "")
        artifacts.append(out)

    write_csv(data / "final_candidate_ledger.csv", candidate_fields, candidates)
    write_csv(data / "final_eligibility_ledger.csv", eligibility_fields, eligibility)
    write_csv(data / "final_hpat_ledger.csv", hpat_fields, hpats)
    write_csv(data / "final_relation_ledger.csv", relation_fields, relations)
    write_csv(data / "evidence_artifacts.csv", artifact_fields, artifacts)


if __name__ == "__main__":
    main()
