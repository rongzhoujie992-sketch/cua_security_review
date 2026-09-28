# HPAC/HPAT Codebook v3.3.0

Version: 3.3.0
Date: 2026-09-18
Scope: final frozen computer-use-agent security review corpus
Coding population: the final frozen CUA review corpus. Foundational security sources supply conceptual provenance and are excluded from the transition and HPAT denominators unless separately admitted as corpus studies under the frozen inclusion protocol.
Version 3.3.0 is the operational rule set used for the coding records in this release. It
retains the agreed HPAC/HPAT concepts, the Q4/Q5 privilege boundary, the nine relation names, the
evidence-status vocabulary, the population definitions, and the separation of historical records.
It reorganizes the definitions, Candidate lifecycle, unitization rules, and decision interfaces so
that the coding path follows one explicit sequence.

Records produced under earlier versions remain labeled by their original rule set; their provenance
is retained where applicable. Current release records use this version.

## 1. Scope and Coding Workflow

This codebook operationalizes the High-Privilege Action Chain (HPAC) as a source-grounded framework for comparing CUA security evidence. It distinguishes:

1. Study identity and source-level scope.
2. Source-native units and Candidate Operations used for HPAT eligibility.
3. Qualified High-Privilege Action Transitions (HPATs), the atomic units of HPAC synthesis.
4. The nine HPAT-level security relations.
5. Optional Cross-transition Relations and conditional control/context records.
6. Evidence Artifacts and source-grounded Decisions.
7. Derived tables, figures, and corpus summaries.

The codebook answers three separate questions:

1. What does the source report, and at what source-native unit?
2. Does a concrete operation satisfy the consequentiality, model-mediation, and independent privilege gates required for HPAT eligibility?
3. Which influence, authorization, permission, operation, effect, state, attribution, containment, recovery, and cross-transition relations does the source establish?

Mandatory principles:

- Preserve the source-native unit, condition, denominator, wording, and locator before interpretation.
- A study may have zero, one, or many candidates and zero, one, or many qualified HPATs.
- A candidate is not an HPAT until every eligibility gate is passed.
- Candidate Operations are eligibility objects; HPATs are the atomic transition units used for HPAC synthesis.
- Every source-native unit is reviewed at Q1. Every Candidate receives the source-grounded evidence
  needed for Q2-Q5 and the final eligibility outcome. A candidate-level audit Decision beyond Q1-Q5 is recorded only when the source explicitly
  reports a fact needed to explain a non-HPAT outcome or preserve a study-level reporting
  observation; it is not a default mirror of the nine relations.
- Only qualified HPATs receive the nine relation-status coding governed by Sections 4-5;
  Appendix A provides the corresponding HPAT record fields.
- Influence, authorization, technical permission, execution, external effect, resulting state, attribution, containment, and recovery are separate fields.
- Silence is not an absence finding.
- Aggregate results remain aggregate results; do not invent atomic operations from percentages or scores.
- Every judgment needs a source locator and decision reason.
- Display symbols and corpus percentages are derived, never hand-entered.

### Study review scope

A Study review scope is the declared set of studies, source packets, source versions, and source
locations that a coding pass must review. A `source_packet_id` identifies the fixed bundle of source
materials for a study; a `review_scope_id` and `review_scope_version` identify the scope used by the
pass. The scope records included studies, available full text, stable locators, and any unavailable
material. It is completion and provenance metadata, not a Candidate or an eligibility judgment.

Both coders use the same frozen review scope and source packets, but discover source-native units and
Candidates independently. A shared scope does not authorize copying a prior Candidate list, filtering
for likely HPATs, or using one coder's labels. If part of a packet is unavailable, record the limitation
and its locator; absence from an unreviewed range is not evidence that a predicate is not established.

### Coding workflow

Both coders independently follow the same path for every study in the frozen review scope:

~~~
verify source and locator
    -> identify source-native units and resolve split/merge (Section 2)
    -> apply Q1 (Section 3)
       -> Q1 fails: retain the source unit in the study completion record and stop for that unit
       -> Q1 satisfied: create a Candidate Operation
          -> apply Q2-Q5 independently (Section 3)
          -> retain candidate-level audit Decisions only when explicitly reported (Section 3)
          -> create an HPAT only when eligibility is Established
             -> code the nine HPAT relations (Sections 4-5, using Appendix A for record fields)
             -> record optional Cross-transition relations when applicable (Section 6)
          -> preserve evidence artifacts and decision provenance (Appendix A)
~~~

Do not begin with relation labels, expected counts, a previous Candidate list, or a disagreement list.
Unitization precedes eligibility; eligibility precedes HPAT relation coding; comparison and
adjudication occur only after both independent records are complete.

Use Section 2 for source units and split/merge, Section 3 for Q1-Q5 and eligibility, Sections 4-5
for the nine relation statuses, Section 6 for optional Cross-transition relations, and Section 8
for reliability and adjudication. Appendix A gives record fields, Appendix B gives validation and
release checks, and Appendix C is historical reference. These appendices do not create additional
semantic rules.

### High-Privilege Action Chain

HPAC is the macroscopic analytical structure used to follow security-relevant relations across a CUA
execution context. Its atomic units are qualified HPATs. It organizes the nine HPAT-level relations
and, where source-reported, the context or state linking one transition to another.

HPAC does not require every source to report every relation or to instantiate a complete end-to-end
chain. A source may contribute one Candidate, one qualified HPAT, one relation, a source-native
aggregate, or a partial chain.

### Protected resource

A protected resource is information, system state, service, identity-bound interface, account, credential, persistent memory, shared workspace, or principal-facing channel constrained by identity, credentials, technical permission, confidentiality expectation, delegation, or task policy.

Examples include private files, code repositories, browser sessions, cookies, tokens, forms, email, accounts, restricted APIs, CLI or GUI operations, MCP resources, persistent memory, shared workspaces, and multi-agent communication state. Public navigation and ordinary local interaction are not protected-resource access merely because a CUA performs them.

### Consequential operation

A consequential operation is a concrete operation that can do at least one of the following:

- read, disclose, transmit, or export protected information;
- create, modify, delete, submit, or transmit persistent or shared state;
- communicate, authenticate, commit, purchase, publish, or make a representation for a principal;
- invoke a service with an external or security-relevant side effect;
- change identity, permission, policy, credential, or delegated access;
- write state that can influence later decisions or actions;
- delegate a task, authority, or access to another actor.

Consequentiality is assessed at Q2. It does not establish model mediation, privilege, authorization, execution, effect, or state.

### Privilege-bearing capability

A privilege-bearing capability is an agent-available capability grounded in an identifiable identity-, credential-, session-, permission-, delegation-, or policy-based access relation to a protected resource, principal-bound interface or service, or policy-governed state relevant to the candidate's documented scenario. The privilege gate deliberately separates two judgments: Q4 establishes that a qualifying basis exists and is applicable to the candidate context; Q5 establishes that the concrete operation is connected to that basis. The exact operation-to-basis connection is therefore not required to establish the capability definition or Q4.

Operationally, Q4 requires source support for the qualifying access relation grounding the capability,
the resource, interface, service, or state governed by that relation, and the relation's availability
and applicability in the documented Candidate scenario. Technical availability alone is insufficient.
Controlled, simulated, sandboxed, or mocked settings are assessed by the same criteria.

Acceptable bases include:

- an identity-bound account or authenticated session;
- a credential, token, cookie, secret, API key, or signing key;
- a role, permission, resource scope, technical access-control rule, or policy-governed interface;
- a user- or system-configured delegated capability;
- a principal-bound service or protected-resource interface;
- authenticated or permission-governed access to an identified protected resource;
- authority to modify policy-governed persistent or shared state.

Consequentiality, harmfulness, external effect, state change, benchmark inclusion, a generic tool name, code execution, sandboxing, trust-boundary crossing, the paper's use of the word privileged, a task prompt, and a model refusal do not establish a privilege-bearing capability by themselves.

High privilege is not equivalent to root or administrator status, unauthorized use, harmfulness, or legal or ethical responsibility. A user-authorized email, private-file read, or form submission may still exercise a privilege-bearing capability.

In the name HPAT, `High-Privilege` denotes the security leverage created by an identity-, credential-, permission-, delegation-, principal-, or policy-governed access relation. It is not a severity score and does not require elevated operating-system privilege. The name is retained because the independent privilege gate now performs this distinction; consequentiality alone cannot satisfy it.

### High-Privilege Action Transition

An HPAT occurs when a concrete consequential operation, whether proposed, attempted, blocked, failed,
or executed, arises through model-mediated decision making and is linked by the source to an
identifiable privilege-bearing access relation.

An HPAT requires:

1. A concrete proposed, attempted, blocked, failed, or executed operation.
2. An identifiable target, resource, recipient, object, or relevant postcondition.
3. Consequentiality under the Consequential operation definition in this section.
4. Source-supported model mediation and privilege-bearing linkage under Section 3.

HPAT eligibility does not require valid authorization, fully reported technical permission scope, operation execution, an external effect, a resulting state, or successful recovery. Those are separately coded relations.

### Candidate operation

A Candidate Operation is created when Q1 confirms a concrete operation after source-unit
identification and any required split/merge resolution. The Candidate Operation is retained for
Q2-Q5 HPAT eligibility review.

Candidate Operations are eligibility objects, not HPATs or independent transition units. Candidates
that fail model mediation or privilege linkage remain in the audit ledger with the failing status;
they are not silently deleted.

### Empirical chain instance

An empirical chain instance is a source-supported sequence of one or more HPATs and/or source-established context or state nodes connected by a relation. A single HPAT may stand alone when no cross-transition relation is established.

### Study-level aggregate

A study-level aggregate is a source-native count, percentage, category, score, or qualitative result
covering multiple units. It is represented by a study-level decision and denominator metadata. It is
not converted into a fabricated transition. Candidate boundaries are controlled by Section 2; this
definition does not authorize reverse-splitting an aggregate into operations or HPATs.

## 2. Unitization and Candidate Discovery

### Source unit types

source_unit_type is one of:

~~~
runtime_trace
scenario_walkthrough
task_table_row
source_native_aggregate
architecture_description
formal_or_verifier_test
other
~~~

source_extraction_unit_id must identify an actual source unit or locator, such as a named table row, figure step, trace segment, scenario, appendix item, algorithm, protocol test, or page-local passage. A generated row number is not a source locator.

### Split, merge, and aggregate rules

Apply these rules before Q1-Q5 and before creating any HPAT.

1. **Source unit.** Identify each source-reported unit that can be located directly in the source and
   may contain an operation: a table row, scenario, trace segment, figure step, protocol test,
   appendix item, or equivalent source unit. Start from the source's reporting units; do not fragment
   a unit into the smallest locatable phrase merely because a locator can be made more precise. A
   generated row number is not a source locator.
2. **Default unit.** After the source unit is identified, treat a source row, scenario, or trace
   segment as one Candidate representation only when the source reports it as one operation unit and
   Q1 confirms a concrete operation. Source-unit identification therefore precedes Q1: a source row
   is not automatically a Candidate, and a Q1-failing unit remains only in the study completion
   record. Do not split alternatives, repeated runs, or side effects merely because they appear as
   separate phrases within the same source unit.
3. **Split.** Create separate Candidates only when the source separately locates, labels, or reports
   each resulting unit and each resulting unit independently satisfies the Q1 operation predicate.
   A different actor, principal, delegation context, or authorization basis; a different protected
   target, recipient, resource, or permission scope; a different operation type or independently
   verified postcondition; a distinct control, containment, or recovery endpoint; or an independently
   reported outcome may support a split only when the source presents it as a distinct operation,
   condition, or outcome unit. Do not complete relation coding to decide a Candidate boundary. A
   difference in relation status, tool name, task label, or possible side effect alone is not
   sufficient to split the unit.
4. **Merge.** Keep multiple clicks, calls, or low-level steps as one Candidate when the source
   presents them as inseparable steps of one source-native operation and does not separately identify
   an actor, principal, delegation context, target/resource, operation, condition, or independently
   reported outcome. Preserve lower-level steps as evidence artifacts. Differences found only while
   assigning relation status do not block a merge; an independently reported outcome or source
   operation remains a split condition.
5. **Conditions and repeated runs.** Baseline, guarded, attacked, repaired, repeated, or
   model-specific runs remain conditions of one Candidate when the actor, operation, target,
   privilege basis, and reported postcondition are unchanged. Split them only when one of those
   elements changes or the source supplies an independent operation locator or postcondition oracle;
   a relation-status difference alone does not split repeated runs.
6. **Aggregates and parent-child reporting.** A source-native aggregate remains one aggregate source
   unit. Do not reverse-split it from a percentage, score, benchmark-wide rate, or family-level
   result. If the source separately reports child operation units, retain those children only when
   they satisfy the split rule above. The parent scenario or aggregate is not an additional
   Candidate when it merely groups or summarizes those children; retain it separately only when the
   source presents it as an independent operation with its own operation predicate, target, resource,
   recipient, object, condition, or postcondition. A row that separately reports deletion,
   modification, permission change, and service disruption must not be collapsed into a generic shell
   operation.
7. **No coder-selected sampling.** Candidate discovery is exhaustive within the distinct
   source-reported operation units or operation classes made available for review. Representative
   sampling by the coder is not permitted.
8. **Unresolved boundary.** If the source does not permit a stable boundary without invention,
   retain the source unit as unresolved and record the reason. Do not force a Candidate count or
   fabricate an HPAT.

### Candidate discovery population and reporting layers

Within a declared review scope, Candidate discovery is exhaustive over the distinct source-reported
operation units or operation classes made available for review. One source-reported operation should
have one Candidate representation unless the source independently reports a distinct operation
boundary under the split rules above. Locator granularity does not determine Candidate granularity:
several locators may support one Candidate, and a single locator may contain multiple Candidates only
when the source separately reports their boundaries.

The same operation may be described at several reporting layers, such as a table, a narrative
example, and an appendix. Do not create duplicate Candidate representations merely because the
operation is repeated at those layers. Conversely, do not demote every general description to context
or aggregate merely because concrete examples are also present. A parent scenario or aggregate that
merely groups separately reported child operations is context or aggregate evidence, not another
Candidate. Retain it as a separate Candidate only when the source presents it as an independent
operation with its own operation predicate and target, resource, recipient, object, condition, or
postcondition.

A taxonomy, dimension, impact-category, capability, payload, or attack-objective row is not a
source-native operation class merely because its label describes what a skill or agent may attempt.
A source-defined operation class enters Candidate discovery only when the source uses it as a
behavioral operation unit and identifies an operation type together with a target, resource,
recipient, object, or relevant postcondition in a source-reported scenario, condition, or reporting
unit sufficient for Q1 evaluation. Otherwise retain the row as study-level taxonomy or aggregate
evidence. Only the qualifying operation unit or operation class enters Candidate discovery.

