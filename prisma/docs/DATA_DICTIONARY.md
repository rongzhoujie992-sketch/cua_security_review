# Data dictionary

## Units

- **Occurrence**: one source-specific search-result occurrence.
- **Record**: globally deduplicated bibliographic identity entering title/abstract screening.
- **Report**: a concrete version/manifestation of a study (for example, a preprint and a formal version).
- **Study**: the intellectual contribution counted after report-version reconciliation.
- **Supplementary source**: a source used by a bounded supplementary evidence route but not counted as a main-corpus study.

## Main-search ledgers

- `dedup/global_occurrence_ledger.csv` — all identified source occurrences.
- `dedup/records_after_dedup.csv` — globally deduplicated records.
- `screening/title_abstract_screening_decisions.csv` — record-level screening outcomes and reasons.
- `screening/report_version_consolidation.csv` — pre-retrieval report-family resolution.
- `fulltext/report_ledger_379.csv` — retrieval/report status for all preferred reports.
- `fulltext/report_not_retrieved_1.csv` — the single report that could not be retrieved.
- `fulltext/report_version_consolidation_10.csv` — additional report-version resolution at full text.
- `fulltext/fulltext_eligibility_ledger_369.csv` — study-level full-text eligibility ledger after report resolution.
- `fulltext/fulltext_excluded_studies_83.csv` — studies excluded at initial full-text eligibility assessment.
- `fulltext/studies_entering_final_review_285.csv` — studies entering final review.
- `author_adjudication/AUTHOR_ADJUDICATION_285.csv` — completed final-review decisions.
- `fulltext/final_included_studies_222.csv` — final main systematic review corpus.

## Supplementary routes

### Foundational/classical security route
- `foundational_branch/foundational_prisma_accounting.csv`
- `foundational_branch/foundational_query_log.csv`
- `foundational_branch/foundation_raw_occurrences_126.csv`
- `foundational_branch/foundational_source_ledger.csv`
- `foundational_branch/foundational_sources_12.csv`

### TDES deployment-evidence supplement
- `tdes_branch/tdes_prisma_accounting.csv`
- `tdes_branch/main_corpus_reextract_8.csv`
- `tdes_branch/academic_candidates_16.csv`
- `tdes_branch/academic_not_selected_12.csv`
- `tdes_branch/official_documents_23.csv`
- `tdes_branch/selected_sources_9.csv`
- `tdes_branch/main_search_reconciliation_4.csv`

## Integrated accounting

`reports/integrated_source_accounting_243.csv` distinguishes main studies, supplementary sources, and non-additive TDES re-extractions.
