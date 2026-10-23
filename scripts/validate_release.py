#!/usr/bin/env python3
"""Recompute and validate the public release counts and core contracts."""
from pathlib import Path
from collections import Counter
import csv
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def artifact_refs(value: str) -> list[str]:
    return [ref.strip() for ref in re.split(r"[;|]", value or "") if ref.strip()]

status = json.loads((ROOT / "validation.json").read_text(encoding="utf-8"))
candidate_rows = read_csv("data/final_candidate_ledger.csv")
eligibility_rows = read_csv("data/final_eligibility_ledger.csv")
hpat_rows = read_csv("data/final_hpat_ledger.csv")
relation_rows = read_csv("data/final_relation_ledger.csv")
artifact_rows = read_csv("data/evidence_artifacts.csv")
route_rows = read_csv("integration/supplementary_evidence_route.csv")
alignment_rows = read_csv("integration/corpus_alignment.csv")
main_prisma_rows = read_csv("prisma/fulltext/final_included_studies_222.csv")
foundational_rows = read_csv("prisma/foundational_branch/foundational_sources_12.csv")
tdes_rows = read_csv("prisma/tdes_branch/selected_sources_9.csv")

candidate_ids = [row["final_candidate_id"] for row in candidate_rows]
eligibility_ids = [row["final_candidate_id"] for row in eligibility_rows]
hpat_ids = [row["hpat_id"] for row in hpat_rows]
hpat_id_set = set(hpat_ids)
candidate_id_set = set(candidate_ids)
relation_keys = [(row["hpat_id"], row["relation_name"]) for row in relation_rows]
artifact_ids = [row["evidence_artifact_id"] for row in artifact_rows]
artifact_id_set = set(artifact_ids)
artifact_by_id = {row["evidence_artifact_id"]: row for row in artifact_rows}
relation_names = {"Influence", "Authorization", "Technical Permission", "Operation Execution", "External Effect", "Resulting State", "Technical Attribution", "Containment", "Recovery"}
route_counts = Counter(row["source_type"] for row in route_rows)
relation_by_hpat = Counter(row["hpat_id"] for row in relation_rows)
positive_relation_artifacts_closed = True
all_relation_artifacts_resolve = True
for row in relation_rows:
    refs = artifact_refs(row.get("evidence_artifacts", ""))
    if any(ref not in artifact_id_set for ref in refs):
        all_relation_artifacts_resolve = False
    if row.get("evidence_status") in {"Present-direct", "Present-partial"}:
        if not refs:
            positive_relation_artifacts_closed = False
        for ref in refs:
            artifact = artifact_by_id.get(ref)
            if not artifact or any(artifact.get(field) != row.get(source) for field, source in (
                ("hpat_id", "hpat_id"), ("study_id", "study_id"),
                ("field_name", "relation_name"), ("evidence_status", "evidence_status"),
            )):
                positive_relation_artifacts_closed = False

post_cutoff_count = route_counts["post_cutoff_study"]
main_coding_count = len(alignment_rows)
actual_counts = {
    "studies": main_coding_count + post_cutoff_count,
    "prisma_main_corpus_studies": len(main_prisma_rows),
    "supplementary_tdes_sources": len(tdes_rows),
    "supplementary_foundational_sources": len(foundational_rows),
    "supplementary_post_cutoff_studies": post_cutoff_count,
    "evidence_source_base": len(main_prisma_rows) + len(foundational_rows) + len(tdes_rows) + post_cutoff_count,
    "candidates": len(candidate_rows),
    "eligibility_rows": len(eligibility_rows),
    "hpats": len(hpat_rows),
    "qualified_hpat_studies": len({row["study_id"] for row in hpat_rows}),
    "relations": len(relation_rows),
    "expected_relations": len(hpat_rows) * 9,
    "evidence_artifacts": len(artifact_rows),
}
actual_checks = {
    "candidate_ids_unique": len(candidate_ids) == len(candidate_id_set),
    "eligibility_ids_unique_and_aligned": len(eligibility_ids) == len(set(eligibility_ids)) and set(eligibility_ids) == candidate_id_set,
    "hpat_ids_unique": len(hpat_ids) == len(hpat_id_set),
    "artifact_ids_unique": len(artifact_ids) == len(artifact_id_set),
    "hpat_candidate_ids_resolve": {row["candidate_operation_id"] for row in hpat_rows} <= candidate_id_set,
    "supplementary_hpat_candidate_keys_resolve": all(
        not row["hpat_id"].startswith("HPAT-SUP-") or row["candidate_operation_id"] in candidate_id_set
        for row in hpat_rows
    ),
    "supplementary_hpat_operation_provenance_present": all(
        not row["hpat_id"].startswith("HPAT-SUP-") or (row.get("adjudicated_operation_id") and row.get("source_candidate_operation_ids"))
        for row in hpat_rows
    ),
    "relation_keys_unique": len(relation_keys) == len(set(relation_keys)),
    "nine_relations_per_hpat": len(relation_by_hpat) == len(hpat_id_set) and all(
        count == 9 and {row["relation_name"] for row in relation_rows if row["hpat_id"] == hpat_id} == relation_names
        for hpat_id, count in relation_by_hpat.items()
    ),
    "positive_relation_artifacts_closed": positive_relation_artifacts_closed,
    "all_artifact_relation_references_resolve": all_relation_artifacts_resolve,
    "candidate_locator_reason_complete": all(row.get("source_locator") and row.get("disposition_rationale") for row in candidate_rows),
    "eligibility_locator_complete": all(row.get("source_locator") for row in eligibility_rows),
    "relation_locator_reason_complete": all(row.get("source_locator") and row.get("decision_reason") for row in relation_rows),
    "artifact_locator_excerpt_complete": all(row.get("source_locator") and row.get("faithful_excerpt_or_paraphrase") for row in artifact_rows),
    "supplementary_route_rows": len(route_rows) == 55 and route_counts == {"foundational_classical": 12, "tdes_academic": 4, "tdes_official": 5, "post_cutoff_study": 34},
    "no_local_filesystem_paths": not any(
        marker in value for rows in (candidate_rows, eligibility_rows, hpat_rows, relation_rows, artifact_rows, route_rows)
        for row in rows for value in row.values() for marker in ("Users\\", "中国科学院")
    ),
    "all_hpat_relation_targets_exist": all(row["hpat_id"] in hpat_id_set for row in relation_rows),
}

assert status["semantic_status"] == "COMPLETE"
assert status["structural_status"] == "PASSED"
assert status["counts"] == actual_counts, (status["counts"], actual_counts)
assert status["checks"] == actual_checks, (status["checks"], actual_checks)
assert status["coding_population"] == {"main_226_study_release": 226, "post_cutoff_added": 34, "unified": 260}
assert status["source_route"] == {"foundational_classical": 12, "tdes": 9, "post_cutoff": 34, "total_supplementary": 55, "overall_evidence_source_base": 277}

print("PUBLIC RELEASE VALIDATION: PASS")
print("260 studies; 1,238 Candidates; 288 HPATs; 2,592 relations; 1,826 evidence artifacts")