Candidate boundaries are finalized before Q2-Q5 and before relation coding. If later source review
reveals a genuine missed or wrongly merged source-native operation boundary, return explicitly to Pass
1 and record a unitization correction. That correction is not an eligibility-driven boundary change.

### Boundary examples

Use the following defaults when a source unit could be read in more than one way:

- **End-to-end scenario.** Keep one end-to-end scenario as one Candidate when the source presents
  the steps as one model-mediated operation and does not separately identify a distinct operation,
  target, condition, or independently reported outcome. Split only when the source independently
  locates or reports one of those units.
- **Alternatives in one table row.** Keep alternatives in one Candidate when they share one row and
  the source does not separately identify their operations or outcomes. Split them only when the row
  separately reports the alternatives as distinct units.
- **Appendix item.** Record an appendix demonstration as a separate Candidate only when the appendix
  independently reports a concrete operation and its target, recipient, object, condition, or relevant
  postcondition. A worked example that merely illustrates the main operation stays with that source
  unit.
- **Endpoint action.** Keep an endpoint action with the preceding steps when the source treats the
  sequence as one operation. Record it separately only when the endpoint is independently located or
  reported as a distinct operation, target/condition, or outcome unit.
- **Side effect.** A side effect remains evidence for the same Candidate unless the source reports it
  as a separate operation or an independently reported outcome. A possible side effect alone does not
  create a new Candidate.
- **Source-native aggregate.** Keep a source-reported count, rate, score, or family result as one
  aggregate source unit. Do not reverse-split it into operations; separately identified source units
  may still be recorded separately under rule 6.

### Stored unitization values

After the Candidate boundary is fixed, assign `source_native_atomicity` as:

~~~
single_operation
source_aggregate
unresolved
~~~

`single_operation` means that the source resolves one operation and its target or postcondition.
`source_aggregate` means that the source deliberately reports a family of variants as one unit.
`unresolved` means that the source does not permit stable atomicity without invention.

`source_native_atomicity` describes the source unit. It is distinct from the later
`transition_record_granularity`, which describes how an established HPAT is represented under
Appendix A. Aggregate evidence limits are governed by Section 4 and do not redefine the
Candidate boundary.

Candidate boundaries are controlled by the split, merge, and aggregate rules in Section 2. Do not apply a
separate split or merge rule after HPAT creation. Once a Candidate boundary is fixed, the HPAT
record inherits that source-native unit; relation evidence may be partial or aggregate-aligned
without creating a new Candidate.

For source-native aggregate results, record:

~~~
aggregate_target
included_record_ids[]
included_record_types[]
source_native_categories[]
numerator
denominator
denominator_unit
aggregation_rule
source_native_metric
coverage_qualifier
~~~

coverage_qualifier values are single_scenario, subset, systematic, design_only, and unknown.

Never infer a single operation, effect, state, or recovery outcome from a percentage or aggregate score.

## 3. HPAT Eligibility

### Eligibility rules

Apply the gates in order and record each gate independently. A later gate cannot repair an earlier
failure, and Q4 and Q5 must not be mechanically synchronized.

| Gate | Question | Pass condition | Failure or uncertainty |
|---|---|---|---|
| Q1 | Is there a concrete operation? | Operation type plus target, resource, recipient, object, or relevant postcondition is located in the source unit. | No Candidate record; retain the source unit in study completion records. |
| Q2 | Is the operation consequential? | The operation can affect protected information, persistent/shared state, a principal-facing action, a security-relevant service, access/policy, later decisions, or delegated capability. | `q2_gate=Not established` or `Indeterminate`; Candidate retained. |
| Q3 | Is the operation model-mediated? | The source connects model interpretation, planning, selection, or generated action choice to the operation. | `q3_gate=Not established` or `Indeterminate`; no Established HPAT. |
| Q4 | Does an applicable privilege basis exist? | The source establishes a qualifying access relation, the resource/interface/service/state governed by that relation, and the relation's availability and applicability in the Candidate scenario. | `q4_gate=Not established` or `Indeterminate`; Q5 is still recorded separately. |
| Q5 | Is the operation linked to that basis? | The source connects the concrete operation to the Q4 basis, explicitly or through deterministic aligned evidence. | `q5_gate=Not established` or `Indeterminate`; do not infer from verbs, labels, tools, or effects. |

For an existing Candidate Operation, the coder records `q2_gate`, `q3_gate`, `q4_gate`, and
`q5_gate`. These four fields are the only authoritative eligibility inputs. Their semantic
projections are fixed as follows:

| Gate value | Q2 semantic projection | Q3 semantic projection |
|---|---|---|
| Established | `consequential` | `established` |
| Not established | `not_consequential` | `not_established` |
| Indeterminate | `indeterminate` | `indeterminate` |

`hpat_eligibility` is derived from the four gates: all four `Established` yields `Established`; any
`Not established` yields `Not established`; otherwise it yields `Indeterminate`. Q1 is the entry
condition that created the Candidate. Q4/Q5 evidence does not populate Technical Permission or any
of the nine relation fields automatically.

~~~
source-native unit
    -> resolve split/merge
    -> apply Q1
       -> Q1 fails: retain the source unit in the study completion record; do not create a Candidate
       -> Q1 satisfied: create a Candidate Operation
          -> apply Q2-Q5 independently
          -> retain candidate-level audit Decisions only when explicitly reported
             -> all required gates Established: create a qualified HPAT and perform full relation coding
             -> a later gate Not established or Indeterminate: retain the Candidate Operation; do not create a transition
~~~

The gates are applied in this order. A later gate cannot justify an earlier candidate. The privilege
decision determines HPAT membership. Candidate-level audit Decisions preserve
explicit reporting evidence without assigning transition status to a non-HPAT Candidate.

### Q1: concrete operation

The source must report a proposed, attempted, blocked, failed, or executed operation located in a source-native unit. The operation must identify an operation type and a target, resource, recipient, object, or relevant postcondition.

A generic task, tool description, attack name, unsafe score, or model output without an operation is insufficient.

For a source-defined operation class, the class itself must satisfy the same Q1 predicate. A class
label without an identifiable operation type and target, resource, recipient, object, or relevant
postcondition remains a taxonomy or aggregate observation and does not create a Candidate.

If Q1 fails, do not create a candidate record. Record the source-native unit in the study completion record with `candidate_discovery_status=no_candidate_operation` and its locator and reason. `candidate_operation_status` is not a field in the candidate schema.

### Q2: consequentiality

The operation must meet the Consequential operation definition in Section 1. A response, search,
lookup, diagnosis, permission question, recommendation, or other information-processing event is not
consequential merely because it concerns security or is produced by a model. It may still pass Q2 when
the source shows that the operation reads or discloses protected information, commits an externally
directed action or representation, changes persistent or shared state, invokes a security-relevant
service, changes access or policy, or satisfies another predicate in the Section 1 definition. A
model response delivered only to the requesting user does not by itself satisfy the externally directed
representation predicate, but it may pass Q2 when it discloses protected information or meets another
consequential-operation predicate. This is an application of the existing definition, not a blacklist
of information-processing operations.

Wrong answers, refusal behavior, generic unsafe scores, ordinary public navigation, a tool description,
and a benchmark label are excluded unless the source reports a distinct operation and consequential
target or postcondition.

Set `q2_gate=Not established` when the operation fails the Consequential operation definition and
retain the rationale. The derived `consequentiality_status` is then `not_consequential`. If the
source cannot resolve consequentiality, set `q2_gate=Indeterminate`, which derives
`consequentiality_status=indeterminate`. The study may still contribute methodological, reliability,
or contextual evidence.

### Q3: model mediation

`q3_gate` has three values:

| Value | Rule | Derived `model_mediation_status` |
|---|---|---|
| Established | The source connects model interpretation, planning, selection, or model-generated action choice to the concrete operation. | `established` |
| Not established | The operation is assigned to a human, static script, deterministic protocol routine, benchmark generator, stochastic procedure, verifier, or other non-model actor. | `not_established` |
| Indeterminate | The issuing actor or mechanism cannot be distinguished. | `indeterminate` |

The following do not establish model mediation alone: a task prompt; a tool or service description; an architecture diagram; a policy-selection output when the protected operation is not executed; a browser-automation proxy used instead of a compromised model; a verifier or conformance test; and automatic logging, signing, or completion.

Only `q3_gate=Established` may proceed to an HPAT eligibility decision of `Established`.

Study-level model-mediation evidence may support Q3 for a Candidate when the source explicitly assigns
the same model-mediated interpretation, planning, or action-selection mechanism to the same task or
scenario family. Inherit that evidence only when the identity of the model/mechanism and the task or
scenario family are aligned; a model name, architecture diagram, or study label alone is insufficient.
If that alignment cannot be established, judge Q3 from Candidate-specific evidence or use
`Indeterminate`.

### Q4: privilege-basis existence and applicability

Q4 asks whether the source establishes a qualifying privilege basis that is available and applicable
in the documented Candidate scenario. Q4 concerns the existence and applicability of the basis; it
does not yet require the concrete operation to be linked to that basis.

Set `q4_gate=Established` only when the source supports all three of the following:

1. a qualifying access relation grounded in identity, credential, session, permission, delegation,
   or policy;
2. the resource, interface, service, or state governed by that relation; and
3. the availability and applicability of that relation in the documented Candidate scenario.

Record the basis type, governed resource/interface/service/state, and source locator. Evidence may be
assembled across an environment description, account or session setup, credential or permission
configuration, tool or API schema, task table, and trace when those materials unambiguously refer to
the same scenario. Q4 does not require the basis and Candidate Operation to appear in the same sentence.

Technical availability alone does not establish Q4. A tool, GUI, browser, filesystem, shell, sandbox,
emulator, helper, mock service, configured runtime, administrator label, task label, benchmark label,
or other executable facility is insufficient unless the source also establishes the qualifying access
relation and the resource/interface/service/state governed by it in the Candidate scenario. Likewise,
naming a private file, account, key, state object, protected target, or policy-relevant object identifies
a possible target; it does not by itself establish the relation through which that target is available.
An explicit statement that an agent has full, unrestricted, or configured access to a local or
system-level resource is evidence of technical availability; it does not itself establish the
qualifying access relation required for Q4 or permit selection of `configured_capability`.

Controlled, simulated, sandboxed, or mocked environments are neither automatically qualifying nor
automatically disqualifying. They may establish Q4 when the source models the same qualifying relation,
governed resource/interface/service/state, and scenario applicability required in any other setting.
Production deployment, a real victim, or a literal password or token is not required.

After complete review of the declared study review scope, set `q4_gate=Not established` when the source
does not establish the required qualifying relation, or affirmatively establishes that the Candidate
uses a public or unprotected path. This is an evidence judgment about the reviewed source, not a claim
that such a capability could not exist in the real system. Set `q4_gate=Indeterminate` when affirmative
basis-relevant evidence exists but the relation, governed resource/interface/service/state, availability,
or scenario applicability is conflicting, ambiguous, or cannot be resolved. Mere absence of a qualifying
basis after complete review is not by itself `Indeterminate`; absence from an unreviewed source range
must not be used for `Not established`. Do not require the literal words `privilege`, `credential`,
`password`, `token`, or `permission` when the required relation is otherwise source-supported.

### Q5: operation-to-capability linkage

Q5 asks whether the source establishes a link between the concrete Candidate Operation and the privilege
basis judged at Q4. Q5 concerns the operation-to-basis connection; it does not re-decide whether the
basis itself qualifies under Q4. Q4 and Q5 remain separately evidenced judgments, and Q5 must still be
recorded when Q4 is `Not established` or `Indeterminate`.

Set `q5_gate=Established` only when the source connects the concrete operation to an Established Q4
basis. The connection may be explicit in one source location or deterministically assembled across
environment, identity or session, permission configuration, tool or API schema, task, and trace records
when the alignment checks below are satisfied. A source-native task table, designed scenario, controlled
environment, mock service, or harness may support Q5 when it explicitly connects the operation to that
basis. Design-level or proxy limitations are recorded in the separate evidence status and qualifier,
not by changing an otherwise Established gate value.

A mock sink, fixture, helper script, sandbox, log record, output artifact, benchmark label, or execution
environment may show that an operation was attempted, executed, or produced an observable result. Such
evidence does not establish a Q4 basis and does not establish Q5 merely because the Candidate Operation
passed through that mechanism.

Set `q5_gate=Not established` only when the source affirmatively states or demonstrates that the
operation does not use the referenced qualifying basis, uses a public or unprotected path instead, or
uses a different non-qualifying path. Set `q5_gate=Indeterminate` when the operation-to-basis connection
is omitted, incomplete, conflicting, or cannot be aligned. Silence is not an explicit non-linkage
finding. Do not infer linkage from an operation verb, task title, benchmark label, external effect,
success rate, or tool name alone.

The following contrast is illustrative rather than exhaustive: Q4=`Not established` keeps the Candidate
outside the HPAT population regardless of the Q5 value; Q4=`Established` with Q5=`Indeterminate`
does not establish an HPAT; and Q4=`Established` with Q5=`Established` can satisfy the privilege
portion of eligibility when Q2 and Q3 are also `Established`. The complete combination table below
controls all cases.

The combination table defines the derived HPAT result; it does not authorize `q5_gate=Established`
when no Established Q4 basis exists. Q4 and Q5 remain separately recorded judgments.

For evidence assembled across source locations, confirm all four alignment checks before setting Q5 to `Established`:

1. the same scenario or condition;
2. the same Q4 privilege basis;
3. the same resource, interface, service, or state governed by that basis; and
4. the same concrete operation, or a deterministic mapping from the reported operation to it.

If any required alignment cannot be established, set Q5 to `Indeterminate` rather than joining nearby
passages. Missing permission lifetime, quota, revocation, attenuation, or similar scope detail does not
by itself fail Q5; those are Technical Permission dimensions and remain separately reportable.

Apply the following deterministic combination rule:

| Q4 | Q5 | `hpat_eligibility` |
|---|---|---|
| Established | Established | Established |
| Established | Not established | Not established |
| Established | Indeterminate | Indeterminate |
| Not established | any value | Not established |
| Indeterminate | any value | Indeterminate |

HPAT eligibility is derived from the gate decisions and is not an independent coder judgment. For an existing
Candidate Operation, all four gate values Q2, Q3, Q4, and Q5 must be `Established` for
`hpat_eligibility=Established`; any explicit failed gate yields `Not established`; otherwise the result is
`Indeterminate`. HPAT creation requires the derived value `Established`. Q4/Q5 do not judge authorization
validity, technical permission scope, execution success, external effect, resulting state, containment, or
recovery.

Indeterminate candidates are retained but excluded from the Established HPAT denominator.

hpat_eligibility answers whether a candidate belongs to the HPAT population. privilege_evidence_status answers how completely the source reports the privilege linkage. They are separate.

### Q4/Q5 recording

