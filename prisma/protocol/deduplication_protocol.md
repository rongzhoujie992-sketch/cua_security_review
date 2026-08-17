# Deduplication Protocol

Deduplication is performed at the report-record level before study-level version consolidation.

Rules are applied in deterministic order:

1. exact normalized arXiv base identifier;
2. exact ACL Anthology identifier;
3. exact normalized DOI for non-arXiv reports;
4. exact canonical report URL;
5. exact source-native identifier;
6. exact normalized title for compatible generic report copies;
7. explicit same-report-copy adjudication where report identity is known.

Fuzzy title similarity is not an automatic merge rule. Identifiable preprint/formal or submission/publication versions are retained as separate report records until later version consolidation.

The complete merge ledger is `dedup/dedup_edges.csv`; every removed duplicate occurrence is listed in `dedup/duplicate_occurrences_removed.csv`. The executable implementation is `scripts/rebuild_dedup.py`.
