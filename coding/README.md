# HPAC/HPAT v3.1.2 Coding Artifact

This repository releases source-grounded coding for a 226-study computer-use-agent security corpus. Candidate Operations support eligibility and diagnostic analyses. Qualified High-Privilege Action Transitions (HPATs) are the sole atomic units for HPAC synthesis.

## Contents

- codebook/: the HPAC/HPAT coding contract
- data/: study, candidate, eligibility, HPAT, evidence, decision, control, and cross-transition records
- role/: non-exclusive threat, evaluation, and safeguard contribution annotations for HPAT-positive studies
- reliability/: blinded second-coder comparisons, unitization decisions, and adjudication records
- reports/: derived counts and relation-status summaries
- scripts/: release validation

## Interpretation

Candidate-wide counts are diagnostic and are not HPAT findings. Contribution-role labels are study-level and non-exclusive; only central labels support role-comparative summaries. The reliability records document the released paired coding and adjudication exercises and should be interpreted within their reported denominators.

## Coding responsibility

Zhoujie RONG (Rong Zhoujie), the manuscript author and first coder, completed the primary source coding, coder comparison, and final adjudication under the frozen codebook. Fang Jingran (Jingran Fang) independently completed the blinded second-coder exercises in reliability/. Candidate identification, HPAT eligibility, comparable relation fields, and contribution-role annotations were independently assessed in the released paired samples and then adjudicated under the corresponding frozen contracts.

## Validate

Run python scripts/validate_release.py.

The repository contains structured records and public source links. It excludes source PDFs, credentials, private communications, and exploit payloads.