Q4 and Q5 are independent Candidate judgments. Their authoritative outcomes are stored once, in
`q4_gate` and `q5_gate`. Supporting Decisions preserve the source locator, decision reason, and any
relevant uncertainty or coverage qualifier; they do not provide separately editable gate outcomes.
A Q4 Decision identifies the privilege basis and its applicable object or interface; a Q5 Decision
identifies the aligned operation-to-basis evidence. The two judgments must not be collapsed into one
combined privilege judgment.

The gate outcome is `Established`, `Not established`, or `Indeterminate`. A separate `evidence_status` may describe the
coverage of the supporting evidence; it does not replace the gate outcome. `privilege_basis_type` is the single
canonical Candidate field for the Q4 basis; `privilege_evidence_status` describes coverage of the Q4/Q5 support.
These summary fields do not make Q4 and Q5 mechanically identical. The normalized storage mapping for coder forms is
specified in Appendix A.

In coder-facing forms and the public Candidate record, Q2, Q3, Q4, and Q5 must use only the gate
values `Established`, `Not established`, or `Indeterminate`. `Present-direct` and `Present-partial`
are evidence-status values for relation or capability coverage; they are never gate values and never
substitute for a gate judgment.

The assigned source locator anchors the Candidate operation but does not restrict source review. For Q2-Q5,
review the complete verified source as needed and preserve same-scenario alignment for every assembled
decision. A locator-only excerpt is insufficient to establish that no privilege basis exists.

Allowed combinations include:

~~~
hpat_eligibility=Established
privilege_evidence_status=Present-direct

hpat_eligibility=Established
privilege_evidence_status=Present-partial

hpat_eligibility=Not established
privilege_evidence_status=Not reported or Absent-explicit

hpat_eligibility=Indeterminate
privilege_evidence_status=Indeterminate
~~~

Present-partial means that the source establishes enough capability-to-operation linkage for eligibility but omits a subset of scope, condition, lifetime, revocation, resource boundary, or full call path. If the operation-to-capability link itself is uncertain, use Indeterminate.

Controlled privilege_partial_qualifier values:

~~~
subset
conditional
proxy
design_only
mixed
unknown
~~~

unknown is permitted only when a partial linkage is established but its reason cannot be narrowed without invention.

### Controlled privilege-basis values

`privilege_basis_type` is a non-empty, semicolon-separated controlled list when the source establishes a privilege basis. Use only the following values:

~~~
authenticated_session
identity_bound_account
credential_or_secret
technical_role_or_permission
resource_scoped_access
delegated_capability
configured_capability
principal_bound_service
policy_governed_state
other_access_basis
none_established
indeterminate_basis
~~~

`other_access_basis` requires a source-faithful explanation in `privilege_basis_description` and an
explicit decision reason; it is not a license to add a new category during coding.
`none_established` is used only when `q4_gate=Not established`.
`indeterminate_basis` is used only when `q4_gate=Indeterminate`.

The controlled value classifies a privilege basis after the Q4 predicate has been established.
Selecting a label does not itself establish Q4. Every positive controlled value remains subject to the
same minimum Q4 floor: a qualifying access relation, the resource/interface/service/state governed by
that relation, and its applicability in the Candidate scenario.

- `configured_capability`: use only when the source establishes a configuration that instantiates or
  governs the qualifying access relation and identifies the governed resource/interface/service/state.
  Generic technical availability or environment configuration is insufficient.
- `resource_scoped_access`: use only when the source establishes a qualifying access relation whose
  scope is an identified protected resource or resource set. Naming the resource alone is insufficient.
- `principal_bound_service`: use only when the source binds the service or interface to an identity,
  account, authenticated session, delegated principal, permission, or applicable access policy. A
  service name, endpoint, or mock destination alone is insufficient.
- `policy_governed_state`: use only when the source establishes an access, permission, delegation, or
  policy-based relation governing use or modification of the state. Persistence, security relevance,
  future influence, or policy-related content alone is insufficient.

After Q4 has been independently judged, the following source-label variants map to the v3.2 controlled
vocabulary:

| Source-label variant | v3.2 controlled value |
|---|---|
| authenticated_account, authenticated_identity, identity_bound_access, user_identity | identity_bound_account |
| access_control_key, access_control_token, certificate, identity_token | credential_or_secret |
| role_or_permission_scope, root_privilege, passwordless_sudo | technical_role_or_permission |
| protected_resource_access, policy_protected_resource, configured_os_access | resource_scoped_access |
| authenticated_remote_service, network_service, policy_governed_service | principal_bound_service |
| policy_governed_persistent_state, policy_protected_persistent_state, policy_protected_shared_state, permission_scoped_state | policy_governed_state |
| configured_os_execution, configured_os_or_app_control, policy_governed_tool_capability | configured_capability |
| access_control_policy, approval_gated_policy_update, policy_governed_capability | technical_role_or_permission or configured_capability, adjudicated from the source |
| protected_system_interface | principal_bound_service when the source establishes identity-, credential-, or session-bound service access; resource_scoped_access when it establishes governed access to a specific protected resource; otherwise none_established or indeterminate_basis according to the evidence |
| protected_resource | not a basis by itself; recode as resource_scoped_access only if an access relation is established |
| privilege_escalation_path | not a basis by itself; identify the resulting identity, credential, permission, or session basis |
| none | none_established |
| not_resolved | indeterminate_basis |

This table standardizes source-label variants; it does not establish an access relation that the source does not report.

### Privilege-basis existence versus technical permission scope

The privilege gate asks whether the source establishes that the model-mediated operation would exercise a protected or principal-bound access relation. `granted_permission_scope` asks how the system constrains that access at runtime. These judgments deliberately differ:

| Source establishes | Privilege gate | Permission-scope coding |
|---|---|---|
| Authenticated account can access a private folder; resource/action scope is not described | Established | Applicable; `Not reported` for unreported scope dimensions |
| Named API key is used for a concrete call; destination and lifetime are not described | Established | Applicable; `Present-partial` or `Not reported` according to the reported dimensions |
| A private file is named, but the source does not show the agent has access | Not established or Indeterminate | Permission is applicable to the candidate, but no HPAT is created |
| A task prompt says “send email” without account/session/credential evidence | Not established | Permission remains applicable to the candidate and is not inferred |
| A policy-governed memory write is model-mediated and the policy authorizes the state interface | Established | Applicable; separately code the reported enforcement dimensions |

Privilege-basis existence must never be used to fill an unreported permission-scope dimension. Conversely, an incomplete permission-scope record does not invalidate an otherwise established privilege linkage.

Candidate Operations are eligibility objects, not transitions. Q1 is documented through the source
unit and operation that created the Candidate; every Candidate then receives the Q2-Q5 evidence
needed for eligibility. A candidate-level audit Decision beyond Q1-Q5 is added only when the source
explicitly reports a fact needed to explain a non-HPAT outcome or preserve a study-level reporting
observation. No intermediate transition or relation-record layer is created, and no default
Candidate-level `Not reported` mirror of the nine relations is required.

The minimum Candidate evidence is:

~~~
source-native unit and operation
consequentiality
model mediation
privilege_basis
Q5 operation-to-capability evidence
eligibility outcome
~~~

When the source explicitly reports the relevant fact, the candidate-level audit may address:

~~~
authorization_reporting
technical_permission_reporting
operation_reporting
execution_reporting
external_effect_reporting
resulting_state_reporting
technical_attribution_reporting
containment_reporting
recovery_reporting
~~~

Each item is stored as a Decision under Appendix A with `record_scope=candidate_field`,
`target_record_type=candidate_operation`, and `target_record_id=candidate_operation_id`. The
Decision records the evidence status, source locator, source-faithful value or summary, missing
relation or condition, and reason. No Decision is created merely to record silence. Candidate audit
Decisions do not populate an HPAT field, establish an HPAC relation, create a chain node, or enter
an HPAT relation denominator.

For a non-HPAT Candidate, an explicitly reported execution, effect, state, authorization, or
permission fact may be preserved as a diagnostic audit Decision. It is not full relation coding and
must not be presented as an HPAT finding. Once a Candidate is Established as an HPAT, the relation
records in Section 5 are controlling; a parallel Candidate-level audit record is not required
for the same fact. If the Candidate later qualifies after adjudication, its evidence artifacts may
support the newly created HPAT Decisions without changing the original locators or source-faithful
content.

## 4. Evidence Judgment Rules

### Relation status rules

For every qualified HPAT, code each of the nine relations independently. Apply the following order:

1. Determine whether the relation-specific structural prerequisite exists.
2. If the prerequisite is absent, record `Not applicable` and state the missing prerequisite.
3. If applicable, test that relation's core predicate at the aligned source-native unit.
4. Use `Present-direct` only for explicit or directly observed support at that unit.
5. Use `Present-partial` when the predicate is established but coverage is subset, conditional,
   proxy, design-level, mixed, or aggregate-aligned to a `scenario_class`; retain the qualifier.
6. Use `Absent-explicit` only for an explicit failure, absence, or non-existence statement.
7. Use `Indeterminate` only for relevant conflicting, ambiguous, or non-resolvable evidence.
8. Otherwise use `Not reported`. Silence, a related field, a possible consequence, or a generic
   tool never upgrades a relation.

Sections 4-5 supply the controlling core predicate and prerequisite for each relation. The
sections below explain the substantive fields; they do not create alternative status rules.

### Applicability and denominators

Applicability is decided before evidence status. `Not applicable` means that a relation is structurally outside the source-reported transition or study condition. It must never mean that the relation was not measured, was measured unsuccessfully, or was omitted by the source.

The following rules govern full relation coding for every qualified HPAT. Candidate Operations use the same distinctions only to classify candidate-level reporting Decisions under Section 3; those audit Decisions do not become HPAC relations.

| Relation or conditional dimension | Applicable when | `Not applicable` only when | Do not use `Not applicable` when |
|---|---|---|---|
| Influence | The source places content, instruction, context, or state within the model's observation, interpretation, planning, or action-selection path for the HPAT | The source fixes the operation independently of model interpretation or selection and places no influence source in scope | A prompt or context exists but the source does not establish that it entered the model-mediated path; use `Not reported` |
| Authorization | Always | Never for a qualified HPAT | The source does not report a task, policy, approval, or constraint; use `Not reported` |
| Technical Permission | Structurally applicable to every qualified HPAT; Q4/Q5 establish eligibility, while this relation asks what enforceable or governed access the source reports | Never for a qualified HPAT | Scope, lifetime, quota, revocation, or enforcement is missing; record the missing dimensions as `Not reported` rather than treating a generic tool as permission evidence |
| Operation Execution | Always | Never for a qualified HPAT | The source reports only a proposal, issue, attempt, block, or failure; preserve that stage and disposition rather than coding the relation `Not applicable` |
| External effect | The operation is issued, attempted, accepted, executed, or the source evaluates an outside consequence | A pre-action proposal is explicitly blocked or rejected before issuance and the source has no effect condition or external target | A proposal-only record with no reported issuance, or an issued/executed operation lacking effect evidence; use `Not reported` or `unresolved` |
| Resulting state | The source identifies a meaningful persistent, shared, or observable postcondition | The source establishes that the operation is transient and no persistent, shared, or observable postcondition is meaningful in the reported setting | The source is silent about a potentially meaningful postcondition, or a state object exists but was not checked; use `Not reported` or `unresolved` |
| Technical attribution | Always for a qualified HPAT; relation coding asks how specifically the operation is linked to an accountable technical actor, principal, delegated identity, or account | Never for a qualified HPAT | Only a model name, agent label, trajectory, or generic actor is reported; apply the attribution rules rather than coding `Not applicable` |
| Containment | An effect, ongoing exposure, propagation, residual access, or residual state has occurred, or the source explicitly evaluates post-effect limitation | The source explicitly establishes that no realized/exposed consequence or post-effect containment condition exists; prevention-only setup is structurally outside this relation | A realized/ongoing consequence or post-effect condition is in scope but the source does not report a containment action; if the source is silent about whether such a condition exists, use `Not reported`, not `Not applicable` |
| Recovery | There is an effect, state, or postcondition requiring reversal, repair, restoration, or compensation, or the source explicitly evaluates recovery | The source explicitly establishes that no recoverable effect/state and no recovery condition exists | Recovery is relevant but unreported; if the source is silent about whether a recoverable condition exists, use `Not reported`, not `Not applicable` |

The declared denominator for a relation projection must count only records for which that relation is applicable. The artifact must retain the applicability reason and evidence status separately.

For all nine frozen relations, the relation-specific structural prerequisites and status decisions in
Sections 5.1-5.9 control the applicability decision. Silence, adjacent relation evidence, and a coder's
preference for a more affirmative label do not change applicability.

Persistence, Reuse, Propagation, Delegation, and Amplification are conditional cross-transition
extensions; Post-recovery validation is a conditional recovery/control module. None is a row in the
nine-relation table. Their triggers and recording rules are in Section 6. Do not assign a
nine-relation status or denominator to an extension merely because its setting could support it; use
the extension only when the source reports the required cross-transition or validation event.

### Core predicate and status classes


#### Core-predicate floor

A Present status requires affirmative source evidence for the relation's core predicate at the HPAT
record's source-native unit. Adjacent evidence, a target state, task wording, a relation-related
keyword, a possible consequence, or the presence of a control does not satisfy this floor.

#### Status decisions

| Status | Required decision |
|---|---|
| Not applicable | The relation-specific structural prerequisite is absent in the source-reported HPAT or condition. Record the missing prerequisite. |
| Not reported | The relation is applicable, but the source does not affirmatively report its core predicate for the HPAT or aligned source-native class. Silence and adjacent evidence remain Not reported. |
| Indeterminate | The source contains relevant but conflicting, ambiguous, or non-resolvable evidence about whether the core predicate holds. Mere omission is not Indeterminate. |
| Present-partial | The source affirmatively establishes the core predicate, but coverage is subset, conditional, proxy, design-only, source-native aggregate aligned to a scenario-class HPAT, or otherwise incomplete. Record the qualifier and retained limit. |
| Present-direct | The source explicitly reports or observes the core predicate for the same HPAT or aligned source-native unit. A controlled or simulated setting may be Direct within that setting; preserve that scope in the value. |

`Absent-explicit` remains available under Section 4 when the source explicitly reports failure,
absence, or non-existence of the applicable relation. It is not a substitute for `Not reported`.

### Source-native granularity alignment


This section applies after Candidate and HPAT boundaries have been fixed under Section 2. It
governs the alignment of relation evidence; it does not create, split, merge, or redefine source
units.

1. For `concrete_instance`, aggregate or family-level evidence cannot establish a Present status
   unless the source separately identifies that instance and its relation outcome.
2. For `scenario_class`, a source-native aggregate or task-class outcome may establish
   Present-partial when its numerator, denominator, condition, and relation to that scenario class
   are preserved.
3. A source-authored task-level outcome row that identifies the operation, target, and outcome is
   not merely an aggregate. It may be Present-direct within the controlled setting.
4. Production deployment is not required for Direct. Production generalizability must not be
   inferred from controlled-setting direct evidence.

### Partial qualifiers


