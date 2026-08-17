#!/usr/bin/env python3
"""Validate the combined PRISMA and HPAC/HPAT public artifact."""
from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABSOLUTE_PATH = re.compile(r"(?:^|[^A-Za-z])[A-Za-z]:[\\/]|/mnt/|/Users/|\\\\")
FORBIDDEN_TOP_LEVEL_TERMS = (
    "incremental_4_canonical_study",
    "migration_derived",
    "calibration_sample",
    "AI screening",
    "Codex",
    "local workspace",
)


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def run_child_validator(component: str) -> list[str]:
    result = subprocess.run(
        [sys.executable, "scripts/validate_release.py"],
        cwd=ROOT / component,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return []
    return [f"{component} validator failed:\n{result.stdout}{result.stderr}"]


def main() -> int:
    errors: list[str] = []
    errors.extend(run_child_validator("prisma"))
    errors.extend(run_child_validator("coding"))

    try:
        manifest = json.loads((ROOT / "artifact_manifest.json").read_text(encoding="utf-8"))
        status = json.loads((ROOT / "release_status.json").read_text(encoding="utf-8"))
        coding = read_csv("coding/data/study_records.csv")
        alignment = read_csv("integration/corpus_alignment.csv")
        prisma = read_csv("prisma/fulltext/final_included_studies_222.csv")
        tdes = read_csv("prisma/tdes_branch/selected_sources_9.csv")
    except (OSError, json.JSONDecodeError, csv.Error) as error:
        print(f"COMBINED RELEASE VALIDATION FAILED\n- invalid input: {error}")
        return 1

    coding_ids = {row["study_id"] for row in coding}
    if len(coding) != manifest["integration"]["coding_study_count"]:
        errors.append("coding study count differs from combined manifest")
    if len(coding_ids) != len(coding):
        errors.append("coding study IDs are not unique")
    if len(alignment) != len(coding) or {row["coding_study_id"] for row in alignment} != coding_ids:
        errors.append("alignment does not cover the coding study records exactly once")

    main_rows = [row for row in alignment if row["corpus_scope"] == "main_systematic_cua_corpus"]
    tdes_rows = [row for row in alignment if row["corpus_scope"] == "tdes_supplementary_academic"]
    expected_main_ids = {f"S-{number:03d}" for number in range(1, 223)}
    if {row["coding_study_id"] for row in main_rows} != expected_main_ids:
        errors.append("main alignment does not cover S-001 through S-222 exactly")
    if len({row["source_key"] for row in main_rows}) != 222:
        errors.append("main alignment source keys are not unique")
    if {row["source_key"] for row in main_rows} != {row["study_id"] for row in prisma}:
        errors.append("main alignment does not cover the PRISMA included-study ledger exactly")

    expected_tdes = {"S-223": "[235]", "S-224": "[236]", "S-225": "[237]", "S-226": "[238]"}
    if len(tdes_rows) != 4:
        errors.append("TDES academic alignment must contain exactly four records")
    for row in tdes_rows:
        if expected_tdes.get(row["coding_study_id"]) != row["source_reference_label"]:
            errors.append(f"unexpected TDES mapping for {row['coding_study_id']}")
    selected_labels = {row["Reference label"] for row in tdes if row["Class"] == "Academic"}
    if {row["source_reference_label"] for row in tdes_rows} != selected_labels:
        errors.append("TDES alignment does not cover the four selected academic sources")

    if manifest["prisma"]["main_systematic_studies"] != 222:
        errors.append("combined manifest main-corpus count is not 222")
    if manifest["prisma"]["foundational_sources"] != 12:
        errors.append("combined manifest foundational count is not 12")
    if manifest["prisma"]["tdes_academic_sources"] != 4 or manifest["prisma"]["tdes_official_documents"] != 5:
        errors.append("combined manifest TDES counts are inconsistent")
    if manifest["coding"]["canonical_study_count"] != len(coding):
        errors.append("coding manifest study count is inconsistent")
    if status.get("artifact_version") != manifest.get("artifact_version"):
        errors.append("release status and artifact manifest versions differ")

    top_files = [
        path
        for path in ROOT.iterdir()
        if path.is_file() and path.name != "MANIFEST.sha256"
    ]
    top_files.extend(path for path in (ROOT / "integration").glob("*") if path.is_file())
    for path in top_files:
        if path.suffix.lower() not in {".md", ".json", ".csv", ".cff", ".yml", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if ABSOLUTE_PATH.search(text):
            errors.append(f"absolute local path in top-level file {path.relative_to(ROOT).as_posix()}")
        for term in FORBIDDEN_TOP_LEVEL_TERMS:
            if term.casefold() in text.casefold():
                errors.append(f"process-only term {term!r} in {path.relative_to(ROOT).as_posix()}")

    manifest_path = ROOT / "MANIFEST.sha256"
    if not manifest_path.is_file():
        errors.append("missing combined MANIFEST.sha256")
    else:
        listed: set[str] = set()
        for line in manifest_path.read_text(encoding="ascii").splitlines():
            if not line.strip():
                continue
            digest, relative = line.split("  ", 1)
            listed.add(relative)
            path = ROOT / relative
            if not path.is_file():
                errors.append(f"manifest points to missing file {relative}")
            elif hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"manifest mismatch for {relative}")
        actual = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*")
            if path.is_file()
            # Keep component manifests; exclude only this top-level manifest.
            and path != manifest_path
            and ".git" not in path.relative_to(ROOT).parts
            and "__pycache__" not in path.relative_to(ROOT).parts
        }
        if listed != actual:
            errors.append("combined manifest file set is incomplete or contains extra entries")

    if errors:
        print("COMBINED RELEASE VALIDATION FAILED")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("COMBINED RELEASE VALIDATION PASSED")
    print("PRISMA main corpus: 222 studies; foundational: 12; TDES: 4 academic + 5 official")
    print("Coding population: 226 study records; 501 candidate operations; 282 qualified HPATs")
    print("Alignment: 226 one-to-one coding-study mappings")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
