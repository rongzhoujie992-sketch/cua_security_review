# Search and study selection

**Main-search eligibility cutoff:** 2026-07-31 inclusive

This component contains the search and selection records for the CUA security
review. The main systematic corpus and the supplementary evidence routes
retain their respective study and source denominators.

## Main systematic CUA corpus

The identification-stage counts below are captured search occurrences from the
executed search records, not exhaustive raw-hit totals from every search
platform.

| Stage | Count |
|---|---:|
| Captured search occurrences identified | 18,371 |
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

TDES contributes **9 supplementary sources**: 4 academic sources and 5
official deployment documents. Eight main-corpus studies were also
re-extracted for deployment evidence without adding to the source count.
See [tdes_branch/README.md](tdes_branch/README.md) for selection methods,
route counts, and evidence scope.

## Final source accounting

| Evidence route | Count |
|---|---:|
| Final main CUA corpus | 222 studies |
| Foundational/classical security route | 12 sources |
| TDES supplementary academic sources | 4 sources |
| TDES official deployment documents | 5 sources |
| Post-cutoff supplementary studies | 34 studies |
| **Final unique evidence/source base** | **277 sources** |

The post-cutoff sources are recorded in the
[supplementary evidence route](../integration/supplementary_evidence_route.csv).
The eight TDES main-corpus re-extractions are already included in the 222 studies
and do not add to this total.

## Repository structure

```text
search/                 source-specific search outputs and frozen query/run logs
dedup/                  occurrence-to-record normalization and deduplication
screening/              title/abstract screening, quality gate, and report-family resolution
fulltext/               retrieval, report-version resolution, and full-text eligibility
author_adjudication/    final decisions for the 285 studies entering final review
foundational_branch/    targeted 12-source classical/theoretical security route
tdes_branch/            targeted deployment-evidence supplement
protocol/               eligibility, deduplication, and selection-process methods
reports/                flow counts, exclusion summaries, and source accounting
figures/                combined main-search and supplementary evidence-route flow (PDF)
scripts/                 reconstruction/validation utilities
docs/                    data dictionary
```

## Key final files

- `fulltext/final_included_studies_222.csv`
- `fulltext/fulltext_excluded_studies_83.csv`
- `author_adjudication/AUTHOR_ADJUDICATION_285.csv`
- `foundational_branch/foundational_sources_12.csv`
- `tdes_branch/selected_sources_9.csv`
- `reports/PRISMA_final_flow_counts_222.csv`
- [Search and selection methods](protocol/selection_process.md)
- `reports/integrated_source_accounting_277.csv`
- [Combined search and evidence-route flow](figures/prisma_flow.pdf)

## Reproducibility

From the repository root, run:

```bash
python prisma/scripts/validate_release.py
```

To reproduce the captured occurrence ledger and deduplication mappings in memory,
run `python prisma/scripts/build_occurrence_ledger.py` and
`python prisma/scripts/rebuild_dedup.py`. Both compare against the published
tables without writing additional files.

The complete screening decisions are in
`screening/title_abstract_screening_decisions.csv`, including the input
bibliographic fields and exclusion reasons.

## Copyright and permitted access

Citation and usage terms apply to the unified repository; see
[CITATION.cff](../CITATION.cff),
[COPYRIGHT_NOTICE.md](../COPYRIGHT_NOTICE.md), and
[THIRD_PARTY_NOTICE.md](../THIRD_PARTY_NOTICE.md).