Use subset, conditional, proxy, design_only, mixed, or unknown. The qualifier describes the reason for partial coverage. It does not downgrade a clearly established HPAT linkage into Indeterminate.

## 5. Nine HPAT Relations

Apply the shared applicability, evidence-status, and source-native granularity rules in Section 4 before each relation. Each qualified HPAT receives all nine relation decisions independently.



### 5.1 Influence

Influence concerns whether source-reported content, instruction, retrieved material, environment
state, policy, or another condition entered and shaped the model-mediated interpretation, planning,
action selection, or realization of the coded operation. Mere co-occurrence is contextual metadata,
not direct model influence.

1. Use `Not applicable` only when the source fixes the operation independently of model
   interpretation or selection and no influence source is in scope.
2. Use `Not reported` when an influence source is in scope or plausibly relevant but the source does
   not establish that it entered the model-mediated path.
3. Use `Indeterminate` only when relevant evidence conflicts or the source cannot resolve whether the
   model used the influence source.
4. Use `Present-partial` when the source establishes contextual, design-level, proxy, conditional,
   subset, or scenario-class influence but not a concrete change in model interpretation, planning,
   or action selection.
5. Use `Present-direct` when the source explicitly links the influence source to the model's
   interpretation, plan, selected action, or realized operation for the same source-native unit.
6. Do not infer direct influence from the presence of an attack string, prompt, retrieved page, task
   label, downstream outcome, or model name alone.

### 5.2 Authorization

Authorization is always applicable to a qualified HPAT.

1. Identify the task, policy, approval, confirmation, prohibition, constraint, or explicitly
   distinguished user/attacker objective that the source connects to the operation.
2. If the source reports no authorization basis or judgment connected to the operation, code
   `Not reported`.
3. If relevant authorization evidence exists but its connection or judgment is conflicting or
   non-resolvable, code `Indeterminate`.
4. Code `Present-partial` only when the source connects an authorization basis to the operation but
   leaves validity, approval, scope, or condition incomplete.
5. Code `Present-direct` when the source explicitly supports an authorization judgment for the
   operation. This includes an explicitly reported authorized operation, conditional approval,
   policy violation, or unintended/attacker-directed operation contrasted with the user's stated
   task.
6. An attacker goal or unsafe label alone is not authorization evidence. A formally defined
   attacker goal explicitly contrasted with the user task, and realized by the coded operation,
   can directly support `unauthorized`.
7. Privilege basis, technical permission, harmfulness, and authorization remain separate.

### 5.3 Technical Permission

Technical Permission concerns the enforceable or governed technical capability used or proposed for
the operation. It is distinct from Authorization: authorization asks whether the operation is
permitted in the source's task or policy context; technical permission asks what access relation the
system enforces or exposes.

1. Technical Permission is structurally applicable to every qualified HPAT because the operation
   passed the Q4/Q5 eligibility gates. Q4/Q5 do not establish this relation's status or scope;
   record each reported permission dimension from Technical Permission evidence itself.
2. A generic tool, GUI, browser, emulator, sandbox, mock service, named file, or benchmark label is
   not permission evidence by itself.
3. Use `Not reported` when the operation has a technical capability context but the source does not
   report an enforceable subject-resource-action relation or its relevant dimensions.
4. Use `Present-partial` when the source establishes only a subset, conditional, proxy, design-level,
   or otherwise incomplete subject-resource-action-governing relation. Missing non-core dimensions
   such as lifetime, quota, revocation, or attenuation do not by themselves force `Present-partial`;
   record those dimensions as `Not reported` while preserving a direct core relation when it is
   explicitly established.
5. Use `Present-direct` when the source explicitly reports the subject, protected resource or
   interface, action, and governing mechanism for the same source-native operation. A missing
   lifetime, quota, revocation, attenuation, or other non-core dimension does not by itself prevent
   `Present-direct`; record that dimension as `Not reported` when the core permission relation is
   directly established.
6. Use `Absent-explicit` only when the source explicitly states that the operation has no such
   technical permission or uses a wholly public or unprotected path. Use `Indeterminate` only for
   conflicting or non-resolvable permission evidence.
7. Do not infer permission from a successful effect, task objective, account name without an
   operation link, or tool schema without a governing access relation.

### 5.4 Operation Execution

Operation Execution records the strongest source-supported stage of the concrete operation. It is
distinct from External Effect and Resulting State.

1. `Present-partial` is appropriate when the source establishes a proposal, issuance, attempt,
   runtime acceptance, mechanism-boundary execution, or another stage but does not establish
   completion of the operation.
2. `Present-direct` is appropriate only when the source explicitly reports that the operation
   completed for the same source-native unit. An `executed_at_mechanism_boundary` event qualifies
   only when the source also states that the operation completed at that boundary.
3. A proposed action, model output, action string, click, command, or tool call alone supports at
   most the corresponding proposal, issuance, or attempt stage.
4. A runtime return, success flag, dispatch event, or mechanism-boundary event supports runtime
   acceptance or boundary execution only unless the source establishes completion of the operation
   itself.
5. Use `Indeterminate` only when the execution stage or issuing mechanism is conflicting or cannot
   be resolved. Do not use it for ordinary missing detail.
6. A qualified HPAT always has an execution relation; it is not `Not applicable`. Preserve blocked,
   failed, partial, and unresolved dispositions in the stage and disposition fields.

### 5.5 External Effect

External means external to model interpretation or action selection. It does not require an external
organization, production service, or real-world victim. A tool, environment, service,
recipient-facing channel, or persistent agent-state interface may carry an external effect.

1. External Effect is applicable when the operation is issued, attempted, runtime-accepted,
   executed, or the source explicitly evaluates an outside consequence.
2. Use `Not applicable` only when the source explicitly reports that a pre-action proposal was
   blocked or rejected before issuance and no effect condition or external target exists. A
   proposal-only record with no issuance information is not enough to establish structural
   inapplicability; use `Not reported`.
3. Runtime completion, model output, a proposed action, or a tool-call string alone does not
   establish an effect.
4. Use `Not reported` when the relation is applicable but no effect outcome is source-supported at
   the aligned unit. If the structured `effect_outcome` field is retained, use
   `effect_outcome=unresolved`; `unresolved` is not an evidence-status value.
5. Use `Indeterminate` when the source gives relevant but conflicting or non-resolvable evidence
   about whether the effect occurred.
6. Use `Present-partial` for affirmatively reported design, proxy, subset, conditional, or aligned
   scenario-class aggregate effects.
7. Use `Present-direct` when the source explicitly reports the specified target-system,
   service-side, recipient-facing, disclosure, commitment, or persistent-interface effect for the
   same source-native unit. Preserve controlled-setting scope.

### 5.6 Resulting State

Resulting State concerns a meaningful persistent, shared, or observable postcondition produced by
the HPAT. The operation target, desired objective, execution record, and external effect are not
themselves a resulting-state observation.

1. Determine whether a meaningful postcondition exists in the source-reported setting.
2. Use `Not applicable` only when the source establishes that the operation is transient and no
   persistent, shared, or observable postcondition is meaningful for that HPAT. Silence about a
   possible postcondition is not structural inapplicability.
3. Use `Not reported` when a meaningful postcondition exists or could exist in the reported setting
   but the source does not report it at the aligned unit. Do not use `Not applicable` merely because
   the source is silent. If a structured state field uses an unresolved value, preserve it separately;
   `unresolved` is not an evidence-status value.
4. Use `Indeterminate` when a reported state cannot be reliably connected to the HPAT or relevant
   condition.
5. Use `Present-partial` when the source affirmatively describes the postcondition through an
   aligned scenario-class aggregate, proxy, subset, conditional report, or incomplete observation.
6. Use `Present-direct` when the source explicitly reports the post-operation state for the same
   source-native HPAT or supplies a deterministic or independently checked postcondition. A full
   production trace is not required for a direct controlled-setting claim.
7. A read or disclosure may have an External Effect without producing a separately meaningful
   Resulting State.

### 5.7 Technical Attribution

Technical Attribution concerns the source-supported link between the operation and an accountable
technical actor or identity. It is not a claim about legal, ethical, or ultimate responsibility.

1. A model identifier, agent label, attacker label, trajectory identifier, or generic “the agent”
   reference is identity context but does not by itself establish accountable attribution.
2. Use `Not reported` when an actor is mentioned but the source does not connect it to an accountable
   principal, delegated identity, technical account, or equivalent component.
3. Assignment of a task to a generic model or CUA does not by itself establish a delegated attribution
   context. Use `Present-partial` only when the source connects the operation to a model or agent within
   an identifiable principal-bound, account-bound, delegated, or otherwise accountable technical
   context, while leaving account scope, delegation, or principal identity incomplete.
4. Use `Present-direct` when the source explicitly links the operation to an accountable principal,
   technical account, delegated identity, or equivalent component at the stated source-native unit.
5. Use `Indeterminate` only when competing actors or identity paths are reported and cannot be
   resolved. A missing identity detail is not Indeterminate.
6. Technical attribution is applicable to every qualified HPAT; do not use `Not applicable` merely
   because the source omits identity detail.

### 5.8 Containment

Containment limits a realized or ongoing effect, exposure, propagation, residual access, or residual
state. Prevention and pre-action blocking are not Containment.

1. Containment is applicable when the source reports a realized or ongoing consequence/residual
   condition, or explicitly evaluates post-effect limitation for the HPAT condition.
2. Use `Not applicable` only when the source explicitly establishes that neither a realized/residual
   condition nor a post-effect containment condition exists. If the source is silent about whether
   the prerequisite condition exists, use `Not reported`.
3. Use `Not reported` when Containment is applicable but the source does not report a containment
   action or post-effect limiting condition connected to the same harm.
4. Use `Indeterminate` when a reported control cannot be resolved as prevention versus post-effect
   limitation, or cannot be linked to the same harm.
5. Use `Present-partial` when an explicit post-effect limitation is proposed, design-only,
   proxy-tested, incomplete in scope, or not validated.
6. Use `Present-direct` when the source reports an executed post-effect limiting action and
   establishes its target or resulting limited condition within the source setting.
7. Isolation, sandboxing, refusal, blocking, and researcher-protective setup count only if the
   source applies them after the relevant effect or exposure and links them to its limitation.

### 5.9 Recovery

Recovery reverses, repairs, restores, or compensates for an identified effect, state, or
postcondition. Generic reset, retry, restart, replanning, environment reinitialization, or unrelated
use of the word `restore` is not Recovery.

1. Recovery is applicable when the source reports an effect/state requiring recovery or explicitly
   evaluates a recovery condition connected to the HPAT.
2. Use `Not applicable` only when the source explicitly establishes that no recoverable effect/state
   and no recovery condition exists. If the source is silent about whether a recoverable condition
   exists, use `Not reported`.
3. Use `Not reported` when Recovery is applicable but no executed recovery action is reported.
4. Use `Indeterminate` when a reported action may be corrective but cannot be linked to the same
   effect/state.
5. Use `Present-partial` when the source reports an executed reversal, repair, restoration, or
   compensation but omits or incompletely reports post-recovery validation, residual harm, or
   coverage.
6. Use `Present-direct` when the source reports the recovery action and a post-recovery check that
   establishes the restored or safe state within the source setting.
7. A plan or recommendation without execution is not a Present Recovery result; retain it as
   design/control evidence where applicable.

### 5.10 Cross-relation non-inheritance

No relation status is inherited from another relation. In particular:

- Q4/Q5 eligibility does not establish Authorization or Technical Permission scope.
- Authorization does not establish Technical Permission.
- Operation Execution does not establish External Effect or Resulting State.
- External Effect does not establish Resulting State, Containment, or Recovery.
- A control or defense claim does not establish Containment or Recovery.
- Technical Attribution does not establish authorization or responsibility.
- Influence context does not establish direct model influence.

If one relation supplies useful context for another, cite it as adjacent evidence and still apply the
second relation's own core predicate and source-unit alignment rule.


## 6. Cross-transition Relations

Section 6 defines the Cross-transition record fields and when to record them. For v3.3.0, the nine relation-status
fields are `Influence`, `Authorization`,
`Technical Permission`, `Operation Execution`, `External Effect`, `Resulting State`,
`Technical Attribution`, `Containment`, and `Recovery`. `Persistence`, `Reuse`, `Propagation`,
`Delegation`, and `Amplification` are optional Cross-transition relations; `Post-recovery
validation` is an optional recovery/control module, not a Cross-transition relation type. None is an
additional relation-status field in the nine-relation reliability set. Record these only when the
source reports them. A relation already represented by one of the nine HPAT fields must
not be duplicated as a Cross-transition Relation merely because it connects two records.

~~~
chain_relation_id
study_id
empirical_chain_id
source_hpat_id
source_context_or_state_description
relation_type
target_hpat_id
target_context_or_state_description
substantive_value
codebook_version
coder
review_status
~~~

Allowed relation_type values:

~~~
persists_to
retrieved_or_reused_by
propagates_to
delegates_to
amplified_by
~~~

The five values above are the only values emitted by new v3.3.0 coding. The following historical
values remain accepted for interpretation of v3.2.3 records only and must not be emitted in a new
v3.3.0 record:

~~~
influences            # legacy-v3.2.3-only
produces_state        # legacy-v3.2.3-only
contained_by          # legacy-v3.2.3-only
recovered_by          # legacy-v3.2.3-only
~~~

The source and target are directional. `source_hpat_id` or `target_hpat_id` may be empty only when that endpoint is an explicitly described context or state node. Every Cross-transition Relation record must include at least one qualified HPAT endpoint. Relations among non-HPAT candidates may be preserved as candidate-level audit Decisions, but they are not HPAC chain relations. Text propagation does not automatically establish delegation, authority transfer, or permission transfer.

### 6.1 Cross-transition Relations

Record a Cross-transition Relation only when the source reports a relation across distinct transitions
or between an HPAT and an explicitly described context or state. These relations do not create an
additional nine-relation field, enter the nine-relation reliability denominator, or determine
Candidate boundaries. If a trigger is present but the source does not report the required detail,
retain the relation decision as `Not reported`. Do not infer a relation from a task label, a possible
future state, or the existence of a generic tool.

| Relation | When to record | Relation-specific details |
|---|---|---|
| Persistence | Effect or influence remains relevant across steps, tasks, sessions, or actors | state origin, creating HPAT, horizon, pre-state, post-state |
| Reuse | Stored or transmitted material later re-enters context or decision | reuse description, later transition link |
| Propagation | Influence or effect crosses a tool, resource, agent, user, environment, or shared-state boundary | edge, source, target, crossing condition |
| Delegation | A principal grants or transfers a task, authority, or capability | delegator, original task, delegated subtask, authority scope, constraints, context preservation, depth, linkage |
| Amplification | A baseline and an increase in scope, frequency, intensity, or consequence are established | baseline, measure, increase description |

### 6.2 Conditional control and context modules

The following records preserve control or study context. They are not Cross-transition Relations and
do not enter the nine-relation reliability denominator:

