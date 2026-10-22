#!/usr/bin/env python3
"""Validate the public release counts and core count contracts."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

status = json.loads((ROOT / "validation.json").read_text(encoding="utf-8"))
assert status["semantic_status"] == "COMPLETE"
assert status["structural_status"] == "PASSED"
assert status["counts"] == {
    "studies": 260,
    "prisma_main_corpus_studies": 222,
    "supplementary_tdes_sources": 9,
    "supplementary_foundational_sources": 12,
    "supplementary_post_cutoff_studies": 34,
    "evidence_source_base": 277,
    "candidates": 1238,
    "eligibility_rows": 1238,
    "hpats": 288,
    "relations": 2592,
    "expected_relations": 2592,
    "evidence_artifacts": 1826,
}
assert all(status["checks"].values())
assert status["coding_population"] == {"main_226_study_release": 226, "post_cutoff_added": 34, "unified": 260}
assert status["source_route"] == {"foundational_classical": 12, "tdes": 9, "post_cutoff": 34, "total_supplementary": 55, "overall_evidence_source_base": 277}

print("PUBLIC RELEASE VALIDATION: PASS")
print("260 studies; 1,238 Candidates; 288 HPATs; 2,592 relations; 1,826 evidence artifacts")
