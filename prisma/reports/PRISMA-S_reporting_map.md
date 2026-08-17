# PRISMA-S search-reporting map

PRISMA-S is used here to structure reporting of the literature-search component. The main systematic search and the two supplementary evidence routes are documented separately so that information sources, search methods, counts, and deduplication remain traceable.

| PRISMA-S item | Reporting in this repository | Status |
|---|---|---|
| 1. Database name | `reports/source_search_summary.csv`; source-specific directories under `search/` identify Google Scholar, arXiv, ACL Anthology, and the ICLR official venue-check route. | Reported |
| 2. Multi-database searching | No simultaneous multi-database platform search was used; information sources were executed and logged separately. | Not used |
| 3. Study registries | No study registry was searched as part of the main systematic search. | Not used |
| 4. Online resources and browsing | Source-specific web/platform searches are logged under `search/`; official deployment-document searching is reported under `tdes_branch/`. | Reported |
| 5. Citation searching | No formal backward/forward citation-search route is counted in the main systematic identification total. | Not used |
| 6. Contacts | Authors, experts, manufacturers, and other parties were not contacted to identify additional main-corpus studies. | Not used |
| 7. Other methods | `foundational_branch/` reports the targeted classical-security route; `tdes_branch/` reports the targeted deployment-evidence supplement. | Reported |
| 8. Full search strategies | Exact/frozen query strings, query IDs, and run logs are provided for the main sources and both supplementary routes. | Reported |
| 9. Limits and restrictions | The eligibility cutoff and source-specific restrictions are documented in query/run logs and protocols; exclusions are separated from search-time restrictions. | Reported |
| 10. Search filters | No published methodological search filter was applied as a reusable filter. | Not used |
| 11. Prior work | No previous review's screened corpus was used as a public inclusion shortcut for the unified main search. Supplementary seed-source routes are explicitly reported where applicable. | Reported |
| 12. Updates | The repository reports the executed final search runs and their dates; no separate alert-based update process is claimed. | Reported |
| 13. Dates of searches | Dates are provided in source-specific run logs and supplementary branch search logs. | Reported |
| 14. Peer review | No independent peer review of the search strategy is claimed. | Reported as not performed |
| 15. Total records | Source-specific occurrence counts are reported in `reports/source_search_summary.csv`; the overall flow is reported in `reports/PRISMA_final_flow_counts_222.csv`. | Reported |
| 16. Deduplication | `protocol/deduplication_protocol.md`, `dedup/`, and `scripts/rebuild_dedup.py` document the occurrence-to-record deduplication process. | Reported |

## Main-search source accounting

```text
Google Scholar          4,210 occurrences
arXiv                  13,503 occurrences
ACL Anthology             657 occurrences
ICLR official venue check   1 occurrence
-------------------------------------------
Total                  18,371 occurrences
```

Search-engine total-hit estimates are not substituted for captured result-card/record counts when a source did not expose a stable exhaustive total.
