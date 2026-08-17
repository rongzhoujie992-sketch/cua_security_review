# HPAC/HPAT v3.1.2 Coding Artifact

This repository releases manual source coding for a 226-study computer-use-agent security corpus. Candidate Operations support eligibility and diagnostic analyses. Qualified High-Privilege Action Transitions (HPATs) are the sole atomic units for HPAC synthesis.

## Contents

- `codebook/`: the HPAC/HPAT coding contract.
- `data/`: final study, candidate, candidate-audit, HPAT, evidence, decision, control, and cross-transition records.
- `role/`: non-exclusive threat, evaluation, and safeguard contribution annotations for HPAT-positive studies.
- `reliability/`: blinded second-coder comparisons, unitization decisions, and operation- and role-level adjudication records.
- `reports/`: deterministic derived counts and relation-status summaries.
- `scripts/`: release validation.

## Interpretation

Candidate-wide counts are diagnostic and are not HPAT findings. Role labels are study-level, non-exclusive annotations: only `central` labels support role-comparative summaries. Reliability values are bounded by the released paired denominators and are not extrapolated to the full corpus. Source locators, evidence statuses, qualifiers, and coder provenance bound the records.

## Coding responsibility

Zhoujie RONG (Rong Zhoujie), the manuscript author, completed the primary source coding, conducted the coder comparison, and made the final adjudication decisions under the frozen codebook. Fang Jingran (Jingran Fang) independently completed the blinded second-coder exercises reported in `reliability/`. The released records preserve this coder provenance without treating the paired samples as a full-corpus reliability estimate.

An independent second coder conducted a blinded review of a stratified 20% corpus sample under the frozen HPAT codebook. Candidate identification, HPAT eligibility, and comparable relation fields were independently assessed and subsequently adjudicated. Contribution-role annotations were independently checked and adjudicated on a separate blinded sample under the frozen role definitions. Full sampling, agreement, and adjudication records are available in `reliability/`.

## Validate

```powershell
python scripts/validate_release.py
```

The repository contains structured records and public source links. It excludes source PDFs, credentials, private communications, local workspaces, and exploit payloads.
