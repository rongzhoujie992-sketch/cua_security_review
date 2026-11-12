#!/usr/bin/env python3
"""Check ledger integrity and recompute counts from the public data."""
from pathlib import Path
from release_checks import release_report

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    actual = release_report(ROOT)
    if actual["errors"]:
        raise SystemExit("Ledger integrity checks failed: " + ", ".join(actual["errors"]))
    counts = actual["counts"]
    print(f"Ledger integrity: {len(actual['checks'])} checks passed")
    print(f"{counts['studies']} studies; {counts['candidates']} ledger rows ({counts['q1_established_candidate_operations']} Q1-established Candidates + {counts['source_unit_audit_rows']} source-unit audit rows); {counts['hpats']} HPATs; {counts['relations']} relations; {counts['evidence_artifacts']} artifacts")


if __name__ == "__main__":
    main()
