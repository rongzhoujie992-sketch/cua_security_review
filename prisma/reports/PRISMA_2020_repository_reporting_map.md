# PRISMA 2020 repository reporting map

This repository documents the literature-search and study-selection records for the review.

| PRISMA 2020 item | Repository evidence | Status in this artifact |
|---|---|---|
| 5 Eligibility criteria | `protocol/eligibility_criteria.md`; `protocol/fulltext_role_aware_eligibility_codebook.md`; `author_adjudication/README.md` | Reported |
| 6 Information sources | `search/`; `reports/source_search_summary.csv`; `foundational_branch/`; `tdes_branch/` | Reported for each evidence route |
| 7 Search strategy | source-specific query/run logs and raw search snapshots in `search/`; supplementary query logs in branch directories | Reported |
| 8 Selection process | `protocol/selection_process.md`; screening/full-text/final-review ledgers | Reported |
| 16a Study selection | `reports/PRISMA_final_flow_counts_222.csv`; `figures/prisma_flow_final_222.svg`; included/excluded ledgers | Reported |
| 16b Excluded studies that may appear eligible | `fulltext/fulltext_excluded_studies_83.csv`; `author_adjudication/AUTHOR_DROPPED_63.csv`; controlled reason codebooks | Reported |
| 27 Availability of data/code/materials | repository ledgers, scripts, manifests, and checksums | Reported in repository |

## Flow-accounting check

```text
18,371 - 8,281 = 10,090
10,090 - 3 = 10,087
10,087 - 9,621 = 466
466 - 87 = 379
379 - 1 = 378
378 - 10 - 83 = 285
285 - 63 = 222
```

The separate foundational and TDES routes are supplementary evidence routes. They are reported independently and are not added to the 222-study main-corpus denominator.
