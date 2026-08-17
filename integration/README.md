# Integration Crosswalk

`corpus_alignment.csv` is the explicit bridge between the two release components.

`S-001` through `S-222` are the coding records for the 222-study PRISMA main systematic corpus. Each maps to one and only one `STUDY-*` row in `prisma/fulltext/final_included_studies_222.csv`.

`S-223` through `S-226` are the four selected supplementary TDES academic sources and map to reference labels `[235]` through `[238]`. They are outside the main systematic denominator but are included in the coding population because they were selected for the same source-grounded HPAT analysis.

The 12 foundational sources and 5 official deployment documents remain in the PRISMA component only. They are not coding-study records and are not mapped to HPAT transitions.

Mapping methods are recorded per row. Identity reconciliations are explicit; all other main-corpus matches are unique normalized-title matches. This file is an integration aid, not a replacement for either child ledger.