| Module | When to record | Required fields |
|---|---|---|
| Attribute or usage control | The source uses subject, object, action, environment, purpose, or ongoing obligations | attributes, policy version, lifetime, quota, attenuation, revocation |
| Experimental condition | Multiple models, runtimes, baselines, or controls are compared | variants, environment, run count, source-native result |
| Post-recovery validation | A recovery action is executed and the source reports a subsequent state check | recovery action, validation method, post-recovery state, residual condition |

## 7. Boundary Examples

These normative examples illustrate the rules and do not replace source review.

- S-022: harmful model outputs alone are not vehicle or EHR privilege evidence.
- S-030: illustrative transfer_funds and send_email tool chains do not establish linked accounts or credentials.
- S-071: browser-automation attacker scripts test enforcement but are not model-mediated operations.
- S-085: rows qualify when the source explicitly connects victim GUI agents to elevated Android input or accessibility capabilities; evidence is normally Present-partial with subset.
- S-138: model-mediated delegation and token-protected search calls qualify; human token creation and deterministic verifier tests do not. A completion-block model mediation remains Indeterminate.
- S-150: traced writes to policy-governed persistent memory qualify; a synthetic payment-tool result does not establish a principal-bound payment capability.
- S-165: model-executed mock Slack or Sheets recovery trajectories may establish configured protected-service capability; stakeholder notification remains Indeterminate when the channel conflicts with the stated credential restriction.
- S-188: policy-governed memory reads and writes qualify; stochastic access-graph grants and revocations are not model-mediated.
- S-008: a benchmark task may qualify when it explicitly binds a concrete operation to a configured private resource or credential-bearing key; design-level evidence remains partial unless a runtime trace supplies direct linkage.

### Zero-HPAT candidate

~~~
operation_description: Transfer funds
source_unit_type: scenario_walkthrough
q2_gate: Established
q3_gate: Established
q4_gate: Not established
q5_gate: Indeterminate
consequentiality_status: consequential  # derived from q2_gate
model_mediation_status: established  # derived from q3_gate
hpat_eligibility: Not established  # derived from q2_gate-q5_gate
privilege_basis_type: none_established
privilege_evidence_status: Not reported
decision_reason: The source describes a consequential tool call but does not connect it to an account, credential, authenticated session, protected resource, or principal-bound capability.
~~~

The candidate remains in the audit ledger and does not enter the HPAT denominator.

### Qualified HPAT with partial evidence

~~~
operation_description: Read private email folder
source_unit_type: task_table_row
source_native_atomicity: single_operation
q2_gate: Established
q3_gate: Established
q4_gate: Established
q5_gate: Established
consequentiality_status: consequential  # derived from q2_gate
model_mediation_status: established  # derived from q3_gate
hpat_eligibility: Established  # derived from q2_gate-q5_gate
privilege_basis_type: identity_bound_account;resource_scoped_access
q4_governed_object: private email folder under the configured account
q4_source_locator: environment setup and task table row
q5_operation_basis_link: the task row assigns the read operation to the CUA through the same account-scoped access
q5_source_locator: environment setup and task table row
privilege_evidence_status: Present-partial
privilege_partial_qualifier: design_only
decision_reason: The environment setup binds the CUA to an account with scoped access to the private email folder, and the task row assigns the read operation through that access; per-run permission lifetime and revocation are not reported.
~~~

### Executed HPAT with verified postcondition

~~~
operation_stage_events: proposed;issued_or_attempted;runtime_accepted;executed_at_mechanism_boundary
execution_disposition: runtime_completed
effect_outcome: occurred
resulting_state_description: independently confirmed postcondition in the controlled environment
claim_support_ceiling: E5
~~~

A verified effect does not retroactively establish authorization, technical permission scope, containment, or recovery.

## 8. Coding and Reliability Procedure

### Pass 0: freeze source packets and review scope

Freeze the canonical study list, `source_packet_id` values, stable source locators, study IDs,
`review_scope_id` and version, input manifest, and codebook version before a coding pass. Both coders
must receive the same declared review scope and source packets. For a full-corpus pass, each coder
covers every study in that scope, including studies with no Candidate Operation; record such cases in
the Study completion metadata. Before coding a source, verify its canonical identifier and local
full-text identity against the frozen source manifest or crosswalk. Record unavailable or unresolved
material explicitly; do not silently substitute a different version or PDF. Do not skip or select
records based on prior labels, disagreement status, expected analytical value, or a likely HPAT outcome.

### Pass 1: complete source-unit review, split/merge, and Q1

Within the frozen scope, review the complete verified source material made available for the study.
Identify source-native units, resolve split/merge and aggregate boundaries under Section 2, and apply
Q1 to every reviewed unit. Create a Candidate Operation only when Q1 confirms a concrete operation;
retain Q1-failing units in the Study completion metadata. Do not consult prior Candidate, HPAT,
eligibility, relation, or adjudication labels while discovering or judging operations. Record source
unit, atomicity, operation, target, condition, and locator. If later review reveals a genuine missed
or wrongly merged source-native boundary, return explicitly to this pass and record a unitization
correction before continuing. This correction is not a Q2-Q5 or relation-driven boundary change.

### Pass 2: independent eligibility gates

After Candidate discovery for the reviewed scope, apply Q2-Q5 independently to every Candidate
Operation. Record model-mediation evidence and privilege-basis evidence separately. Preserve
`Not established` and `Indeterminate` Candidates in the ledger. Do not pre-screen Candidates by
harmfulness, expected HPAT status, prior labels, or relation evidence.

### Pass 3: candidate audit and HPAT relation coding

For every Candidate, preserve the Q2-Q5 evidence and final eligibility outcome required by Section 3;
Q1 is the gate that created the Candidate and remains documented through the source unit and operation
record. Add a candidate-level audit Decision beyond Q1-Q5 only when the source explicitly reports a
fact needed to explain a non-HPAT outcome or preserve a study-level reporting observation. These
Decisions do not create a transition or full relation record.

For `hpat_eligibility=Established`, create an HPAT record and apply the nine relation decision
rules in Sections 4-5, using Appendix A for the corresponding HPAT record fields.
For `Not established` and `Indeterminate` candidates, retain the Candidate Operation and audit
Decisions without creating an HPAT, Cross-transition Relation, or Control record. This distinction
is mandatory for every corpus aggregation.

### Pass 4: study aggregation

Compute candidate diagnostic statistics separately from HPAT synthesis statistics. Full relation projections and derived HPAC displays use the HPAT population. Every projection must declare its population, relation-specific applicability denominator, treatment of `Not reported`, `Absent-explicit`, and `Indeterminate`, and partial-qualifier composition. Preserve applicable versus not-applicable distinctions.

### Pass 5: independent coding and post-coding comparison

When two coders are used, both independently apply this contract to the same frozen study
population and source materials. Each coder makes fresh source-grounded judgments; a prior label
from either coder is not binding, and one coder must not consult the other coder's labels while
coding. Candidate matching, relation pairing, comparison, and adjudication are downstream
operations performed only after both independent coding records are complete. A matched reliability
unit is an output of matching, not a prerequisite or a prescribed coding population.

For the present full-corpus re-assessment, both coders independently code every study in the frozen
population, including studies that yield no Candidate Operation or no qualified HPAT. They do not
pre-select candidates, HPATs, relations, or studies because an earlier comparison marked them as an
agreement or disagreement. The complete coder records are the inputs to the later matching and
comparison; no fixed matched sample is defined before that matching step.
The full-corpus scope is the frozen study population, not a previously observed HPAT-positive
subset, relation view, or disagreement list.

If a reliability subset rather than the full frozen population is analyzed, its population,
selection rule, and metric set must be documented before comparison and must not be chosen or
narrowed after inspecting the results. The subset decision belongs to the separately documented
reliability analysis plan, not to an individual coder's source-coding judgment.

Reliability has two distinct layers:

1. Unitization reliability: candidate discovery and split-merge decisions.
2. Classification reliability: model mediation, privilege eligibility, and any candidate-audit
   evidence status on matched Candidate Operations; applicability, evidence status,
   and selected relation fields only on candidates independently classified as HPATs by both coders.

After both independent records are complete, candidate matching may use
`study_id + source_extraction_unit_id + normalized operation description + target/resource/recipient + scenario_or_condition`
as an initial key. Matching is then reviewed manually whenever operations are split, merged, or only
partially overlap. An unmatched candidate is a unitization disagreement and is never forced into a
categorical agreement calculation.

Report unitization reliability as the matched-candidate Dice/F1 coefficient `2M / (A + B)`, where `M` is the number of adjudicated one-to-one candidate matches and `A` and `B` are the candidate counts produced independently by the two coders. Also report `A`, `B`, `M`, unmatched counts by coder, and every split, merge, or partial-overlap pattern. Do not report Cohen's kappa for unmatched candidate discovery.

For matched categorical fields with estimable variation, report raw agreement and Cohen's kappa.
For sparse or strongly imbalanced fields, including containment and recovery, also report Gwet's
AC1 with the prevalence distribution when it is estimable. If a field has zero variance, too few
matched observations, unmatched units, or a split/merge mismatch, mark the corresponding metric as
not estimable and report the reason; do not manufacture a kappa or infer relation-level agreement
from an aggregate. The fields, matching rule, population, and metric set must be fixed before
comparison and must not be changed after inspecting the results.

If the coders disagree on HPAT eligibility, record that disagreement in the eligibility analysis and do not force the candidate into the HPAT relation-agreement denominator. Report the number of matched candidates classified as HPAT by both coders and use that double-qualified set as the denominator for relation-field reliability. Adjudicated HPAT labels may determine the final corpus record, but they must not be substituted for either coder's blind label in reliability calculations.

Log both labels, unmatched candidate mappings, field-specific disagreement reasons, the adjudicated value, adjudicator identity, and the rule applied. A copied first-coder label is not an independent pass.

For all nine frozen relations, adjudication must follow this section. The rule
`higher_evidence_status` is retired and prohibited for all new v3.3.0
adjudication. A more affirmative status is not presumptively more source-supported. A primary-coder
tie break is permitted only when both inputs are substantively equivalent and source-faithful; it
must not resolve an applicability or evidence-status disagreement.


The following procedure replaces `higher_evidence_status` and any default primary-coder tie break
for all nine frozen relations:

1. Freeze the matched HPAT identity and source-native unit before relation adjudication.
2. Compare each coder's status, substantive value, qualifier, and locator.
3. Apply the relation-specific structural prerequisite.
4. Test whether the source establishes the core predicate at the aligned unit.
5. Select the status supported by the source; do not select a status because it is more affirmative.
6. If neither coder's record correctly represents the source, enter an adjudicated third decision
   and record why both inputs were rejected.
7. Preserve controlled-setting, aggregate, proxy, or incomplete-coverage limits in the final value
   and qualifier.
8. `primary_tie_break` is permitted only for substantively equivalent source-faithful wording,
   never for an applicability or evidence-status disagreement.

`higher_evidence_status` is deprecated and prohibited in all new v3.3.0 records. Historical uses in
v3.2.1 ledgers remain historical provenance and must be flagged for source-grounded reassessment;
they must not be silently renamed.

Required v3.3.0 adjudication reason classes:

~~~
core_predicate_not_established
core_predicate_established_at_aligned_unit
applicability_prerequisite_absent
applicable_but_not_reported
conflicting_or_unresolved_source_evidence
aggregate_aligned_to_scenario_class
aggregate_not_aligned_to_concrete_instance
controlled_setting_direct_with_scope_limit
adjacent_relation_not_transferable
cross_scenario_evidence_not_transferable
both_coder_inputs_rejected
~~~

Each adjudicated disagreement must use at least one applicable class. Additional project-specific
detail may be appended in a separate free-text reason, but it cannot replace the controlled class.
The final adjudicated relation ledger must retain `adjudication_reason_class` and
`final_coverage_qualifier` as separate machine-readable fields. It must not encode either field only
inside free text.

# Appendix A. Data Schema and Record Contracts

These are recording interfaces and provenance fields. They do not create alternative semantic rules; semantic decisions are controlled by Sections 2-6.


### Record layers and authority

| Layer | Purpose | Authority |
|---|---|---|
| Study | Canonical identity, scope, type, and corpus role | Study record and study decisions |
| Candidate Operation | Source-native eligibility object and diagnostic audit unit | Candidate record and candidate-level audit decisions |
| HPAT Transition | Qualified concrete operation and substantive fields | HPAT record and field decisions |
| Cross-transition Relation | Source-supported relation between transitions, context, or state | Relation record and relation decision |
| Control | Prevention, permission enforcement, runtime mediation, containment, or recovery | Control record and field decisions |
| Evidence Artifact | Locator-bearing observation supporting a decision | Evidence artifact record |
| Decision | Source-grounded judgment, status, reason, and uncertainty | Decision record |
| Derived view | Tables, figures, counts, and display symbols | Generated only |

The Study, Candidate Operation, HPAT Transition, and nine relation records are the scientific
coding objects. Evidence Artifacts and Decisions document how a judgment is supported; they are not
additional Candidates, HPATs, or relations. Controls and Cross-transition Relations are conditional
extensions and do not expand the nine-relation reliability population. Derived views are reporting
outputs, never independent coding objects.

The contracts in this appendix define recording, provenance, aggregation, and release interfaces after the
semantic path is decided. They may constrain what must be recorded, but they do not add a new
scientific judgment beyond Sections 2-6.

Decisions do not replace substantive records. Derived displays are generated from authoritative records and must not be hand-edited.

### Study record

Required fields:

~~~
study_id
source_packet_id
review_scope_id
review_scope_version
review_scope_complete
input_manifest_sha256
study_title
stable_source_id
canonical_version
publication_status
source_availability
study_types[]
corpus_roles[]
primary_analytical_role
phenomenon_classes[]
evidence_functions[]
permitted_claim_uses[]
settings[]
empirical_scope
inclusion_reason
candidate_operation_count
qualified_hpat_count
hpat_scope_status
codebook_version
coder
review_status
~~~

Conditional or maintained fields:

~~~
current_reference_number
version_relationship
publication_date
pdf_sha256
source_native_metrics[]
boundary_note
final_adoption_status
unavailable_material_reason
~~~

The review-scope fields are Study-level completion and provenance metadata. `source_packet_id` names
the fixed source bundle; `review_scope_id` and `review_scope_version` identify the declared set of
studies and locations; `review_scope_complete` records whether that scope was fully reviewed; and
`input_manifest_sha256` identifies the frozen input manifest used by the pass. When the scope is not
complete, `unavailable_material_reason` records the missing or unresolved material and locator. These
fields do not create Candidate judgments and must not be copied into a Candidate as scientific values.

`review_scope_complete` uses `true`, `false`, or `indeterminate`. Use `true` only when every declared
study and source location in the scope was reviewed or its status was explicitly recorded; use `false`
when declared material was unavailable or not reviewed; use `indeterminate` when completion cannot be
resolved from the records. A false or indeterminate value requires `unavailable_material_reason`.

