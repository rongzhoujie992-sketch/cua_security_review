# Search and study selection

## Search methods

The main systematic search used separately executed Google Scholar, arXiv,
and ACL Anthology searches, plus an ICLR official venue check. Exact query
strings, query identifiers, source-specific restrictions, execution dates,
and available raw snapshots are recorded under [search/](../search/).
The eligibility cutoff is 2026-07-31 inclusive. Search-time restrictions
and eligibility exclusions are recorded separately.

Identification counts describe captured search occurrences. Search-engine
hit estimates are not substituted for captured records where an exhaustive
total was unavailable. Source-specific counts appear in
[source_search_summary.csv](../reports/source_search_summary.csv).

Study registries, formal backward or forward citation searching, and
contact-based searches were not part of main-corpus identification. Searches
used the recorded query definitions rather than a published methodological
filter or a previously screened review corpus. The logs document the final
executed runs; no separate alert-based update process was used. The search
strategy was not independently peer reviewed.

The [foundational route](../foundational_branch/README.md) and
[deployment-evidence supplement](../tdes_branch/README.md) have their own
search logs, seed-source records, selection methods, and accounting.

## Screening and eligibility

Deduplication follows [deduplication_protocol.md](deduplication_protocol.md),
with occurrence-to-record mappings under [dedup/](../dedup/) and the
reconstruction script [rebuild_dedup.py](../scripts/rebuild_dedup.py).
Title/abstract screening follows
[eligibility_criteria.md](eligibility_criteria.md),
[title_abstract_screening_protocol.md](title_abstract_screening_protocol.md),
and the [scholarly admissibility criteria](scholarly_admissibility_and_quality_gate.md).
The complete [screening decision table](../screening/title_abstract_screening_decisions.csv)
retains the input bibliographic fields, decisions, and exclusion reasons.

Full-text assessment and report-version reconciliation follow the
[role-aware eligibility codebook](fulltext_role_aware_eligibility_codebook.md).
The retrieval, version-resolution, initial eligibility, and exclusion ledgers
are under [fulltext/](../fulltext/). The complete flow is recorded in
[PRISMA_final_flow_counts_222.csv](../reports/PRISMA_final_flow_counts_222.csv)
and the [combined search and evidence-route flow](../figures/prisma_flow.pdf).

## Final eligibility review

The author reviewed the 285 studies remaining after initial full-text
eligibility assessment: 222 were included and 63 were excluded.

| Exclusion reason | Studies |
|---|---:|
| `AUTHOR-E01-REDUNDANT` | 45 |
| `AUTHOR-E02-SCOPE` | 14 |
| `AUTHOR-E03-EVIDENCE` | 4 |

The records are provided in:

- [AUTHOR_ADJUDICATION_285.csv](../author_adjudication/AUTHOR_ADJUDICATION_285.csv): all final decisions; `KEEP` identifies the 222 retained studies and `DROP` the 63 exclusions, with reason codes and explanations.
- [final_included_studies_222.csv](../fulltext/final_included_studies_222.csv): the retained main corpus and source identifiers.
- [author_exclusion_reason_codebook.csv](../author_adjudication/author_exclusion_reason_codebook.csv): controlled reason definitions.
