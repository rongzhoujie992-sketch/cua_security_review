#!/usr/bin/env python3
"""Project the verified supplementary ledgers into the public release schema."""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

from release_checks import MAIN, SUPPLEMENT, derive_eligibility


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
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


def merge_supplementary_rows(path: Path, supplement_rows: list[dict[str, str]]) -> None:
    """Retain original-corpus rows and replace only this supplementary population."""
    fields, existing = read_csv(path)
    original = [dict(row, coding_population=MAIN) for row in existing
                if row.get("coding_population", MAIN) != SUPPLEMENT
                and not (row.get("canonical_group_id", "") or row.get("matching_group_id", "")).startswith("SUP-")]
    supplementary = [dict(row, coding_population=SUPPLEMENT) for row in supplement_rows]
    for row in original + supplementary:
        fields.extend(key for key in row if key not in fields)
    write_csv(path, fields, original + supplementary)


def integrate_provenance(repo: Path, supplement: Path) -> None:
    """Project existing matching, gate and relation decisions without re-adjudicating."""
    matching = read_csv(supplement / "provenance/matching_inventory.csv")[1]
    candidates = read_csv(supplement / "data/final_candidate_ledger.csv")[1]
    hpats = read_csv(supplement / "data/final_hpat_ledger.csv")[1]
    relations = read_csv(supplement / "data/final_relation_ledger.csv")[1]
    adjudications = read_csv(supplement / "provenance/adjudication_ledger.csv")[1]
    comparisons = read_csv(supplement / "reliability/candidate_comparison.csv")[1]
    units = read_csv(supplement / "reliability/unitization_comparison.csv")[1]
    c_by_id = {r["canonical_unit_id"]: r for r in candidates}
    h_by_unit = {r["canonical_unit_id"]: r for r in hpats}
    m_by_id = {r["canonical_unit_id"]: r for r in matching}
    cmp_by_id = {r["canonical_unit_id"]: r for r in comparisons}
    unit_by_id = {r["canonical_unit_id"]: r for r in units}
    projected_matching = []
    for row in matching:
        key = row["canonical_unit_id"]
        comparison, unit = cmp_by_id.get(key, {}), unit_by_id.get(key, {})
        out = dict(row, matching_group_id=key, match_type=row["mapping_type"],
                   primary_candidate_operation_ids=row["first_candidate_operation_ids"],
                   primary_source_locators=comparison.get("first_source_locator", ""),
                   second_source_locators=comparison.get("second_source_locator", ""),
                   primary_operations=unit.get("first_operation_description", ""),
                   second_operations=unit.get("second_operation_description", ""),
                   primary_targets=comparison.get("first_target_or_recipient", ""),
                   second_targets=comparison.get("second_target_or_recipient", ""),
                   primary_atomicity=comparison.get("first_source_native_atomicity", ""),
                   second_atomicity=comparison.get("second_source_native_atomicity", ""),
                   matching_note=row["mapping_rationale"], canonical_resolution=row["adjudicated_candidate_status"])
        projected_matching.append(out)
    merge_supplementary_rows(repo / "provenance/matching_inventory.csv", projected_matching)

    projected_adjudications = []
    for row in adjudications:
        key = row["canonical_unit_id"]
        candidate, match = c_by_id.get(key, {}), m_by_id[key]
        is_candidate = row["target_field"] == "candidate_status"
        out = dict(row, canonical_group_id=key, match_type=match["mapping_type"],
                   record_type=("candidate" if candidate else "source_unit_completion") if is_candidate else "candidate_gate",
                   final_candidate_id=key if candidate else "", hpat_id=h_by_unit.get(key, {}).get("hpat_id", ""),
                   unit_role="source_native_candidate" if candidate else "source_unit_reviewed_no_candidate")
        if is_candidate and candidate:
            out["final_eligibility"] = candidate["hpat_eligibility"]
            for i in range(1, 6):
                out[f"q{i}_final"] = candidate[f"q{i}_gate"]
            out["operation_description"] = candidate["operation_description"]
            out["target_or_recipient"] = candidate["target_or_recipient"]
            out["source_native_atomicity"] = candidate["source_native_atomicity"]
        elif row["target_field"] in {f"q{i}_gate" for i in range(2, 6)}:
            out[f"q{row['target_field'][1]}_final"] = row["adjudicated_value"]
        projected_adjudications.append(out)
    for row in relations:
        projected_adjudications.append(dict(
            row, record_type="relation", canonical_group_id=row["canonical_unit_id"],
            final_candidate_id=row["canonical_unit_id"],
            match_type=m_by_id[row["canonical_unit_id"]]["mapping_type"],
            adjudicated_relation_status=row["relation_status"], adjudicated_source_locator=row["source_locator"],
            supporting_excerpt_or_source_note=row["substantive_value"],
        ))
    merge_supplementary_rows(repo / "provenance/adjudication_ledger.csv", projected_adjudications)


