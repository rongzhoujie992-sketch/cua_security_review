#!/usr/bin/env python3
from pathlib import Path
from collections import Counter
import csv

ROOT = Path(__file__).resolve().parents[1]

def rows(rel):
    with open(ROOT / rel, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

assert len(rows("dedup/global_occurrence_ledger.csv")) == 18371
assert len(rows("dedup/records_after_dedup.csv")) == 10090
screening = rows("screening/title_abstract_screening_decisions.csv")
screening_ids = {row["record_id"] for row in screening}
dedup_ids = {row["record_id"] for row in rows("dedup/records_after_dedup.csv")}
removed_ids = {row["record_id"] for row in rows("dedup/records_removed_before_screening.csv")}
assert len(screening) == len(screening_ids) == 10087
assert screening_ids == dedup_ids - removed_ids
assert sum(row["ta_decision"] == "EXCLUDE_TA" for row in screening) == 9621
assert sum(row["ta_decision"] in {"INCLUDE_TA", "UNCLEAR"} for row in screening) == 466
assert len(rows("screening/reports_sought_for_retrieval.csv")) == 379
assert len(rows("fulltext/report_ledger_379.csv")) == 379
fulltext = rows("fulltext/fulltext_eligibility_ledger_369.csv")
assert Counter(row["eligibility_status"] for row in fulltext) == {
    "INCLUDE_REVIEW": 285, "EXCLUDE_REVIEW": 83, "REPORT_NOT_RETRIEVED": 1,
}
assert len(rows("fulltext/fulltext_excluded_studies_83.csv")) == 83
adjudication = rows("author_adjudication/AUTHOR_ADJUDICATION_285.csv")
assert len(adjudication) == 285
assert Counter(row["author_decision"] for row in adjudication) == {"KEEP": 222, "DROP": 63}
main = rows("fulltext/final_included_studies_222.csv")
assert len(main) == 222
assert {row["study_id"] for row in main} == {
    row["study_id"] for row in adjudication if row["author_decision"] == "KEEP"
}

foundations = rows("foundational_branch/foundational_sources_12.csv")
assert len(foundations) == 12
assert len(rows("foundational_branch/foundation_raw_occurrences_126.csv")) == 126
assert len(rows("tdes_branch/main_corpus_reextract_8.csv")) == 8
assert len(rows("tdes_branch/academic_candidates_16.csv")) == 16
assert len(rows("tdes_branch/academic_not_selected_12.csv")) == 12
assert len(rows("tdes_branch/official_documents_23.csv")) == 23
tdes = rows("tdes_branch/selected_sources_9.csv")
assert len(tdes) == 9
assert Counter(row["Class"] for row in tdes) == {"Academic": 4, "Official deployment document": 5}
assert len(rows("tdes_branch/main_search_reconciliation_4.csv")) == 4

post_cutoff = [row for row in rows("../integration/supplementary_evidence_route.csv")
               if row["source_type"] == "post_cutoff_study"]
assert len(post_cutoff) == 34
source_total = len(main) + len(foundations) + len(tdes) + len(post_cutoff)
accounting = rows("reports/integrated_source_accounting_277.csv")
expected_accounting = {
    "Final main CUA corpus": len(main),
    "Foundational/classical security branch": len(foundations),
    "TDES supplementary sources": len(tdes),
    "Post-cutoff supplementary studies": len(post_cutoff),
    "Final unique evidence/source base": source_total,
}
assert len(accounting) == len(expected_accounting)
assert {row["component"]: int(row["count"]) for row in accounting} == expected_accounting
assert sum(int(row["count"]) for row in accounting
           if row["additive_to_unique_source_base"] == "YES") == source_total

print("RELEASE VALIDATION: PASS")
print("Main PRISMA: 18,371 -> 10,090 -> 10,087 -> 466 -> 379 -> 378 -> 285 -> 222")
print("Supplementary routes: 12 foundational + 9 TDES + 34 post-cutoff studies")
print(f"Final unique evidence/source base: {source_total}")