hpat_scope_status values:

~~~
zero_qualified_hpat
aggregate_only
one_or_more_qualified_hpats
indeterminate
~~~

candidate_operation_count and qualified_hpat_count are derived after the completion review. hpat_scope_status is a derived study summary and does not imply that every source unit is a qualified HPAT. It replaces the ambiguous v2.1 term `transition_scope_status` for v3.2 records.

Derive `hpat_scope_status` in this order:

1. `one_or_more_qualified_hpats` when `qualified_hpat_count > 0`.
2. `aggregate_only` when candidate discovery is complete, the source contributes only source-native aggregates, and no candidate operation can be resolved without invention.
3. `indeterminate` when candidate discovery, model mediation, or privilege eligibility remains unresolved and no qualified HPAT has been established.
4. `zero_qualified_hpat` when candidate and eligibility review are complete, no unresolved gate remains, and `qualified_hpat_count = 0`.

`candidate_operation_count` counts Candidate Operation records created after Q1. It includes candidates later coded as `not_consequential`, `model_mediation_status=not_established`, `hpat_eligibility=Not established`, or `hpat_eligibility=Indeterminate`. These mutually exclusive derivation rules are applied only after the completion review.

Common corpus_roles values:

~~~
core_direct
adjacent_mechanism
contextual_background
~~~

study_types may include survey, attack_study, benchmark, measurement, control_design, control_evaluation, case_study, formal_analysis, deployment_or_incident, and other.

evidence_functions may include mechanism_evidence, runtime_evidence, postcondition_evidence, control_evidence, formal_evidence, measurement_evidence, survey_synthesis, and contextual_evidence.

### Public study-record projection

`data/study_records.csv` publishes the identity, bibliographic, canonical-source, full-text, review-scope,
zero-HPAT, and coder-provenance fields needed to interpret the released coding records. It does not
duplicate study classifications or corpus labels whose values do not alter the released Candidate,
HPAT, evidence, decision, control, or contribution-role records.

### Candidate Operation record

The public candidate CSV fields are:

~~~
candidate_operation_id
adjudicated_operation_id
study_id
source_unit_type
source_extraction_unit_id
source_native_atomicity
scenario_or_condition
operation_description
operation_type
target_or_recipient
q2_gate
q3_gate
q4_gate
q5_gate
consequentiality_status
model_mediation_status
model_mediation_evidence
hpat_eligibility
privilege_basis_type
privilege_basis_description
privilege_evidence_status
privilege_partial_qualifier
q4_governed_object
q4_source_locator
q5_operation_basis_link
q5_source_locator
source_locator
~~~

The public Candidate record includes `q2_gate`, `q3_gate`, `q4_gate`, and `q5_gate`. During
independent coding, these four fields are the only entered eligibility values and each accepts only
`Established`, `Not established`, or `Indeterminate`. `consequentiality_status` and
`model_mediation_status` are derived semantic projections, and `hpat_eligibility` is derived from the
four gates. Package assembly generates these three derived fields; none is an independent coder
judgment. `Present-direct` and `Present-partial` are evidence-status values and must never be entered
as gate values.
The Candidate record must preserve the Q1 evidence through `operation_description`,
`operation_type`, `target_or_recipient`, `source_extraction_unit_id`, and `source_locator`.
For `q4_gate=Established`, record the Q4 basis in the canonical `privilege_basis_type` field, together
with `q4_governed_object` and `q4_source_locator`. Do not create or maintain a separate
`q4_basis_type` field.
For `q5_gate=Established`, record `q5_operation_basis_link` and `q5_source_locator`.
Operational review progress is outside the public coding-record schema.

`adjudicated_operation_id` is downstream metadata. Leave it empty during independent source coding;
populate it only after candidate matching and adjudication.

### HPAT Transition record

### Core fields

~~~
hpat_id
candidate_operation_id
study_id
operation_id
source_extraction_unit_id
source_unit_type
source_native_atomicity
transition_record_granularity
privilege_basis_type
privilege_evidence_status
operation_type
target_resource
security_consequence
security_relevance_basis
codebook_version
coder
~~~

### Conditional and derived fields

The following fields are retained when the source, representation, relation, extension, or
post-coding process requires them:

~~~
adjudicated_operation_id
scenario_id
experimental_condition_id
represented_instance_count
selection_basis
realization_context
primary_runtime_position
risk_or_failure_source
influence_mechanism
instruction_source
origin_trust_status
principal
actor
affected_party_or_resource_owner
delegated_task_or_objective
task_constraints
authorization_basis
authorization_judgment
permission_subject
permission_resource
permission_action
permission_destination
permission_context_or_purpose
permission_lifetime
permission_quota
permission_attenuation
permission_revocation
permission_enforcement_point
granted_permission_scope
operation_stage_events[]
execution_disposition
effect_outcome
external_effect_description
resulting_state_description
empirical_chain_id
review_status
~~~

Equivalent fields in a derived view must retain exact mappings in the manifest. An HPAT is created
only after the Candidate Operation passes all eligibility gates. It inherits the Candidate's
Candidate boundary and is the only atomic transition record in the framework. Relation evidence
does not create a second HPAT for the same Candidate. Core identity and eligibility fields are
required; conditional fields are populated only when their source or post-coding process requires them.
Required means that the field slot and its decision status are recorded; it does not require a
positive source claim or permit an inferred value. Relation status, locator, evidence artifact,
qualifier, and decision reason remain required in the
corresponding relation or Decision record, even when a conditional HPAT field is empty.

`adjudicated_operation_id` is downstream metadata. Leave it empty during independent source coding;
populate it only after candidate matching and adjudication. `review_status` records workflow state
and does not replace a source-grounded field judgment.

### Runtime position

~~~
observation_context
interpretation_planning
action_selection
action_execution
external_effect_state
feedback
~~~

primary_runtime_position records where the concrete operation is situated. It does not replace operation_stage_events.

### Realization context

~~~
pre_execution_proposal
state_grounded_generated_artifact
interactive_runtime
other_source_defined
~~~

### Granularity and selection basis

Candidate boundaries are determined under the split, merge, and aggregate rules in Section 2. This
subsection records how an established HPAT is represented; it does not create, split, or merge
Candidate Operations.

transition_record_granularity is concrete_instance or scenario_class.

selection_basis is one of:

~~~
exhaustive_instances
exhaustive_scenario_classes
source_reported_case
preregistered_representative_case
unknown
~~~

`selection_basis` records the source's reporting basis. It does not authorize coder-selected
sampling. `preregistered_representative_case` is valid only when the source itself documents that
design. An author-selected example is not exhaustive unless the source says so, and a representative
example does not substitute for an aggregate denominator.

### Relation fields

### Authorization

authorization_basis records the task, objective, policy, approval, confirmation, or constraint that the source connects to the operation. Environmental content has no authority merely because the agent observes it.

authorization_judgment values:

~~~
authorized
conditional_pending_confirmation
unauthorized
undetermined
~~~

When the source does not report the basis or judgment, use evidence_status Not reported. Harmful, unsafe, attacked, benign, and user-requested labels do not determine authorization. User-requested misuse may be authorized in the task sense while remaining unsafe.

Authorization is always applicable to a qualified HPAT. Apply the shared core-predicate, status, and granularity rules in Section 4 and the complete Authorization decision tree in Section 5.1.

### Technical permission

The permission record is structured around the following fields. Every dimension is applicable to a qualified HPAT whose operation could exercise technical access, but a source may leave any dimension unreported. Candidate-level reporting of these dimensions is retained only as diagnostic audit Decisions under Section 3.

~~~
permission_subject
permission_resource
permission_action
permission_destination
permission_context_or_purpose
permission_lifetime
permission_quota
permission_attenuation
permission_revocation
permission_enforcement_point
~~~

`granted_permission_scope` is a concise source-faithful summary generated from, or checked against, these dimensions. It is not a substitute for them. A missing dimension is recorded as `Not reported`, not silently left absent from the evidence ledger.

Authorization and permission are independent. A task instruction does not prove technical enforcement. A technical capability does not prove authorization. A tool or account name does not prove resource- or operation-scoped permission.
Passing Q4/Q5 establishes HPAT eligibility only. It does not populate `permission_subject`,
`permission_resource`, `permission_action`, `permission_enforcement_point`, or any other
Technical Permission field, and it does not determine that relation's evidence status. These
fields must be coded from Technical Permission evidence itself.

### Operation stage and execution fields

operation_stage_events is cumulative and may contain:

~~~
proposed
issued_or_attempted
runtime_accepted
executed_at_mechanism_boundary
~~~

execution_disposition values:

~~~
blocked_or_rejected
failed
runtime_completed
partial
unresolved
not_applicable
~~~

| Stage events | Disposition | Interpretation |
|---|---|---|
| proposed | blocked_or_rejected | Pre-action guard prevented issuance or acceptance. |
| proposed, issued_or_attempted | failed | The operation was attempted but the interface or tool failed. |
| proposed, issued_or_attempted, runtime_accepted | partial | Runtime acceptance is established, but operation completion is not established; effect remains separate. |
| proposed, issued_or_attempted, runtime_accepted | runtime_completed | Use only when the source explicitly reports that the operation itself completed; effect remains separate. |
| proposed, issued_or_attempted, runtime_accepted, executed_at_mechanism_boundary | partial | A mechanism-boundary event is observed, but completion of the operation is not established; effect remains separate. |
| proposed, issued_or_attempted, runtime_accepted, executed_at_mechanism_boundary | runtime_completed | Use only when the source explicitly reports completion at that mechanism boundary; effect remains separate. |

`runtime_accepted` and `executed_at_mechanism_boundary` are stage observations, not completion
claims. A runtime return, success flag, dispatch event, or boundary event must not be promoted to
`runtime_completed` unless the source explicitly reports completion of the operation itself.
Runtime completion never by itself establishes external effect, resulting state, attribution,
containment, or recovery.

For a qualified HPAT, Operation Execution remains structurally applicable even when the operation
was blocked, failed, or only proposed. Do not use `execution_disposition=not_applicable` to represent
an unobserved or unsuccessful stage; preserve the observed stage and use `blocked_or_rejected`,
`failed`, `partial`, or `unresolved` as appropriate.

### External effect and resulting state fields

effect_outcome values:

~~~
occurred
not_occurred
unresolved
not_applicable
~~~

Use occurred only when the source establishes a specified external consequence, such as a target-system change, information disclosure, service-side operation, or recorded external commitment.

Use not_occurred only when an appropriate check confirms that the specified effect did not happen.

Use unresolved for runtime success without effect confirmation or for conflicting evidence.

resulting_state_description records a state or postcondition only when the source establishes it. A read or disclosure may have an external effect without a persistent state change. A state record is not automatically a deterministic postcondition oracle.

| Evidence | Establishes at most |
|---|---|
| Action trace, click, keystroke, command, or tool call | Issued or attempted operation |
| Runtime return, success flag, or execution trace | Runtime acceptance; completion only when the source explicitly reports completion of the operation |
| Post-operation observation | Observed effect or state in the reported setting |
| Deterministic oracle or independent confirmation | The specified postcondition within its scope |

Never infer effect or state from a proposal, trace, model output, or runtime success alone. A generated action artifact establishes what the artifact contains, not that a real service accepted it.

Apply Sections 5.5-5.6 when coding External Effect or Resulting State. A source-authored
task-level outcome can be Direct within a controlled setting when it is aligned to the coded
source-native unit. A family-level or benchmark-wide aggregate can support Partial only for an
aligned `scenario_class`; it cannot establish a `concrete_instance` result.

### Control fields

### Control semantics

control_semantics values may include:

~~~
detection_or_classification
advisory_or_feedback
pre_action_blocking
technical_permission_enforcement
runtime_mediation
post_effect_containment
recovery_or_restoration
~~~

Each control records control point, mechanism, boundary, validation, coverage, and bypass or residual exposure where reported.

Classification accuracy does not establish blocking. Blocking does not establish technical permission enforcement. Reduced ASR or leakage does not establish containment or recovery.

### Control Record contract

Create a Control record only for a qualified HPAT to which the source attaches a prevention, enforcement, mediation, containment, or recovery mechanism. A control reported only for a non-HPAT candidate remains a candidate-level audit Decision and does not become an HPAC Control record. Attribution is not a Control record: it remains a field and Decision on the HPAT.

~~~
control_record_id
study_id
hpat_id
control_semantics[]
control_point
control_mechanism
protected_boundary
control_condition
enforcement_subject
enforcement_resource
enforcement_action
technical_permission_enforcement
containment_scope
recovery_action
post_recovery_validation
residual_harm_or_unrecovered_state
evidence_status
partial_qualifier
source_locator
decision_reason
codebook_version
coder
review_status
~~~

`technical_attribution` and `attribution_linkage` must not be stored as a Control record field. `containment_scope`, `recovery_action`, and `post_recovery_validation` may be present only when their applicability conditions in Section 4 are met.

### Technical attribution

technical_attribution or attribution_linkage is established only when the source connects the operation to an acting principal, delegated identity, technical account, or equivalent accountable identity. A model ID, attacker label, trajectory, or author explanation alone is insufficient. Technical attribution is not legal or ethical responsibility.

### Containment

Containment limits a realized or ongoing effect, propagation, access, residual state, or residual exposure. Effect-prevention or pre-action blocking is not automatically containment.

A tested post-effect limit with relevant validation may be Present-direct. A design claim or unverified isolation is usually Present-partial. An experimental sandbox that protects researchers is not automatically a control implemented by the evaluated system.

Apply the complete Containment decision tree in Section 5.8. In particular, prevention,
pre-action blocking, refusal, isolation, or researcher-protective setup is not Containment unless
the source applies it after the relevant effect or exposure and links it to limiting that same harm.

### Recovery

For the Recovery relation, a Present status requires an identified recoverable effect, state, or
postcondition and an executed corrective action. Present-partial may omit or incompletely report
post-recovery validation. Present-direct additionally requires a source-reported post-recovery state
check. Record residual harm or unrecovered state where applicable.

Rollback APIs, checkpoints, plans, sandbox reset, sanitization, deactivation, quota expiry, retry, replanning, task restart, or environment reinitialization do not automatically establish validated security recovery.

Apply the complete Recovery decision tree in Section 5.9. A Present Recovery decision requires
an executed corrective action linked to the identified effect or state. Present-direct additionally
requires a source-reported post-recovery check within the stated setting.

### Decision record fields


~~~
decision_id
record_scope
study_id
target_record_type
target_record_id
target_field
substantive_value
evidence_status
evidence_artifacts[]
evidence_provenance[]
source_pdf
source_locator
decision_reason
missing_relation_or_condition
uncertainty
coverage_qualifier
claim_support_ceiling
codebook_version
coder
review_status
~~~

record_scope values:

~~~
source_extraction
study_field
candidate_field
transition_field
chain_relation_field
control_field
study_aggregate
table_cell
~~~