def integrate_comparisons(repo: Path, supplement: Path) -> None:
    """Keep supplementary independent pairs separate from the original denominator."""
    source = supplement / "reliability"
    candidates = read_csv(source / "candidate_comparison.csv")[1]
    mapping_types = {r["canonical_unit_id"]: r["mapping_type"] for r in candidates}
    for row in candidates:
        row["matching_group_id"] = row["canonical_unit_id"]
        row["comparison_scope"] = "strict_one_to_one" if row["mapping_type"] == "one_to_one" else row["mapping_type"]
    merge_supplementary_rows(repo / "reliability/candidate_comparison.csv", candidates)
    units = read_csv(source / "unitization_comparison.csv")[1]
    for row in units:
        row["matching_group_id"] = row["canonical_unit_id"]
        row["comparison_scope"] = "strict_one_to_one" if mapping_types[row["canonical_unit_id"]] == "one_to_one" else mapping_types[row["canonical_unit_id"]]
    merge_supplementary_rows(repo / "reliability/unitization_comparison.csv", units)

    gate_rows = read_csv(source / "q1_q5_comparison.csv")[1]
    gates = {}
    for row in gate_rows:
        key = row["canonical_unit_id"]
        out = gates.setdefault(key, {k: row[k] for k in ("study_id", "first_candidate_operation_id", "second_candidate_operation_id")})
        out["matching_group_id"], out["comparison_scope"] = key, "strict_one_to_one"
        field = row["field_name"].removesuffix("_gate")
        for coder in ("first", "second"):
            out[f"{coder}_{field}"] = row[f"{coder}_value_raw"]
            out[f"{coder}_{field}_source_locator"] = row[f"{coder}_source_locator"]
            out[f"{coder}_{field}_reason_raw"] = row[f"{coder}_reason_raw"]
        out[f"{field}_agreement"] = ("yes" if row["first_value_raw"] == row["second_value_raw"] else "no") if row["first_value_raw"] and row["second_value_raw"] else ""
    merge_supplementary_rows(repo / "reliability/q1_q5_comparison.csv", list(gates.values()))
    eligibility = read_csv(source / "eligibility_comparison.csv")[1]
    for row in eligibility:
        row["matching_group_id"], row["comparison_scope"] = row["canonical_unit_id"], "strict_one_to_one"
        for coder in ("first", "second"):
            row[f"{coder}_eligibility_reported"] = row[f"{coder}_hpat_eligibility_raw"]
            row[f"{coder}_eligibility"] = derive_eligibility([row[f"{coder}_q{i}_gate_raw"] for i in range(2, 6)])
        row["eligibility_agreement"] = "yes" if row["first_eligibility"] == row["second_eligibility"] else "no"
    merge_supplementary_rows(repo / "reliability/eligibility_comparison.csv", eligibility)
    relations = read_csv(source / "relation_comparison.csv")[1]
    for row in relations:
        row["matching_group_id"] = row["canonical_unit_id"]
        row["comparison_scope"] = "adjudicated_supplementary_population"
        row["comparable_for_relation_reliability"] = "no"
        for coder in ("first", "second"):
            row[f"{coder}_evidence_status"] = row[f"{coder}_relation_status"]
            row[f"{coder}_relation_record_present"] = "yes" if row[f"{coder}_relation_status"] else "no"
    merge_supplementary_rows(repo / "reliability/relation_comparison.csv", relations)


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
        out["unitization_status"] = match.get("review_status", "")
        out["unitization_stable"] = row.get("unitization_stable", "")
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
        candidate = next(r for r in candidates if r["final_candidate_id"] == row["canonical_unit_id"])
        out["source_excerpt"] = candidate.get("source_excerpt", "")
        out["unitization_status"] = candidate.get("unitization_status", "")
        out["first_source_locator"] = candidate.get("first_source_locator", "")
        out["second_source_locator"] = candidate.get("second_source_locator", "")
        out["adjudication_reason"] = row.get("decision_reason", "")
        out["adjudication_disposition"] = ""
        out["disposition_reason_class"] = candidate.get("disposition_reason_class", "")
        out["disposition_rationale"] = candidate.get("disposition_rationale", "")
        out["adjudication_rationale"] = candidate.get("adjudication_rationale", "")
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
        out["candidate_operation_id"] = source_hpat["canonical_unit_id"]
        out["source_extraction_unit_id"] = source_hpat.get("source_extraction_unit_id", "")
        out["supports_record_type"] = "hpat_transition"
        out["evidence_type"] = row.get("evidence_type", "")
        out["observation_mode"] = row.get("observation_mode", "")
        out["evidence_status"] = status_by_artifact.get(row["evidence_artifact_id"], "")
        out["artifact_provenance"] = ""
        if not out["scope_and_condition"]:
            out["scope_and_condition"] = match_by_unit[source_hpat["canonical_unit_id"]]["scenario_or_condition"]
        artifacts.append(out)

    write_csv(data / "final_candidate_ledger.csv", candidate_fields, candidates)
    write_csv(data / "final_eligibility_ledger.csv", eligibility_fields, eligibility)
    write_csv(data / "final_hpat_ledger.csv", hpat_fields, hpats)
    write_csv(data / "final_relation_ledger.csv", relation_fields, relations)
    write_csv(data / "evidence_artifacts.csv", artifact_fields, artifacts)
    integrate_provenance(repo, supplement)
    integrate_comparisons(repo, supplement)


if __name__ == "__main__":
    main()
