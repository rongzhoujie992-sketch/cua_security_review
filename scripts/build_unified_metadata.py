#!/usr/bin/env python3
"""Build the unified supplementary source route and source accounting."""
from __future__ import annotations

import csv
import argparse
from pathlib import Path
from tempfile import NamedTemporaryFile


def read(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        out = csv.DictWriter(handle, fieldnames=fields)
        out.writeheader()
        out.writerows(rows)


def publish(tables: list[tuple[Path, list[str], list[dict[str, str]]]]) -> None:
    """Stage both CSVs and restore originals if a replacement fails."""
    staged = {}
    originals = {}
    replaced = []
    try:
        for path, fields, rows in tables:
            originals[path] = path.read_bytes() if path.exists() else None
            with NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
                staged[path] = Path(handle.name)
            write(staged[path], fields, rows)
        for path, temporary in staged.items():
            temporary.replace(path)
            replaced.append(path)
    except Exception:
        for path in reversed(replaced):
            if originals[path] is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(originals[path])
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("supplement", type=Path, help="Supplementary source package to integrate")
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[1]
    supplement = args.supplement
    route_fields = ["route_source_id", "route", "source_type", "title", "source_locator", "coding_status", "coding_study_id", "scope_note", "source_url"]
    route: list[dict[str, str]] = []

    for row in read(repo / "prisma" / "foundational_branch" / "foundational_source_ledger.csv"):
        route.append({"route_source_id": row["canonical_id"], "route": "supplementary", "source_type": "foundational_classical", "title": row["title"], "source_locator": row["source_locator"], "coding_status": "source_route_only", "coding_study_id": "", "scope_note": "Conceptual or authoritative foundation; not a Candidate/HPAT coding unit."})
    for row in read(repo / "prisma" / "tdes_branch" / "selected_sources_9.csv"):
        source_type = "tdes_official" if row["Class"].lower().startswith("official") else "tdes_academic"
        study_id = {"TDES-ACA-001": "S-223", "TDES-ACA-002": "S-224", "TDES-ACA-003": "S-225", "TDES-ACA-004": "S-226"}.get(row["Source ID"], "")
        route.append({"route_source_id": row["Source ID"], "route": "supplementary", "source_type": source_type, "title": row["Source"], "source_locator": row["URL"], "coding_status": "coded_in_main_population" if study_id else "source_route_only", "coding_study_id": study_id, "scope_note": row["Boundary"]})
    selected = {row["Study_ID"]: row for row in read(supplement / "prisma" / "data" / "post_cutoff" / "selected_studies.csv")}
    for row in read(supplement / "prisma" / "source_manifest.csv"):
        study_id = row["study_id"]
        selected_row = selected.get(study_id, {})
        route.append({"route_source_id": study_id, "route": "supplementary", "source_type": "post_cutoff_study", "title": selected_row.get("Title", ""), "source_locator": row["relative_path"], "coding_status": "coded_in_unified_ledgers" if study_id != "B1-W007" else "source_reviewed_q1_not_established", "coding_study_id": study_id, "scope_note": "Post-cutoff source selected through the Dedup34 route.", "source_url": selected_row.get("Source_URL", "")})
    accounting = [
        {"component": "Final main CUA corpus", "count": "222", "unit": "study", "additive_to_unique_source_base": "YES", "note": "Systematic review corpus"},
        {"component": "Foundational/classical security branch", "count": "12", "unit": "source", "additive_to_unique_source_base": "YES", "note": "Separate theoretical/authoritative evidence route"},
        {"component": "TDES supplementary sources", "count": "9", "unit": "source", "additive_to_unique_source_base": "YES", "note": "Additive to the 222-study main corpus; the 4 academic sources are included in the 226-study coding population"},
        {"component": "Post-cutoff supplementary studies", "count": "34", "unit": "study", "additive_to_unique_source_base": "YES", "note": "Dedup34 selected source route"},
        {"component": "Final unique evidence/source base", "count": "277", "unit": "source", "additive_to_unique_source_base": "TOTAL", "note": "222 + 12 + 9 + 34"},
    ]
    from release_checks import release_report
    actual = release_report(repo, source_route=route, source_accounting=accounting)
    if actual["errors"]:
        raise SystemExit("Ledger integrity checks failed: " + ", ".join(actual["errors"]))
    publish([
        (repo / "integration" / "supplementary_evidence_route.csv", route_fields, route),
        (repo / "prisma" / "reports" / "integrated_source_accounting_277.csv", list(accounting[0]), accounting),
    ])
    print(f"Updated {len(route)} supplementary source-route records and unified source accounting.")


if __name__ == "__main__":
    main()
