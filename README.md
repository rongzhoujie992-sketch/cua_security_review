# CUA Security Review Reproducibility Artifact

This repository accompanies *Computer-Use Agent Security: A Survey Through the Lens of the High-Privilege Action Chain*.

It provides source-grounded HPAC/HPAT coding for CUA security studies.
HPAC organizes the analysis around consequential operations. Each qualified
High-Privilege Action Transition (HPAT) is an operation-level unit with nine
separately coded relations: influence, authorization, technical permission,
operation execution, external effect, resulting state, technical attribution,
containment, and recovery. These records support cross-study comparison of
what sources report about operations, effects, state changes, attribution, and
post-effect controls.

## Scope and counts

- Codebook: HPAC/HPAT v3.3.0
- PRISMA systematic corpus: 222 studies
- Existing coding population: 226 studies (222 PRISMA studies plus 4 selected TDES academic sources)
- Post-cutoff supplement: 34 studies
- Unified coding population: 260 studies
- Candidate and eligibility ledger rows: 1,238 each, comprising 1,228
  Q1-established Candidate Operations and 10 source-unit audit records; those
  10 records are not Candidate Operations.
- Qualified HPATs: 288 across 80 studies
- Relation records: 2,592 (9 per HPAT)
- Evidence artifacts: 1,826
- Unified evidence/source base: 277 source records (222 main-corpus study sources, 12 foundational sources, 9 TDES source records, and 34 post-cutoff study sources)

## Evidence profile

Across 288 qualified HPATs, these counts show HPATs with positive source
evidence (`Present-direct` or `Present-partial`) among applicable HPATs. The
denominator excludes `Not applicable` and includes other applicable statuses,
such as `Not reported` and `Absent-explicit`.

| Relation | Source-positive HPATs / applicable HPATs |
| --- | ---: |
| External Effect | 243 / 287 |
| Resulting State | 202 / 286 |
| Containment | 34 / 255 |
| Recovery | 11 / 274 |

## Contents

- `data/`: Candidate, eligibility, HPAT, relation, and evidence ledgers.
- `prisma/`: search, screening, eligibility, PRISMA flow, and supplementary-source records.
- `integration/`: coding crosswalks and the unified supplementary evidence route.
- `provenance/`: coder matching and adjudication records.
- `reliability/`: independent coder-comparison tables and reliability statistics.
- `codebook/`: the coding manual used for the final projection.
- `scripts/`: source integration, data checks, and reproducible statistics.

Source locators use portable identifiers such as `source://S-001.txt` together
with page, section, figure, table, or line information. Reviewed-paper full
texts are not redistributed; the identifiers and locators support source
tracing. `integration/corpus_alignment.csv` supplies original-corpus source
URLs; `integration/supplementary_evidence_route.csv` supplies post-cutoff source
URLs while retaining the original PDF identifiers.

An HPAT's `candidate_operation_id` resolves to a public Candidate record. For
supplementary rows, `canonical_unit_id` and `canonical_group_id` identify the
source unit, while `adjudicated_operation_id` and
`source_candidate_operation_ids` retain operation-level provenance.

The complete supplementary route is recorded in
`integration/supplementary_evidence_route.csv`. Foundational sources and
official deployment documents are source-route materials; the coding ledgers
contain the selected academic and post-cutoff study records. The original and
supplementary reliability denominators remain separate.

The [unified source accounting](prisma/reports/integrated_source_accounting_277.csv)
reports all 277 sources across the main corpus and supplementary routes.

Matching and adjudication records cover both coding populations. The
`coding_population` field separates `original_226` from `post_cutoff_34`.
The adjudication ledger preserves the supplementary gate decisions and
projects its existing relation decisions; these have different record types
and must not be added together as Candidate counts.

Independent reliability uses 568 original-corpus semantic one-to-one pairs
and, separately, 67 supplementary pairs. The populations and their agreement
statistics are reported separately in the
[main-corpus reliability summary](reliability/reliability_summary.json) and
[supplementary reliability summary](reliability/supplementary_reliability_summary.json).

Run `python scripts/validate_release.py` from the repository root to recompute
the unified ledger counts and structural checks. Run
`python prisma/scripts/validate_release.py` to check study selection and the
277-source accounting across all routes.
`python scripts/test_release_checks.py` tests eligibility derivation,
agreement statistics, and ledger linkage. These commands read the data
directly and do not create report files.

Citation and usage terms are provided in [CITATION.cff](CITATION.cff),
[COPYRIGHT_NOTICE.md](COPYRIGHT_NOTICE.md), and
[THIRD_PARTY_NOTICE.md](THIRD_PARTY_NOTICE.md).
