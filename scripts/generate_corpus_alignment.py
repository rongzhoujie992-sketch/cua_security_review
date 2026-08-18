#!/usr/bin/env python3
"""Generate the cross-package study/source alignment table."""
from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MANUAL_MAIN = {
    "S-003": "STUDY-170",
    "S-031": "STUDY-001",
    "S-060": "STUDY-308",
    "S-086": "STUDY-140",
    "S-095": "STUDY-153",
    "S-122": "STUDY-294",
    "S-131": "STUDY-239",
    "S-164": "STUDY-142",
    "S-173": "STUDY-202",
    "S-070": "STUDY-081",
    "S-085": "STUDY-208",
    "S-115": "STUDY-257",
}
TDES_SOURCE_IDS = {
    "S-223": "TDES-ACA-001",
    "S-224": "TDES-ACA-002",
    "S-225": "TDES-ACA-003",
    "S-226": "TDES-ACA-004",
}


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKC", value.replace("{", "").replace("}", "")).casefold()
    value = re.sub(r"\barxiv\s*:\s*\S+", " ", value)
    value = re.sub(r"[^\w]+", " ", value, flags=re.UNICODE)
    return " ".join(value.split())


def main() -> None:
    coding = read_csv("coding/data/study_records.csv")
    prisma = read_csv("prisma/fulltext/final_included_studies_222.csv")
    tdes = read_csv("prisma/tdes_branch/selected_sources_9.csv")

    by_title: dict[str, list[dict[str, str]]] = {}
    for row in prisma:
        by_title.setdefault(norm(row["title"]), []).append(row)
    tdes_by_id = {row["Source ID"]: row for row in tdes}

    rows: list[dict[str, str]] = []
    unresolved: list[tuple[str, str, int]] = []
    for study in coding:
        coding_id = study["study_id"]
        if coding_id in TDES_SOURCE_IDS:
            source_id = TDES_SOURCE_IDS[coding_id]
            source = tdes_by_id[source_id]
            rows.append(
                {
                    "coding_study_id": coding_id,
                    "coding_title": study["title"],
                    "coding_year": study["year"],
                    "coding_source_url": study["canonical_source_url"],
                    "corpus_scope": "tdes_supplementary_academic",
                    "source_key": source_id,
                    "source_title": source["Source"],
                    "source_year": study["year"],
                    "mapping_method": "explicit_tdes_source_mapping",
                    "mapping_note": "Supplementary academic source; outside the 222-study main-corpus denominator.",
                }
            )
            continue

        target_id = MANUAL_MAIN.get(coding_id)
        if target_id:
            target = next(row for row in prisma if row["study_id"] == target_id)
            method = "manual_identity_reconciliation"
            note = "Explicit reconciliation of coding and PRISMA identifiers after title/identity review."
        else:
            matches = by_title.get(norm(study["title"]), [])
            if len(matches) != 1:
                unresolved.append((coding_id, study["title"], len(matches)))
                continue
            target = matches[0]
            method = "exact_normalized_title_match"
            note = "Unique normalized-title match to the final PRISMA main-corpus record."
        rows.append(
            {
                "coding_study_id": coding_id,
                "coding_title": study["title"],
                "coding_year": study["year"],
                "coding_source_url": study["canonical_source_url"],
                "corpus_scope": "main_systematic_cua_corpus",
                "source_key": target["study_id"],
                "source_title": target["title"],
                "source_year": target["year"],
                "mapping_method": method,
                "mapping_note": note,
            }
        )

    if unresolved:
        for coding_id, title, count in unresolved:
            print(f"UNRESOLVED {coding_id} ({count} matches): {title}")
        raise SystemExit(f"{len(unresolved)} unresolved main-corpus identity mappings")

    output = ROOT / "integration/corpus_alignment.csv"
    output.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0])
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(rows, key=lambda row: int(row["coding_study_id"].split("-")[1])))
    print(f"WROTE {output.relative_to(ROOT).as_posix()} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
