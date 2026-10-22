# CUA Security Review Reproducibility Artifact

This repository contains the machine-readable coding data and documentation for
the CUA security review. It is intended for independent inspection and
reproduction of the reported coding and synthesis.

## Scope

- Codebook: HPAC/HPAT v3.3.0
- PRISMA main systematic corpus: 222 studies.
- Coding population: 260 studies, comprising the existing 226-study coding release plus 34 post-cutoff supplementary studies.
- Candidate records: 1,238
- Eligibility rows: 1,238
- Qualified HPATs: 288
- Relation records: 2,592 (9 relations per qualified HPAT)
- Evidence artifacts: 1,826
- Supplementary evidence route: 55 sources (12 foundational/classical, 9 TDES, 34 post-cutoff)
- Studies with qualified HPATs: 68

## Contents

- `data/`: Candidate, eligibility, HPAT, relation, and evidence ledgers.
- `prisma/`: search, screening, eligibility, PRISMA flow, and supplementary-source records.
- `integration/`: coding crosswalks and the unified supplementary evidence route.
- `provenance/`: coder matching and adjudication records.
- `reliability/`: coder-comparison tables and reliability diagnostics.
- `codebook/`: the coding manual used for the final projection.
- `validation.json`: release counts and structural checks.

Source locators use portable identifiers such as `source://S-001.txt` and the
corresponding page, section, figure, table, or line information. Source papers
are not redistributed in this artifact; the study identifiers and locators are
provided so that reviewers can trace records to the cited source corpus.

The PRISMA main flow remains 222 studies. The coding population is 260 studies:
the existing 226-study coding release plus 34 post-cutoff selected studies.
Foundational/classical sources, TDES sources, and post-cutoff studies are
listed together in `integration/supplementary_evidence_route.csv`. The 12
foundational sources and 5 official deployment documents remain source-route
evidence and are not Candidate/HPAT coding units. Reliability denominators
remain separated between the original main release and the supplementary run.

Run `python scripts/validate_release.py` from the repository root to validate
the public release counts and core count contracts. The PRISMA component can
also be validated independently with `python prisma/scripts/validate_release.py`.
