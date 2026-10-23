# Release 2.1.0

Released 2026-10-23. This release contains the PRISMA reproducibility materials
and the unified HPAC/HPAT v3.3.0 coding data for the CUA security review.

- Main systematic corpus: 222 studies
- Existing coding population: 226 studies (222 main-corpus studies plus 4 selected TDES academic sources)
- Post-cutoff supplement: 34 studies
- Unified coding population: 260 studies
- Candidate records: 1,238
- Qualified HPATs: 288 across 80 studies
- Relation records: 2,592
- Evidence artifacts: 1,826
- Supplementary evidence route: 55 source records (12 foundational/classical, 9 TDES, 34 post-cutoff study sources)
- Unified evidence/source base: 277 source records

The PRISMA component's own source accounting is 243 (222 main studies, 12
foundational sources, and 9 TDES sources). The unified release adds 34
post-cutoff study sources, giving 277 overall. Reliability files retain their
source-layered denominators; supplementary reliability is not pooled with the
original 226-study reliability population.

Reviewed-paper full texts are not redistributed. Run `python
scripts/validate_release.py` from the repository root to recompute and verify
the release counts and structural checks.
