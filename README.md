# CUA Security Survey Reproducibility Artifact

This versioned repository combines the reproducibility materials for the CUA security review and its HPAC/HPAT source-coding analysis. The two components remain internally separate so that review-flow counts, source counts, and coding populations cannot be confused.

## Components

- `prisma/` contains the PRISMA/PRISMA-S search, screening, report-family resolution, full-text eligibility, foundational route, and TDES supplementary evidence materials.
- `coding/` contains the HPAC/HPAT v3.1.2 manual codebook, public study and operation records, evidence ledger, contribution-role records, and bounded independent-coder comparison records.
- `integration/` contains the one-to-one crosswalk between the coding study records and the PRISMA evidence records.

## Population boundaries

The PRISMA main systematic corpus contains 222 studies. It is accompanied by 12 foundational security sources, 4 supplementary TDES academic sources, and 5 official deployment documents. These supplementary routes are source counts and are outside the 222-study denominator.

The coding component contains 226 study records: the 222 main-corpus studies plus four selected TDES academic sources identified by stable artifact IDs in `integration/corpus_alignment.csv`. Foundational sources and official deployment documents are not part of the HPAT coding population.

The released coding state contains 501 candidate operations and 282 qualified High-Privilege Action Transitions (HPATs) across 91 HPAT-positive studies. Candidate operations are diagnostic eligibility records; qualified HPATs are the atomic units for HPAC synthesis. The reliability directory reports the bounded paired samples and adjudication records supplied with the coding release.

Coder roles and name variants are documented in `coding/README.md` and `coding/reliability/README.md`.

## Reproduce the release checks

From the repository root:

```text
python scripts/validate_release.py
```

The top-level validator runs both child validators, verifies the 226-row crosswalk, checks the population boundaries, scans top-level public metadata for local paths and process-only disclosures, and verifies `MANIFEST.sha256`.

To regenerate the crosswalk from the released child tables:

```text
python scripts/generate_corpus_alignment.py
python scripts/validate_release.py
```

The reviewed-paper PDFs are not redistributed. Consult the notices in each component for licensing and third-party material terms.
