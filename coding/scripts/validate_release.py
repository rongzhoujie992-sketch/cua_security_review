#!/usr/bin/env python3
"""Validate the public HPAC/HPAT coding release against its release manifest."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABSOLUTE_PATH = re.compile(r"(?:^|[^A-Za-z])[A-Za-z]:[\\/]|\\\\|/mnt/|/Users/")


def read_csv(relative: str) -> tuple[list[str], list[dict[str, str]]]:
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def read_json(relative: str) -> dict[str, object]:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def read_cff_value(name: str) -> str | None:
    match = re.search(
        rf"(?m)^{re.escape(name)}: [\"']?([^\"'\n]+)[\"']?$",
        (ROOT / "CITATION.cff").read_text(encoding="utf-8"),
    )
    return match.group(1) if match else None


def main() -> int:
    errors: list[str] = []
    try:
        manifest_metadata = read_json("artifact_manifest.json")
        summary = read_json("reports/coding_summary.json")
        release_status = read_json("release_status.json")
    except (OSError, json.JSONDecodeError) as error:
        print(f"RELEASE VALIDATION FAILED\n- invalid release metadata: {error}")
        return 1

    expected = {
        "data/study_records.csv": manifest_metadata["canonical_study_count"],
        "data/candidate_operation_records.csv": manifest_metadata["candidate_operation_count"],
        "data/candidate_audit_decisions.csv": manifest_metadata["candidate_audit_decision_count"],
        "data/hpat_transition_records.csv": manifest_metadata["qualified_hpat_count"],
        "data/evidence_artifacts.csv": manifest_metadata["evidence_artifact_count"],
        "data/decision_records.csv": manifest_metadata["hpat_relation_decision_count"],
        "data/control_records.csv": manifest_metadata["control_record_count"],
        "data/cross_transition_relations.csv": manifest_metadata["cross_transition_relation_count"],
        "role/contribution_role_records.csv": manifest_metadata["role_record_count"],
        "role/central_role_crosswalk.csv": manifest_metadata["role_study_count"],
        "reliability/candidate_unitization_decisions_final.csv": 61,
        "reliability/candidate_audit_status_comparison.csv": 66,
        "reliability/hpat_operation_adjudication_records.csv": 61,
        "reliability/hpat_relation_comparison_double_qualified.csv": 20,
        "reliability/role_adjudication_records.csv": 18,
        "reliability/role_status_comparison.csv": 54,
        "reliability/study_scope_comparison.csv": 45,
    }
    data: dict[str, tuple[list[str], list[dict[str, str]]]] = {}
    for relative, expected_count in expected.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing {relative}")
            continue
        headers, rows = read_csv(relative)
        data[relative] = (headers, rows)
        if len(rows) != expected_count:
            errors.append(f"{relative} has {len(rows)} rows; manifest expects {expected_count}")

    allowed_evidence_statuses = {
        "Present-direct",
        "Present-partial",
        "Absent-explicit",
        "Not reported",
        "Not applicable",
        "Indeterminate",
    }
    for relative, (headers, rows) in data.items():
        if "evidence_status" not in headers:
            continue
        invalid_statuses = sorted(
            {row["evidence_status"] for row in rows if row["evidence_status"] not in allowed_evidence_statuses}
        )
        if invalid_statuses:
            errors.append(f"{relative} contains invalid evidence statuses: {', '.join(invalid_statuses)}")

    studies = data.get("data/study_records.csv", ([], []))[1]
    candidates = data.get("data/candidate_operation_records.csv", ([], []))[1]
    hpats = data.get("data/hpat_transition_records.csv", ([], []))[1]
    roles = data.get("role/contribution_role_records.csv", ([], []))[1]
    crosswalk = data.get("role/central_role_crosswalk.csv", ([], []))[1]

    study_headers = data.get("data/study_records.csv", ([], []))[0]
    expected_public_study_headers = [
        "study_id",
        "canonical_identity_key",
        "title",
        "authors",
        "year",
        "publication_status",
        "canonical_source_url",
        "full_text_status",
        "zero_hpat_reason",
        "coder_id",
    ]
    if study_headers != expected_public_study_headers:
        errors.append("study records contain fields outside the public study projection")
    required_public_study_fields = {
        "canonical_identity_key",
        "title",
        "authors",
        "year",
        "publication_status",
        "canonical_source_url",
        "full_text_status",
        "coder_id",
    }
    for field in sorted(required_public_study_fields):
        if any(not row.get(field, "").strip() for row in studies):
            errors.append(f"study records contain a blank required public field: {field}")

    if len({row["study_id"] for row in studies}) != len(studies):
        errors.append("study IDs are not unique")
    if len({row["candidate_operation_id"] for row in candidates}) != len(candidates):
        errors.append("candidate IDs are not unique")
    if len({row["hpat_id"] for row in hpats}) != len(hpats):
        errors.append("HPAT IDs are not unique")

    established = {row["candidate_operation_id"] for row in candidates if row["hpat_eligibility"] == "Established"}
    hpat_candidates = {row["candidate_operation_id"] for row in hpats}
    if established != hpat_candidates:
        errors.append("Established candidates do not exactly match HPAT records")

    hpat_studies = {row["study_id"] for row in hpats}
    role_studies = {row["study_id"] for row in roles}
    crosswalk_studies = {row["study_id"] for row in crosswalk}
    if hpat_studies != role_studies or hpat_studies != crosswalk_studies:
        errors.append("role records or crosswalk do not exactly cover HPAT-positive studies")
    if len(hpat_studies) != manifest_metadata["hpat_positive_study_count"]:
        errors.append("HPAT-positive study count differs from artifact manifest")

    role_counts = Counter(row["study_id"] for row in roles)
    if any(count != 3 for count in role_counts.values()):
        errors.append("each HPAT-positive study must have exactly three role records")
    if len({(row["study_id"], row["contribution_role"]) for row in roles}) != len(roles):
        errors.append("study-by-role records are not unique")
    if any(row["contribution_role"] not in {"threat", "evaluation", "safeguard"} for row in roles):
        errors.append("invalid contribution role")
    if any(row["role_status"] not in {"central", "supporting", "context_only", "not_present"} for row in roles):
        errors.append("invalid contribution-role status")
    role_headers = data.get("role/contribution_role_records.csv", ([], []))[0]
    if "annotation_status" in role_headers:
        errors.append("role records retain an internal annotation-status field")
    if any("primary_research_role" in row for row in crosswalk):
        errors.append("exclusive primary-role column is forbidden")

    summary_expectations = {
        "study_count": len(studies),
        "candidate_operation_count": len(candidates),
        "candidate_audit_decision_count": len(data.get("data/candidate_audit_decisions.csv", ([], []))[1]),
        "qualified_hpat_count": len(hpats),
        "hpat_positive_study_count": len(hpat_studies),
        "hpat_relation_decision_count": len(data.get("data/decision_records.csv", ([], []))[1]),
        "evidence_artifact_count": len(data.get("data/evidence_artifacts.csv", ([], []))[1]),
        "control_record_count": len(data.get("data/control_records.csv", ([], []))[1]),
        "cross_transition_relation_count": len(data.get("data/cross_transition_relations.csv", ([], []))[1]),
        "role_study_count": len(crosswalk),
        "role_record_count": len(roles),
    }
    for key, count in summary_expectations.items():
        if summary.get(key) != count:
            errors.append(f"coding summary mismatch for {key}")
    if {"second_coder_candidate_units", "adjudicated_candidate_units"} & set(summary):
        errors.append("coding summary retains reliability-workflow counters")

    if manifest_metadata.get("artifact_version") != release_status.get("artifact_version"):
        errors.append("artifact and release-status versions differ")
    if manifest_metadata.get("artifact_version") != read_cff_value("version"):
        errors.append("artifact and CITATION.cff versions differ")
    if manifest_metadata.get("release_date") != read_cff_value("date-released"):
        errors.append("artifact and CITATION.cff release dates differ")
    release_count_fields = {
        "canonical_study_count": "canonical_study_count",
        "candidate_operation_count": "candidate_operation_count",
        "qualified_hpat_count": "qualified_hpat_count",
        "hpat_positive_study_count": "hpat_positive_study_count",
        "role_annotation_studies": "role_study_count",
    }
    for release_key, manifest_key in release_count_fields.items():
        if release_status.get(release_key) != manifest_metadata.get(manifest_key):
            errors.append(f"release-status mismatch for {release_key}")

    reliability = read_json("reliability/reliability_summary.json")
    if reliability.get("scope", {}).get("primary_sample_studies") != 45:
        errors.append("reliability sample denominator is not 45")
    if reliability.get("candidate_unitization", {}).get("paired_exact_candidate_matches") != 22:
        errors.append("paired candidate denominator is not 22")

    for path in ROOT.rglob("*"):
        if not path.is_file() or "scripts" in path.relative_to(ROOT).parts:
            continue
        if path.suffix.lower() in {".csv", ".md", ".json", ".cff", ".yml", ".txt"}:
            if ABSOLUTE_PATH.search(path.read_text(encoding="utf-8", errors="replace")):
                errors.append(f"absolute local path in {path.relative_to(ROOT).as_posix()}")

    manifest = ROOT / "MANIFEST.sha256"
    if not manifest.is_file():
        errors.append("missing manifest")
    else:
        for line in manifest.read_text(encoding="ascii").splitlines():
            if not line:
                continue
            expected_digest, relative = line.split("  ", 1)
            path = ROOT / relative
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected_digest:
                errors.append(f"manifest mismatch for {relative}")

    if errors:
        print("RELEASE VALIDATION FAILED")
        print("\n".join("- " + item for item in errors))
        return 1
    print("RELEASE VALIDATION PASSED")
    print(
        f"studies={len(studies)} candidates={len(candidates)} hpats={len(hpats)} "
        f"role_studies={len(hpat_studies)} reliability_sample=45"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
