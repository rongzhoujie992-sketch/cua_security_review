# Integration Crosswalk

`corpus_alignment.csv` is the explicit bridge between the 226-study coding
population and the 222-study PRISMA component. The unified supplementary source
route is recorded separately in `supplementary_evidence_route.csv`.

`S-001` through `S-222` are the coding records for the 222-study PRISMA main systematic corpus. Each maps to one and only one `STUDY-*` row in `prisma/fulltext/final_included_studies_222.csv`.

`S-223` through `S-226` are the four selected supplementary TDES academic sources. They map to stable artifact IDs `TDES-ACA-001` through `TDES-ACA-004`, independent of manuscript bibliography numbering. They are outside the main systematic denominator but are included in the coding population because they were selected for source-grounded HPAT analysis.

The unified supplementary route contains 12 foundational/classical source
records, 9 TDES source records, and 34 post-cutoff study sources. Foundational
and official deployment documents remain source-route materials; they are not
mapped to Candidate or HPAT transitions. Together with the 222-study main corpus,
these routes form the [277-source evidence base](../prisma/reports/integrated_source_accounting_277.csv).

Mapping methods are recorded per row, with explicit identity reconciliations
and normalized-title matches where applicable.

For each of the 34 post-cutoff studies, `source_url` records its arXiv, DOI or
official conference publication page. `source_locator` preserves the original
PDF identifier used by the coding records. Use `coding_study_id` to connect a
coded source locator with its public publication page.

The existing `provenance/` tables contain both the original-corpus and the
supplementary process records, distinguished by `coding_population`.
Supplementary raw gate decisions retain their original decision IDs and
fields; relation adjudications are projected from the existing supplementary
relation ledger. The independent-comparison tables use the same population
field so their denominators remain separate.
