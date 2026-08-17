# CUA Security Review — PRISMA Reproducibility Repository

**Public release:** 1.0  
**Release date:** 2026-08-15  
**Main-search eligibility cutoff:** 2026-07-31 inclusive

This repository publishes the reproducibility materials for a systematic review of computer-use-agent (CUA) security. It separates the **main systematic CUA corpus** from two supplementary evidence routes so that study counts and source counts remain explicit.

## Main systematic CUA corpus

| Stage | Count |
|---|---:|
| Records identified | 18,371 |
| Duplicate occurrences removed | 8,281 |
| Records after global deduplication | 10,090 |
| Other removals before screening | 3 |
| Records screened | 10,087 |
| Records excluded at title/abstract + admissibility screening | 9,621 |
| Retained report records before pre-retrieval version consolidation | 466 |
| Alternate report versions consolidated before retrieval | 87 |
| Reports sought for retrieval | 379 |
| Reports not retrieved | 1 |
| Reports assessed for eligibility | 378 |
| Duplicate/superseded report versions resolved at full text | 10 |
| Studies excluded after initial full-text eligibility assessment | 83 |
| Studies entering final review | 285 |
| Studies excluded after final review | 63 |
| **Studies included in the final main CUA corpus** | **222** |

```text
18,371 - 8,281 = 10,090
10,090 - 3 = 10,087
10,087 - 9,621 = 466
466 - 87 = 379
379 - 1 = 378
378 - 10 - 83 = 285
285 - 63 = 222
```

## Supplementary evidence routes

### Foundational / classical security route

```text
126 identification occurrences
→ 47 unique records screened
→ 22 reports assessed
→ 12 foundational sources included
```

These sources establish classical security concepts and remain outside the 222-study main-corpus denominator.

### TDES — targeted deployment-evidence supplement

Academic route:

```text
23 academic records reviewed in the executed search
+ 1 additional seed-source academic record
= 24 academic items handled

8 main-corpus studies re-extracted only (no additive count)
16 additional academic candidates assessed
→ 12 not selected
→ 4 supplementary academic sources selected
```

Official deployment documents route:

```text
12 provider families reviewed
→ 23 official deployment-document locators inspected
→ 5 official deployment documents selected
```

TDES contributes **9 supplementary sources** (4 academic + 5 official deployment documents) outside the main-corpus study count.

## Final source accounting

| Evidence route | Count |
|---|---:|
| Final main CUA corpus | 222 studies |
| Foundational/classical security route | 12 sources |
| TDES supplementary academic sources | 4 sources |
| TDES official deployment documents | 5 sources |
| **Final unique evidence/source base** | **243 sources** |

**243 is a source count, not a study count. The systematic main corpus remains 222 studies.**

## Repository structure

```text
search/                 source-specific search outputs and frozen query/run logs
dedup/                  occurrence-to-record normalization and deduplication
screening/              title/abstract screening, quality gate, and report-family resolution
fulltext/               retrieval, report-version resolution, and full-text eligibility
author_adjudication/    final decisions for the 285 studies entering final review
foundational_branch/    targeted 12-source classical/theoretical security route
tdes_branch/            targeted RQ4 deployment-evidence supplement
protocol/               eligibility, deduplication, and selection-process methods
reports/                PRISMA, PRISMA-S, exclusion, and integrated source accounting
figures/                main PRISMA flow and integrated evidence-route map
scripts/                 reconstruction/validation utilities
docs/                    data dictionary
```

## Key final files

- `fulltext/final_included_studies_222.csv`
- `fulltext/fulltext_excluded_studies_83.csv`
- `author_adjudication/AUTHOR_DROPPED_63.csv`
- `foundational_branch/foundational_sources_12.csv`
- `tdes_branch/selected_sources_9.csv`
- `reports/PRISMA_final_flow_counts_222.csv`
- `reports/PRISMA_2020_repository_reporting_map.md`
- `reports/PRISMA-S_reporting_map.md`
- `reports/integrated_source_accounting_243.csv`
- `figures/prisma_flow_final_222.svg`
- `figures/integrated_evidence_routes_243.svg`

## Final review

The final review included 222 studies and excluded 63. See `protocol/selection_process.md` and `author_adjudication/`.

## Reproducibility

Run:

```bash
python scripts/validate_release.py
```

The repository does not redistribute reviewed-paper full-text PDFs. See `THIRD_PARTY_NOTICE.md`.

## Copyright and permitted access

This repository is publicly accessible solely to permit inspection and verification of the review methods and materials reported in the associated paper. The author-created repository materials are not released under an open license; see `COPYRIGHT_NOTICE.md`. Third-party materials remain subject to their respective rights and terms.
