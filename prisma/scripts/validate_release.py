#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib

ROOT = Path(__file__).resolve().parents[1]

def rows(rel):
    with open(ROOT / rel, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

assert len(rows("dedup/global_occurrence_ledger.csv")) == 18371
assert len(rows("dedup/records_after_dedup.csv")) == 10090
assert len(rows("screening/reports_sought_for_retrieval.csv")) == 379
assert len(rows("fulltext/report_ledger_379.csv")) == 379
assert len(rows("fulltext/fulltext_excluded_studies_83.csv")) == 83
assert len(rows("author_adjudication/AUTHOR_ADJUDICATION_285.csv")) == 285
assert len(rows("author_adjudication/AUTHOR_DROPPED_63.csv")) == 63
assert len(rows("fulltext/final_included_studies_222.csv")) == 222

assert len(rows("foundational_branch/foundational_sources_12.csv")) == 12
assert len(rows("foundational_branch/foundation_raw_occurrences_126.csv")) == 126
assert len(rows("tdes_branch/main_corpus_reextract_8.csv")) == 8
assert len(rows("tdes_branch/academic_candidates_16.csv")) == 16
assert len(rows("tdes_branch/academic_not_selected_12.csv")) == 12
assert len(rows("tdes_branch/official_documents_23.csv")) == 23
assert len(rows("tdes_branch/selected_sources_9.csv")) == 9
assert len(rows("tdes_branch/main_search_reconciliation_4.csv")) == 4

j = json.loads((ROOT / "reports/integrated_source_accounting_243.json").read_text(encoding="utf-8"))
assert j["main_systematic_cua_corpus"]["studies_included"] == 222
assert j["foundational_security_branch"]["sources_included"] == 12
assert j["tdes_branch"]["supplementary_academic_sources_selected"] == 4
assert j["tdes_branch"]["official_documents_selected"] == 5
assert j["tdes_branch"]["main_corpus_reextracts"] == 8
assert j["unique_source_accounting"]["tdes_main_corpus_reextracts_additive"] == 0
assert j["unique_source_accounting"]["final_unique_evidence_source_base"] == 243
assert 222 + 12 + 4 + 5 == 243

manifest = ROOT / "MANIFEST.sha256"
if manifest.exists():
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, rel = line.split("  ", 1)
        p = ROOT / rel
        assert p.exists(), rel
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected, rel

print("RELEASE VALIDATION: PASS")
print("Main PRISMA: 18,371 -> 10,090 -> 10,087 -> 466 -> 379 -> 378 -> 285 -> 222")
print("Supplementary routes: 12 foundational + 9 TDES")
print("Final unique evidence/source base: 243")
