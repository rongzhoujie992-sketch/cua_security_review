# Integration Crosswalk

`corpus_alignment.csv` is the explicit bridge between the 226-study coding
population and the 222-study PRISMA component. The unified supplementary source
route is recorded separately in `supplementary_evidence_route.csv`.

`S-001` through `S-222` are the coding records for the 222-study PRISMA main systematic corpus. Each maps to one and only one `STUDY-*` row in `prisma/fulltext/final_included_studies_222.csv`.

`S-223` through `S-226` are the four selected supplementary TDES academic sources. They map to stable artifact IDs `TDES-ACA-001` through `TDES-ACA-004`, independent of manuscript bibliography numbering. They are outside the main systematic denominator but are included in the coding population because they were selected for source-grounded HPAT analysis.

The unified supplementary route contains 12 foundational/classical source
records, 9 TDES source records, and 34 post-cutoff study sources. Foundational
and official deployment documents remain source-route materials; they are not
mapped to Candidate or HPAT transitions. The resulting unified evidence/source
base is 277 source records. The PRISMA component's separate accounting is 243
because it predates the 34 post-cutoff route.

Mapping methods are recorded per row, with explicit identity reconciliations
and normalized-title matches where applicable.