### Q4/Q5 decision mapping

The authoritative Q4 and Q5 outcomes are `q4_gate` and `q5_gate` in the Candidate record. Each
outcome is supported by a Decision with `record_scope=candidate_field`,
`target_record_type=candidate_operation`, and the relevant `target_record_id`. Use
`target_field=q4_privilege_basis` for the Q4 Decision and
`target_field=q5_operation_capability_link` for the Q5 Decision. These are provenance labels for the
evidence, reason, and uncertainty supporting the Candidate gate; they are not a second gate outcome
and do not create additional Candidate fields. The Candidate's single canonical Q4 basis field is
`privilege_basis_type`.

For independent coding, use the Q4 and Q5 forms as two separate coder-facing inputs. During package
assembly, map each form's `decision` to the corresponding Candidate gate and preserve its evidence,
reason, uncertainty, qualifier, and locator in a supporting Decision record. `source_text_locator`
is retained through the linked Evidence Artifact, and `q5_judgment_basis` is retained as evidence
provenance. The two judgments remain separate and must not be collapsed into one combined privilege
judgment.

The assigned locator anchors the Candidate operation but does not restrict source review. For Q2-Q5,
review the complete verified source as needed and preserve same-scenario alignment for assembled evidence.

### Evidence artifact fields


Each artifact contains at least:

~~~
evidence_artifact_id
study_id
candidate_operation_id
hpat_id
source_extraction_unit_id
supports_record_type
field_name
evidence_type
observation_mode
evidence_status
source_locator
faithful_excerpt_or_paraphrase
scope_and_condition
evidence_role
coder_id
~~~

observation_mode values:

~~~
author_narrative
static_artifact_analysis
projected_or_simulated_execution
runtime_trace_or_return
post_operation_observation
deterministic_checker_or_independent_confirmation
~~~

Evidence provenance may include original_experiment, system_evaluation, benchmark_trace, formal_model, case_study, survey_synthesis, design_claim, and other_verified.

### Claim-support ceiling


For operation, effect, state, and postcondition claims:

| Level | Evidence object | Highest supported claim |
|---|---|---|
| E0 | Author narrative or scenario description | Intended or claimed setup |
| E1 | Model output, plan, refusal, or proposed action | Proposal or decision |
| E2 | Action trace, click, command, or tool call | Issued or attempted operation |
| E3 | Runtime return, success flag, or execution trace | Runtime acceptance; completion only when the source explicitly reports completion of the operation |
| E4 | Post-operation observation | Observed effect or state in the reported environment |
| E5 | Deterministic oracle or independent confirmation | Specified postcondition within the checked scope |

The ceiling limits claims; it does not convert a low-level artifact into a negative finding.

### Study and corpus aggregation

Study-level derived fields may include highest_established_operation_stage, operation_stage_display, relation-status views, unobserved relations, strongest demonstrated relation, and display symbols for tables or figures. These are generated from decisions and authoritative records.

An aggregate denominator must state whether it counts studies, candidates, qualified HPATs, source rows, scenarios, runs, or another source-native unit. A study counts once or multiple times only under an explicitly declared aggregation rule. Indeterminate candidates are retained but excluded from an Established HPAT denominator.

### Analytical populations

The codebook defines two statistical populations with different purposes. They do not constitute two transition frameworks.

**Candidate diagnostic population.** This population contains Candidate Operations for which consequentiality and model mediation are established. It supports only eligibility and reporting audits, including the proportion that passes the independent privilege gate, reasons privilege linkage is not established, candidate-level reporting of authorization or technical permission, and explanations for zero-HPAT studies. Candidate-wide statistics must be explicitly labeled `candidate diagnostic` or `candidate-wide audit`. They must not be presented as HPAT, HPAC, transition-relation, or security-mechanism findings.

**HPAT synthesis population.** This population contains qualified HPAT records with an established independent privilege linkage. It is the primary transition population for HPAC synthesis, full relation coding, Sections 3-5 analytical claims, HPAC chain relations, Control records, and HPAT relation projections.

The default population for any unlabeled transition-level synthesis is the HPAT synthesis population. A candidate diagnostic result and an HPAT synthesis result may be compared only when both denominators and purposes are stated. Candidate Operations are eligibility objects; HPATs are the atomic transition units used for HPAC synthesis.

### Display projection

The public data preserves two fields for every applicable relation:

~~~
relation_status
partial_qualifier
~~~

The compact manuscript display uses the following mapping:

| Source-level status | Compact display | Public release requirement |
|---|---|---|
| Present-direct | Direct or check mark | Preserve the source-level status and evidence locator |
| Present-partial | Partial or circle | Preserve the qualifier; a circle is display compression, not one homogeneous category |
| Absent-explicit | Explicit absence or explanatory note | Never merge with source silence |
| Not reported | Not established or cross mark if the table defines that display | Preserve `Not reported` in the public data |
| Not applicable | Em dash | Exclude from the relation-specific applicable denominator |
| Indeterminate | Indeterminate or explanatory note | Do not convert to Direct, Partial, or explicit absence |

Any relation with substantial Partial coverage must publish the composition of `subset`, `conditional`, `proxy`, `design_only`, `mixed`, and `unknown` records. Corpus claims may not treat every Partial as equivalent evidence.

# Appendix B. QA, Validator, and Release

These checks govern package completeness and release. They do not replace source-grounded coding decisions in Sections 2-6.
Validation has two layers. Deterministic checks enforce controlled values, required fields, derived
projections, references, multiplicity, version, and manifest contracts when the required records are
provided. Semantic review flags identify obligations that still require reading the source, including
unitization, split/merge, duplicate reporting, same-scenario alignment, and aggregate handling. A
passing deterministic check never proves that a Candidate boundary or semantic judgment is correct.


### Public artifact requirements

Subject to safety review, the public coding projection contains the formal codebook, study and candidate records, qualified HPAT records, source-linked evidence, transition-field decisions, control records, cross-transition relations, a validation script, and a deterministic manifest. It excludes source PDFs and non-public safety-sensitive material.

The README describes the released record scope, evidence limits, and validation command. It does not claim to reproduce a source judgment beyond the evidence and decision records that are released.

### Validation checklist

Before a coding release is complete, verify:

- every included study has a stable public source URL or a documented availability status;
- every supplied Study record identifies the frozen `source_packet_id`, `review_scope_id`,
  `review_scope_version`, `review_scope_complete`, and `input_manifest_sha256`; an incomplete scope
  has an `unavailable_material_reason`;
- candidate discovery is exhaustive within the stated source units;
- every Candidate has a real source unit or locator, a legal `source_native_atomicity` value, and a recorded
  condition or reason when the boundary is unresolved;
- every split or merge is supported by a source-native distinction or an inseparable-operation
  rationale; relation differences alone do not create a new Candidate;
- every source aggregate preserves its source-native numerator, denominator, denominator unit, and
  coverage qualifier, and no aggregate is reverse-split without separately identified source units;
- `transition_record_granularity` is recorded only after HPAT eligibility and is not used to alter
  Candidate boundaries;
- every Candidate has all four authoritative gate values Q2-Q5 and their required evidence;
- every stored `consequentiality_status`, `model_mediation_status`, and `hpat_eligibility` value
  matches its deterministic gate projection;
- every Candidate has the required Q1-Q5 evidence, and any candidate-level audit
  Decision has a source locator and reason;
- every Established HPAT has model-mediation evidence and operation-to-capability evidence;
- every HPAT references one qualifying Candidate with the same source-native unit, and every qualified
  HPAT has exactly one record for each of the nine relation names;
- no Indeterminate candidate enters the HPAT denominator;
- no non-HPAT candidate is represented as a transition, HPAC chain endpoint, or HPAC Control record;
- every candidate-wide result is labeled as diagnostic or audit and is not presented as an HPAT finding;
- every full relation projection, HPAC chain analysis, and HPAT finding uses the qualified HPAT population unless an explicitly labeled comparison states otherwise;
- every positive relation has an evidence artifact, locator, and coverage qualifier;
- Present-partial has a partial qualifier or adjudication note;
- Present-partial for any of the nine relation-status fields affirmatively states that relation's
  core predicate;
- a Present status does not contain or semantically assert `Not reported`, absence of source-grounded
  evidence, or absence of the relation-specific result;
- Present-direct aggregate evidence is not attached to a `concrete_instance` HPAT;
- Authorization Present records contain a source-linked authorization basis and judgment;
- External Effect `Not applicable` records document pre-issuance blocking or rejection and the
  absence of an effect condition or external target;
- Resulting State Present records contain an affirmative postcondition rather than only a target,
  operation-success, or execution statement;
- Containment Present records contain a post-effect limiting action or condition linked to the same
  effect, exposure, or residual state;
- Recovery Present records contain an executed corrective action linked to the same effect or state,
  and Present-direct records also contain a post-recovery check;
- Containment and Recovery evidence is aligned to the same source-native task, example, panel, or
  scenario as the HPAT;
- Technical Attribution `Present-direct` records identify an accountable principal, account, delegated
  identity, or equivalent component; `Present-partial` records identify the connected model, agent, or
  delegated technical actor and state which identity, account, principal, or delegation scope is
  incomplete;
- no new final adjudication uses `higher_evidence_status`;
- runtime completion is not used as effect or state evidence;
- external effect is not used as resulting-state evidence without a state observation;
- controls, attribution, containment, and recovery are not inferred from one another;
- Persistence, Reuse, Propagation, Amplification, Delegation, and Post-recovery validation are used
  only when their Section 6 triggers are present and are not counted as additional nine relations;
- aggregate numerators and denominators retain source-native units;
- derived tables and figures are generated from records rather than hand-edited;
- coder identity and codebook version are recorded where the public schema carries them;
- manifest hashes and validation outputs are deterministic under a frozen release date.

### Release statement

This document is the complete v3.3.0 manual candidate for independent coding review. Candidate
Operations remain eligibility objects; HPATs remain the sole atomic transition units used for HPAC
synthesis. Version 3.3.0 does not add or remove an eligibility category,
privilege basis, source-unit type, transition layer, evidence status, partial qualifier, relation,
matching rule, population purpose, or relation meaning. It consolidates the source-native
unitization and aggregate rules while retaining the v3.2.3 Q4/Q5 and nine-relation protocol.

This manual changes no historical record. Existing ledgers remain labeled by their actual coding
version. It may be distributed for independent coding after the project owner confirms the manual
and its version hash. A data package may claim v3.3.0 only after both coders independently apply the
manual to the declared reassessment scope, comparison and source adjudication are complete,
unitization coverage is reported, validators pass, and a separately versioned data release is
generated.

---

### Field-consistency validation


The companion `validate_v3.3.0_relation_consistency.py` applies deterministic structural and lexical
checks and emits semantic review flags. With `--study-csv`, it checks the Study-level review-scope
metadata. With `--candidate-csv`, it requires the complete public Candidate interface, blocks invalid
gate values and the noncanonical `q4_basis_type` field, checks the Q2/Q3 semantic projections, requires
minimum Q1/Q4/Q5 evidence objects, and verifies that the stored derived `hpat_eligibility` agrees with
Q2-Q5. When the release root supplies relation and HPAT IDs, it checks Candidate/HPAT foreign-key and
exactly-nine relation multiplicity. It never assigns or changes a semantic status or Candidate boundary.

#### Release-blocking errors

0. When `--study-csv` is supplied, a Study record lacks required review-scope metadata, has an invalid
   `review_scope_complete` value, or marks an incomplete scope without an unavailable-material reason.
1. The public Candidate record lacks any required gate, derived projection, or Q4/Q5 evidence field,
   or contains the noncanonical `q4_basis_type` field.
2. A Q2-Q5 gate uses `Present-direct`, `Present-partial`, or any value outside
   `Established`, `Not established`, and `Indeterminate`.
3. `consequentiality_status` or `model_mediation_status` disagrees with its fixed Q2/Q3 mapping.
4. A Q1-established Candidate lacks a concrete operation, target/resource/recipient/object/postcondition,
   or source locator.
5. An Established Q4 lacks `privilege_basis_type`, a governed object/interface/state, or a source locator.
6. An Established Q5 lacks an operation-to-basis link or aligned source locator.
7. `hpat_eligibility` disagrees with the deterministic Q2-Q5 combination.

8. A Present status whose substantive value is empty or explicitly says the relation is not
   reported, is unsupported, or did not occur.
9. A Present-partial record without a valid partial qualifier or explicit coverage limit.
10. A `concrete_instance` Present-direct record supported only by an aggregate or family-level
   evidence statement.
11. A final v3.3.0 status disagreement adjudicated with `higher_evidence_status`.
12. A v3.3.0 adjudication reason outside the controlled classes when the coder statuses differ.
13. A v3.3.0 record whose codebook version is not `3.3.0`.
14. When release IDs are supplied, a relation references no qualified HPAT or a qualified HPAT does
    not have exactly one record for each of the nine relation names.

#### Mandatory human-review flags

1. Authorization Present without a source-linked basis and authorization judgment.
2. External Effect `Not applicable` without a pre-issuance block/rejection and no effect
   condition/target.
3. Resulting State Present whose value appears to state only a target, operation, or execution
   result rather than a postcondition.
4. Containment Present without a linked post-effect limiting action or condition.
5. Recovery Present without a linked executed corrective action; Present-direct without a
   post-recovery check.
6. Containment or Recovery evidence apparently taken from another example, task, panel, or scenario.
7. Technical Attribution `Present-partial` lacks an explicit note of the connected technical actor or
   the incomplete identity/account/principal/delegation scope.

These flags require source review because wording alone cannot establish source-unit alignment.
Validator output is a release gate and audit queue, not an automatic recoding decision.

### Candidate validation


Candidate validation is separate from relation validation. The conditions below are a normative
Candidate-package QA contract. The companion `validate_v3.3.0_relation_consistency.py` validates the
controlled Candidate interface when `--candidate-csv` is supplied, but it does not automatically decide
Candidate split/merge boundaries, duplicate reporting, or source alignment. A Candidate-aware checker
or documented human review is therefore required for those semantic obligations. The checks must not
infer a Candidate boundary or assign a semantic status:

#### Release-blocking errors

1. A Candidate lacks a real `source_extraction_unit_id`, operation description, or target/recipient
   when Q1 is Established.
2. `source_unit_type` is missing or outside the controlled values defined in Section 2.
3. `source_native_atomicity` is outside `single_operation`, `source_aggregate`, or `unresolved`.
4. An `unresolved` unit has no source locator and reason.
5. A source aggregate lacks its declared denominator metadata when an aggregate result is recorded.
6. A child Candidate has no documented source-native split distinction or parent mapping.
7. An HPAT has no qualifying Candidate or has a boundary different from its Candidate without an
   adjudicated source-native unitization decision.

#### Mandatory human-review flags

1. Several Candidates share one source unit or locator but no distinct operation, target, condition, or
   independently reported outcome is recorded.
