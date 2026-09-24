# CUA Security Review Reproducibility Artifact

This repository contains the machine-readable coding data and documentation for
the CUA security review. It is intended for independent inspection and
reproduction of the reported coding and synthesis.

## Scope

- Codebook: HPAC/HPAT v3.3.0
- PRISMA main systematic corpus: 222 studies.
- Coding population: 226 studies, comprising the 222 main-corpus studies plus 4 supplementary TDES academic sources.
- Matching groups: 1,034
- Candidate records: 1,031
- Eligibility: 246 Established, 77 Indeterminate, 708 Not established
- Qualified HPATs: 246
- Relation records: 2,214 (9 relations per qualified HPAT)
- Evidence artifacts: 1,606
- Studies with qualified HPATs: 68

## Contents

- `data/`: Candidate, eligibility, HPAT, relation, and evidence ledgers.
- `prisma/`: search, screening, eligibility, PRISMA flow, and supplementary-source records.
- `integration/`: crosswalk linking the 226 coding studies to the 222-study main corpus and 4 supplementary TDES academic sources.
- `provenance/`: coder matching and adjudication records.
- `reliability/`: coder-comparison tables and reliability diagnostics.
- `codebook/`: the coding manual used for the final projection.
- `validation.json`: release counts and structural checks.

Source locators use portable identifiers such as `source://S-001.txt` and the
corresponding page, section, figure, table, or line information. Source papers
are not redistributed in this artifact; the study identifiers and locators are
provided so that reviewers can trace records to the cited source corpus.

The PRISMA flow ends at 222 studies. Four additional TDES academic sources
(`S-223`–`S-226`) are reported as a supplementary route and are included in the
226-study coding population; they are not added to the PRISMA main-corpus
denominator. The 12 foundational sources and 5 official deployment documents
are separate supplementary sources and are not part of the coding population.

The package's semantic projection and structural checks are complete; the
validation file records the checks and their results.

Run `python scripts/validate_release.py` from the repository root to validate
the public release manifest and core count contracts. The PRISMA component can
also be validated independently with `python prisma/scripts/validate_release.py`.
