# Contribution-Role Coding Contract v1.0

Status: frozen role-annotation contract; independent comparisons and adjudication records are released separately. This freeze defines the terminology and
decision rules; it is not an inter-rater-reliability result.

Population: HPAT-positive studies supporting the qualified HPAT records in the release. This contract does not classify all 222 review studies.

Unit: one `study x contribution_role` record for each of `threat`,
`evaluation`, and `safeguard`. Each study therefore receives three records.
The labels are non-exclusive.

## Controlled Status Values

| Status | Meaning | Used in role comparisons |
|---|---|---|
| `central` | The study claims and substantively develops this contribution through a method, artifact, analysis, or reported result. | Yes |
| `supporting` | The study uses this role to validate another central contribution, but does not offer it as a contribution of its own. | No |
| `context_only` | The role appears in background, motivation, limitations, or future work only. | No |
| `not_present` | The source does not materially treat this role. | No |

Every `central`, `supporting`, and `context_only` judgment requires a source
locator. `central` additionally requires a concise source-grounded reason.

## Role Rules

### Threat contribution

Code `central` when the study introduces, characterizes, demonstrates, or
systematically analyzes an attack mechanism, vulnerability, exploitation
path, or security harm. The threat material must be claimed and developed as
a contribution, not only used as a benchmark scenario.

An attack-success experiment supporting a newly proposed attack is normally
`threat = central` and `evaluation = supporting`, unless the study also makes
a reusable benchmark, metric, or general measurement protocol contribution.

### Evaluation contribution

Code `central` when the study introduces a reusable benchmark, test protocol,
metric, dataset, evaluation environment, or systematic security measurement
whose evaluative function is itself a claimed contribution.

An attack or safeguard paper does not receive `evaluation = central` merely
because it reports ASR, task success, latency, ablations, or experiments.
Those are ordinarily `evaluation = supporting`.

### Safeguard contribution

Code `central` when the study proposes and substantively develops a control,
policy, enforcement mechanism, detector, monitor, containment mechanism, or
recovery mechanism, and reports its intended operation or validation.

A discussion of possible mitigations, a limitation section, or a future-work
proposal is `context_only`, not `safeguard = central`.

## Classification Procedure

1. Read the title, abstract, introduction contribution statement, method, and
   results or evaluation sections.
2. Code all three roles independently. Do not choose a primary role.
3. Distinguish a reusable or claimed contribution from an experiment that
   merely supports another contribution.
4. Record the shortest adequate locator and a decision reason.
5. Assign `other` only after the three role records are complete and none is
   `central`. `other` is a derived display label, not a fourth coded role.

## Boundary Examples

| Scenario | Correct coding |
|---|---|
| A new prompt-injection attack is tested with ASR across models. | `threat = central`; `evaluation = supporting` |
| A benchmark supplies attack scenarios and a reusable protocol but does not introduce a new attack. | `evaluation = central`; `threat = supporting` or `context_only` |
| A detector is tested against an established benchmark. | `safeguard = central`; `evaluation = supporting` |
| A system offers an attack taxonomy, a benchmark, and a validated guardrail. | More than one `central` label is permitted when each has its own claimed contribution and evidence. |
| The conclusion says future work should develop recovery. | `safeguard = context_only` unless a recovery control is developed in the study. |

## Public release note

The released role records use these rules for three non-exclusive contribution labels per HPAT-positive study. Bounded independent comparisons and adjudication records are provided separately under `reliability/`; they do not change the meaning of the role labels.
