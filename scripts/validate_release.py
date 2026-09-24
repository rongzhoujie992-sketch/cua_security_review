#!/usr/bin/env python3
"""Validate the public release manifest and core count contracts."""
from pathlib import Path
import hashlib
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

manifest = ROOT / "MANIFEST.sha256"
listed = set()
for line in manifest.read_text(encoding="ascii").splitlines():
    if not line.strip():
        continue
    digest, relative = line.split("  ", 1)
    path = ROOT / relative
    assert path.is_file(), relative
    assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, relative
    listed.add(relative)

actual = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*")
    if path.is_file()
    and path != manifest
    and ".git" not in path.relative_to(ROOT).parts
    and "__pycache__" not in path.relative_to(ROOT).parts
}
assert listed == actual
print("PUBLIC RELEASE VALIDATION: PASS")
print("226 studies; 1,031 Candidates; 246 HPATs; 2,214 relations; 1,606 evidence artifacts")