2. One Candidate contains multiple independently located operations or postcondition oracles.
3. A `scenario_class` HPAT is supported only by an aggregate whose numerator, denominator, or
   condition is missing.
4. A split appears to be based only on a relation difference, tool name, task label, or possible
   side effect.

These checks support audit and release preparation; they do not replace the source-grounded
split, merge, and aggregate rules in Section 2.

# Appendix C. Legacy Reference and Version History

This appendix preserves historical wording and the old-to-new section crosswalk. It is not an additional coding path.


**Status:** historical Q4/Q5 operational reference retained for traceability from v3.2.1/v3.2.2.
For new v3.3.0 coding, Section 3 and Sections 4-5 are controlling; this appendix does not
create a second Q4/Q5 decision path. Where wording overlaps, the current controlling sections govern.
It does not alter the HPAC/HPAT ontology, the nine relation names, or any existing ledger value
unless that record is independently re-assessed under the applicable contract.

## C.1 Configured capability and the independent privilege gate

This historical note is retained only for version traceability. Current Q4 and Q5 judgments are governed
exclusively by Section 3. Configured, controlled, simulated, sandboxed, or mocked settings are neither
automatically qualifying nor automatically disqualifying; apply the qualifying-relation,
governed-resource/interface/service/state, scenario-applicability, and operation-linkage requirements
in Section 3.

## C.2 Authorization is distinct from task context

The task, objective, benign carrier instruction, attack goal, or evaluation condition is not automatically valid authorization. `authorization_basis` records what the source connects to the operation; `authorization_judgment` records the source-supported judgment about that basis. A task or policy may support `Present-partial` when it is explicitly connected to the operation but validity, scope, or approval is incomplete. Silence or an unsafe label remains `Not reported`, not evidence of authorization or lack of authorization.

## C.3 Contextual influence versus direct model influence

Content, prompts, retrieved material, environment state, or evaluation conditions may be recorded as contextual influence when they are in scope for the operation. `Present-direct` influence requires source support that the relevant model interpretation, planning, or action selection was affected by that content or condition. A source that only reports co-occurrence, task setup, or a downstream outcome does not establish direct influence; retain the appropriate partial or unreported status.

## C.4 Source-native aggregates do not become atomic direct evidence

Percentages, scores, benchmark-wide rates, family-level outcomes, and other source-native aggregates
remain aggregate evidence. Candidate boundaries are determined under Section 2; this rule does not
authorize reverse-splitting. Aggregates may support an applicable or partial relation, but they do not
establish a direct per-HPAT execution, external effect, or resulting state unless the source
separately identifies the operation, target/postcondition, and observation unit. Preserve the
source-native denominator and do not reverse-split an aggregate.

## C.5 Resulting state requires a source-supported postcondition

`Resulting State` concerns a meaningful persistent, shared, or observable postcondition of the HPAT operation. A protected-information read or disclosure does not by itself create a separate post-read state; a separate later disclosure or state-changing operation is coded separately when the source supports it. An explicit source-reported postcondition may be direct even when the source does not provide a full runtime trace; a merely possible or inferred postcondition remains partial, unreported, or not applicable under the existing rules.

## C.6 Technical attribution is not model identity

A model name, agent label, attacker label, trajectory, or generic “the agent” reference does not establish accountable technical attribution by itself. `Present-direct` attribution requires a source-supported link to an acting principal, delegated identity, technical account, or equivalent accountable component. Where the source identifies only a model or trajectory and does not establish that linkage, do not infer attribution; use the existing evidence-status rules.

## C.7 Containment is post-effect limitation, not prevention

Containment limits a realized or ongoing effect, propagation, residual access, residual state, or exposure. Pre-action blocking, refusal, isolation, sandboxing, or researcher-protective environment setup is not automatically containment. A containment claim should identify the relevant realized/ongoing consequence or an explicit post-effect limitation. Use `Not applicable` only when the source explicitly establishes that no such prerequisite condition exists; if the source is silent about whether a realized or ongoing condition exists, use `Not reported`.

## C.8 Recovery requires corrective action; direct recovery requires validation

Recovery requires an identified effect, state, or postcondition requiring recovery and an executed
reversal, repair, restoration, or compensation action. Present-partial may omit or incompletely report
post-recovery validation; Present-direct additionally requires a source-reported post-recovery state
check. “Restore,” reset, retry, replanning, task restart, sandbox reset, deactivation, or environment
reinitialization language alone does not establish recovery. A pre-effect denial with an explicitly
absent recoverable state is structurally `Not applicable`; if the source is silent about whether a
recoverable condition exists, use `Not reported`.

## C.9 Applicability and evidence status remain separate

`Not applicable` is reserved for a relation structurally outside the source-reported transition or condition. `Not reported` means the relation is applicable but the source does not report enough information. Missing permission scope, lifetime, enforcement, validation, or postcondition detail must not be converted to `Not applicable` merely because the source is silent. Conversely, a structurally inapplicable relation must not be treated as a negative finding.

## Section crosswalk

| v3.2.3 location | v3.3.0 location | Treatment |
|---|---|---|
| Sections 1-2 | Section 1 | Scope, hierarchy, and coder path consolidated |
| Section 3 | Section 3 | Q1-Q5 eligibility retained |
| Sections 4-5 and 19 | Sections 2-4 | Unitization and evidence rules consolidated |
| Sections 6-10, 17, and 20 | Appendix A | Recording, schema, and aggregation contracts |
| Sections 11 and 18 | Section 6 | Optional Cross-transition relations and records |
| Sections 12-16 and Appendix D.3 | Section 5 | Nine relation rules and record fields in Appendix A |
| Section 21 and Appendix D.4 | Section 8 | Independent coding, reliability, and adjudication |
| Sections 22-23 | Section 7 | Boundary and worked examples |
| Appendix D.5-D.6 and Sections 25-27 | Appendix B | Validation and release controls |
| Appendix C and version history | Appendix C | Historical reference only; not an additional decision path |

### Version 3.2.2 (2026-08-31)

- Adds a shared core-predicate floor and source-native granularity rule for Authorization, External
  Effect, Resulting State, Containment, and Recovery.
- Adds complete relation-specific decision trees for the five targeted relations without changing
  their names, meanings, applicability denominators, or evidence-status vocabulary.
- Retires `higher_evidence_status` and prohibits nominally stronger-status adjudication.
- Restricts `primary_tie_break` to substantively equivalent, source-faithful wording.
- Adds eleven controlled adjudication reason classes, including a reason for rejecting both coder
  inputs.
- Adds machine-checkable field-consistency gates and identifies semantic checks that must remain
  human review flags rather than automatic reclassification.
- Preserves historical data labels and requires a new independent pass before any data product can
  claim v3.2.2.

### Version 3.2.3 (2026-09-03)

- Extends the shared core-predicate, applicability, source-unit, and evidence-status protocol to all
  nine frozen relations.
- Adds deterministic decision rules for Influence, Operation Execution, Technical Attribution, and
  Technical Permission while retaining the v3.2.2 rules for Authorization, External Effect,
  Resulting State, Containment, and Recovery.
- Defines relation status values as non-ordinal decision classes with explicit relation-specific
  prerequisites; a more affirmative label may not be selected merely because it is stronger.
- Adds cross-relation non-inheritance rules so Q4/Q5, authorization, execution, effects, states,
  controls, attribution, containment, and recovery cannot silently establish one another.
- Makes source-native unit alignment and split/merge/partial-overlap handling part of the reliability
  protocol; only strict one-to-one pairs are eligible for direct pairwise agreement statistics.
- Corrects the execution-stage table: `runtime_accepted` and
  `executed_at_mechanism_boundary` do not imply `runtime_completed` without an explicit completion
  statement.
- Clarifies that Q4/Q5 establish eligibility but never auto-populate Technical Permission, and
  separates the nine relation-status fields from conditional persistence, reuse, propagation,
  amplification, and post-recovery-validation dimensions.
- Resolves the `Not applicable` versus `Not reported` boundary for Resulting State and Containment,
  and aligns the validator's Execution and Technical Permission checks with these rules.
- Updates the validator contract and version boundary for v3.2.3 records. No historical record is
  relabeled by this candidate release.

### Version 3.3.0 (initial 2026-09-11; final consolidation 2026-09-15)

- Clarifies that Q1 is applied after source-unit boundary resolution and before a Candidate Operation
  record is created; Q2-Q5 then apply to that Candidate.
- Refines the pre-release coder path so Q1 is documented through the source unit and operation that
  create a Candidate, Q2-Q5 evidence is retained for that Candidate, and candidate-level audit
  records beyond eligibility are recorded only when the source explicitly reports the relevant fact;
  HPAT relation records remain the controlling relation layer.
- Makes the Candidate boundary rule explicit: downstream relation differences cannot create a
  split or prevent a merge unless the source separately reports an operation, condition, or outcome
  unit.
- Separates core HPAT identity and eligibility fields from conditional, derived, and workflow
  fields in Appendix A without removing the underlying field vocabulary.
- Establishes Section 2 as the main location for source units,
  Candidate boundaries, split/merge decisions, repeated runs, and source-native aggregates.
- Adds explicit split, merge, and aggregate rules with a default source-unit rule, controlled split and
  merge conditions, an unresolved-boundary outcome, and a prohibition on coder-selected sampling.
- Separates `source_native_atomicity` from the later HPAT
  `transition_record_granularity` and clarifies that Section 4 governs evidence alignment rather
  than Candidate boundaries.
- Makes `selection_basis` a record of the source's reporting basis and preserves the prohibition on
  reverse-splitting aggregates or treating representative examples as exhaustive.
- Removes duplicated split/merge rules from Section 2 and makes the workflow in Section 8 refer to
  Section 2 as the controlling unitization rule.
- Adds a coding workflow so that source review, unitization,
  eligibility, Candidate audit, HPAT relation coding, optional Cross-transition relations, and provenance follow
  one sequence.
- Separates Candidate and HPAT records from Evidence Artifacts, Decisions, Controls, Cross-transition
  Relations, and derived views; these records do not create additional HPAT or reliability
  populations.
- Makes the nine-relation decision order explicit and separates Persistence, Reuse, Propagation,
  Amplification, Delegation, and Post-recovery validation from the nine relation-status fields.
- Stores the authoritative Q4 and Q5 gate outcomes in the public Candidate record and preserves
  their supporting privilege-basis and operation-to-capability evidence as independent candidate-field
  Decisions. Existing candidate forms remain projections of this single gate interface.
- Makes `q2_gate`, `q3_gate`, `q4_gate`, and `q5_gate` the only authoritative eligibility inputs and
  publishes all four fields in the Candidate record.
- Defines the complete Q2/Q3 gate-to-status mappings, derives `hpat_eligibility`, and treats
  `consequentiality_status` and `model_mediation_status` as non-editable semantic projections.
- Makes `privilege_basis_type` the single canonical Candidate field for the Q4 basis; no separate
  `q4_basis_type` field is permitted.
- Adds four Q5 alignment checks for assembled evidence and clarifies that missing non-core permission
  dimensions do not by themselves make the operation-to-capability link indeterminate.
- Includes policy-governed state among the protected or governed objects that must align for Q5.
- Adds concise source-unit boundary examples for end-to-end scenarios, table-row alternatives,
  appendix items, endpoint actions, side effects, and source-native aggregates.
- Orders the nine relation sections as Influence, Authorization, Technical Permission, Operation
  Execution, External Effect, Resulting State, Technical Attribution, Containment, and Recovery,
  and updates the affected appendix cross-references.
- Places the Q1-Q5 rules in Section 3 and the relation-status rules in Sections 4-5; retained
  Appendix C is historical reference only.
- Separates Cross-transition relation types from control/context modules and states that
  `Post-recovery validation` is not a Cross-transition `relation_type`.
- Adds Candidate split/merge release-blocking errors and human-review flags to the validation
  contract. The companion validator remains relation-focused; these Candidate checks are a
  normative QA contract and are not claimed as automated by the relation validator.
- Retains `influences`, `produces_state`, `contained_by`, and `recovered_by` as
  `legacy-v3.2.3-only` Cross-transition values for historical compatibility; new v3.3.0 coding
  emits only the five values listed in Section 6.
- Final consolidation (2026-09-15) adds the declared Study review-scope and source-packet metadata,
  completes the source-scope and Candidate-discovery contract, clarifies information-processing versus
  consequential operations at Q2, permits explicitly aligned study-level Q3 mediation evidence,
  defines the Q4 three-value evidence boundary, and records the illustrative Q4/Q5 contrast without
  replacing the deterministic combination table.
- Final consolidation also permits explicit return to Pass 1 for a genuine source-native unitization
  correction, keeps duplicate-reporting and aggregate decisions as semantic review obligations, and
  separates deterministic validator checks from mandatory human-review flags. It does not add a new
  Candidate type, ontology layer, relation, gate, evidence status, or version number.
- Post-stress-test operational consolidation (2026-09-16) preserves the privilege-bearing capability
  definition while making Section 3 the sole detailed Q4/Q5 authority. It requires the qualifying
  relation, the resource/interface/service/state governed by that relation, and scenario applicability
  for Q4; clarifies affirmative non-linkage versus unresolved linkage at Q5; and states that controlled
  basis labels classify an independently established basis rather than establishing it.
- Targeted interface follow-up (2026-09-16) clarifies that the Q4/Q5 combination table derives HPAT
  status but does not authorize an Established Q5 without an Established Q4 basis; adds the accountable
  technical-context floor for Technical Attribution `Present-partial`; and makes an out-of-vocabulary
  `source_unit_type` a release-blocking validation error. No ontology, Candidate type, gate, relation,
  or version number is added.
- Final boundary clarification (2026-09-17) states that full, unrestricted, or configured system-level
  access is evidence of technical availability rather than a sufficient Q4 access relation, and separates
  taxonomy, dimension, impact-category, and capability labels from source-native operation units or
  operation classes eligible for Q1. It does not add an ontology element, Candidate type, gate, relation,
  evidence status, or version number, and it does not relabel existing records.
- Candidate-boundary consolidation (2026-09-18) tightens the split requirement to a source-reported
  boundary plus independent Q1 content, clarifies when parent scenarios or aggregates are not separate
  Candidates from their child operations, and makes the minimum Q1 content for a source-defined
  operation class explicit. It does not add a migration workflow, Candidate type, field, gate, relation,
  evidence status, or version number.
- Does not relabel, overwrite, or reinterpret any v3.2.3 or earlier record.

### Version 3.2.1 (2026-08-29)

Version 3.2.1 clarified the v3.2 Q4/Q5 privilege boundary while preserving the existing HPAC
relation set, Candidate/HPAT hierarchy, frozen population definitions, source-unit types, and
relation meanings. It separated Q4 privilege-basis existence/applicability from Q5
operation-to-capability linkage; permitted deterministic cross-section evidence assembly;
distinguished explicit absence from unresolved linkage; and stated the Q4/Q5-to-eligibility
combination rule. It did not authorize automatic recoding of historical records.
