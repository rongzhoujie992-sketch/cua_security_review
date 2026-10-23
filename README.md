# CUA Security Review Reproducibility Artifact

This repository contains the machine-readable coding data and documentation for
the CUA security review.

## Scope and counts

- Codebook: HPAC/HPAT v3.3.0
- PRISMA systematic corpus: 222 studies
- Existing coding population: 226 studies (222 PRISMA studies plus 4 selected TDES academic sources)
- Post-cutoff supplement: 34 studies
- Unified coding population: 260 studies
- Candidate and eligibility rows: 1,238 each
- Qualified HPATs: 288 across 80 studies
- Relation records: 2,592 (9 per HPAT)
- Evidence artifacts: 1,826
- Unified evidence/source base: 277 source records (222 main-corpus study sources, 12 foundational sources, 9 TDES source records, and 34 post-cutoff study sources)

## Contents

- `data/`: Candidate, eligibility, HPAT, relation, and evidence ledgers.
- `prisma/`: search, screening, eligibility, PRISMA flow, and supplementary-source records.
- `integration/`: coding crosswalks and the unified supplementary evidence route.
- `provenance/`: coder matching and adjudication records.
- `reliability/`: coder-comparison tables and reliability diagnostics.
- `codebook/`: the coding manual used for the final projection.
- `validation.json`: release counts and structural checks.

Source locators use portable identifiers such as `source://S-001.txt` together
with page, section, figure, table, or line information. Reviewed-paper full
texts are not redistributed; the identifiers and locators support source
tracing.

An HPAT's `candidate_operation_id` resolves to a public Candidate record. For
supplementary rows, `canonical_unit_id` and `canonical_group_id` identify the
source unit, while `adjudicated_operation_id` and
`source_candidate_operation_ids` retain operation-level provenance.

The complete supplementary route is recorded in
`integration/supplementary_evidence_route.csv`. Foundational sources and
official deployment documents are source-route materials; the coding ledgers
contain the selected academic and post-cutoff study records. The original and
supplementary reliability denominators remain separate.

The PRISMA subpackage reports its own 243-source accounting (222 main studies,
12 foundational sources, and 9 TDES sources). The unified root release adds the
34 post-cutoff study sources and therefore reports 277 sources overall.

Run `python scripts/validate_release.py` from the repository root to recompute
the unified ledger counts and structural checks. The PRISMA component can be
validated independently with `python prisma/scripts/validate_release.py`; its
243-source result is limited to that component and is not the unified total.
