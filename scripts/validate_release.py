#!/usr/bin/env python3
"""Validate the public release counts and core count contracts."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

status = json.loads((ROOT / "validation.json").read_text(encoding="utf-8"))
assert status["semantic_status"] == "COMPLETE"
assert status["structural_status"] == "PASSED"
assert status["counts"] == {
    "studies": 226,
    "prisma_main_corpus_studies": 222,
    "supplementary_tdes_academic_sources": 4,
    "matching_groups": 1034,
    "candidates": 1031,
    "eligibility_rows": 1031,
    "hpats": 246,
    "relations": 2214,
    "expected_relations": 2214,
    "evidence_artifacts": 1606,
}

print("PUBLIC RELEASE VALIDATION: PASS")
print("226 studies; 1,031 Candidates; 246 HPATs; 2,214 relations; 1,606 evidence artifacts")
