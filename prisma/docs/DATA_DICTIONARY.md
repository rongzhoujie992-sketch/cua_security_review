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
- `fulltext/report_ledger_379.csv` — retrieval/report status for all preferred reports; `REPORT_NOT_RETRIEVED` identifies the single unretrieved report.
- `fulltext/report_version_consolidation_10.csv` — additional report-version resolution at full text.
- `fulltext/fulltext_eligibility_ledger_369.csv` — study-level full-text eligibility ledger after report resolution; `INCLUDE_REVIEW` identifies the 285 studies entering final review.
- `fulltext/fulltext_excluded_studies_83.csv` — studies excluded at initial full-text eligibility assessment.
- `author_adjudication/AUTHOR_ADJUDICATION_285.csv` — completed final-review decisions; `author_decision=KEEP` identifies the 222 retained studies and `DROP` the 63 exclusions.
- `fulltext/final_included_studies_222.csv` — final main systematic review corpus.

The full-text eligibility ledger contains 369 study-level rows: 368 assessed
studies (285 `INCLUDE_REVIEW` + 83 `EXCLUDE_REVIEW`) and one retained
`REPORT_NOT_RETRIEVED` record. The 378 assessed reports represent 368 studies
after consolidation of 10 duplicate or superseded report versions. Report-version
consolidation and substantive study exclusion are separate steps.

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

`reports/integrated_source_accounting_277.csv` records the main corpus and all
supplementary routes in the 277-source evidence base. TDES main-corpus
re-extractions remain in `tdes_branch/main_corpus_reextract_8.csv` and do not
add sources to this total.
