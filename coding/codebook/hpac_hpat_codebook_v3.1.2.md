# HPAC/HPAT Codebook v3.1.2

Version: 3.1.2
Status: Frozen coding contract for manual source coding and public record interpretation
Date: 2026-08-13
Scope: final frozen computer-use-agent security review corpus
Coding population: the final frozen CUA review corpus. Foundational security sources supply conceptual provenance and are excluded from the transition and HPAT denominators unless separately admitted as corpus studies under the frozen inclusion protocol.
This codebook defines the coding records and derived public views released in this package.

## 1. Purpose

This codebook operationalizes the High-Privilege Action Chain (HPAC) as a source-grounded framework for comparing CUA security evidence. It separates:

1. Study identity and study-level scope.
2. Source-native Candidate Operations used only for eligibility and diagnostic audit.
3. Qualified High-Privilege Action Transitions (HPATs), the sole atomic transition units.
4. Cross-transition relations.
5. Technical attribution.
6. Controls, containment, and recovery.
7. Evidence artifacts and source-grounded decisions.
8. Derived tables, figures, and corpus summaries.

The codebook answers three separate questions:

1. What does the source report, and at what source-native unit?
2. Does a concrete operation satisfy the consequentiality, model-mediation, and independent privilege gates required for HPAT eligibility?
3. Which authorization, permission, operation, effect, state, attribution, containment, recovery, and cross-transition relations does the source establish?

Mandatory principles:

- Preserve the source-native unit, condition, denominator, wording, and locator before interpretation.
- A study may have zero, one, or many candidates and zero, one, or many qualified HPATs.
- A candidate is not an HPAT until every eligibility gate is passed.
- Candidate Operations are eligibility objects; HPATs are the atomic transition units used for HPAC synthesis.
- Every model-mediated consequential candidate receives the candidate-level audit Decisions defined in Section 9, whether or not it qualifies as an HPAT. These Decisions preserve source-reported material without creating a second transition construct.
- Only qualified HPATs receive full relation coding under Sections 10-16.
- Authorization, technical permission, execution, external effect, resulting state, attribution, containment, and recovery are separate fields.
- Silence is not an absence finding.
- Aggregate results remain aggregate results; do not invent atomic operations from percentages or scores.
- Every judgment needs a source locator and decision reason.
- Display symbols and corpus percentages are derived, never hand-entered.

## 2. Analytical hierarchy

### 2.1 High-Privilege Action Chain

HPAC is the macroscopic organizing structure for security-relevant influence across a CUA execution context. It may connect a delegated task or governing objective, acquired context, interpretation and planning, action selection, action execution, external effect, resulting state, feedback, persistence, reuse, propagation, attribution, containment, and recovery.

HPAC is not a claim that every source reports every link. A source may contribute candidate-level audit evidence, one qualified HPAT, one or more HPAC relations, or a source-native aggregate without establishing a complete chain instance.

### 2.2 Protected resource

A protected resource is information, system state, service, identity-bound interface, account, credential, persistent memory, shared workspace, or principal-facing channel constrained by identity, credentials, technical permission, confidentiality expectation, delegation, or task policy.

Examples include private files, code repositories, browser sessions, cookies, tokens, forms, email, accounts, restricted APIs, CLI or GUI operations, MCP resources, persistent memory, shared workspaces, and multi-agent communication state. Public navigation and ordinary local interaction are not protected-resource access merely because a CUA performs them.

### 2.3 Consequential operation

A consequential operation is a concrete operation that can do at least one of the following:

- read, disclose, transmit, or export protected information;
- create, modify, delete, submit, or transmit persistent or shared state;
- communicate, authenticate, commit, purchase, publish, or make a representation for a principal;
- invoke a service with an external or security-relevant side effect;
- change identity, permission, policy, credential, or delegated access;
- write state that can influence later decisions or actions;
- delegate a task, authority, or access to another actor.

Consequentiality identifies a candidate. It does not establish model mediation, privilege, authorization, execution, effect, or state.

### 2.4 Privilege-bearing capability

A privilege-bearing capability is an agent-available capability grounded in an identifiable identity-, credential-, session-, permission-, delegation-, or policy-based access relation to a protected resource, principal-bound interface or service, or policy-governed state relevant to the operation under review. The access relation must be connected to the operation under review.

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

### 2.5 High-Privilege Action Transition

An HPAT occurs when model-mediated interpretation, planning, or action selection yields a concrete proposed, attempted, or executed consequential operation whose realization would exercise a privilege-bearing capability, and the source establishes the connection between that capability and the operation.

An HPAT requires:

1. A concrete proposed, attempted, blocked, failed, or executed operation.
2. An identifiable target, resource, recipient, object, or relevant postcondition.
3. Consequentiality under Section 2.3.
4. Source-supported model mediation and privilege-bearing linkage under Section 3.

HPAT eligibility does not require valid authorization, fully reported technical permission scope, operation execution, an external effect, a resulting state, or successful recovery. Those are separately coded relations.

### 2.6 Candidate operation

A candidate operation is a source-native operation retained for eligibility review. Candidates that fail model mediation or privilege linkage remain in the audit ledger with the failing status. They are not silently deleted.

### 2.7 Empirical chain instance

An empirical chain instance is a source-supported sequence of one or more HPATs and/or source-established context or state nodes connected by a relation. A single HPAT may stand alone when no cross-transition relation is established.

### 2.8 Study-level aggregate

A study-level aggregate is a source-native count, percentage, category, score, or qualitative result covering multiple units. It is represented by a study-level decision and denominator metadata. It is not converted into a fabricated transition.

## 3. Eligibility sequence

~~~
source-native candidate operation
    -> consequentiality gate
    -> model-mediation gate
    -> candidate-level audit Decisions
    -> independent privilege gate
       -> Established: create qualified HPAT and perform full relation coding
       -> Not established or Indeterminate: retain Candidate Operation and audit Decisions; do not create a transition
~~~

The gates are applied in this order. A later gate cannot justify an earlier candidate. The privilege decision determines HPAT membership. Candidate-level audit Decisions preserve reporting evidence without assigning transition status to a non-HPAT candidate.

### 3.1 Q1: concrete operation

The source must report a proposed, attempted, blocked, failed, or executed operation located in a source-native unit. The operation must identify an operation type and a target, resource, recipient, object, or relevant postcondition.

A generic task, tool description, attack name, unsafe score, or model output without an operation is insufficient.

If Q1 fails, do not create a candidate record. Record the source-native unit in the study completion record with `candidate_discovery_status=no_candidate_operation` and its locator and reason. `candidate_operation_status` is not a field in the candidate schema.

### 3.2 Q2: consequentiality

The operation must meet Section 2.3. Wrong answers, refusal behavior, generic unsafe scores, ordinary public navigation, a tool description, and a benchmark label are excluded unless the source reports a distinct operation and consequential target or postcondition.

If Q2 fails, set consequentiality_status to not_consequential and retain the rationale. The study may still contribute methodological, reliability, or contextual evidence.

### 3.3 Q3: model mediation

model_mediation_status has three values:

| Value | Rule |
|---|---|
| established | The source connects model interpretation, planning, selection, or model-generated action choice to the concrete operation. |
| not_established | The operation is assigned to a human, static script, deterministic protocol routine, benchmark generator, stochastic procedure, verifier, or other non-model actor. |
| indeterminate | The issuing actor or mechanism cannot be distinguished. |

The following do not establish model mediation alone: a task prompt; a tool or service description; an architecture diagram; a policy-selection output when the protected operation is not executed; a browser-automation proxy used instead of a compromised model; a verifier or conformance test; and automatic logging, signing, or completion.

Only established model mediation may proceed to an HPAT eligibility decision of Established.

### 3.4 Q4: independent privilege basis

The source must identify a privilege-bearing access basis for the concrete operation. The evidence must identify both the basis and the operation-to-basis link.

Examples include a named account, authenticated session, credential, token, permission-scoped interface, delegated capability, authenticated or permission-governed access to a protected resource, policy-governed state, or principal-bound service. A protected resource without an established access relation is the target of an operation, not a privilege basis.

Trust-boundary crossing, external effect, code execution, sandboxing, generic access, and the word privileged do not pass Q4 by themselves.

### 3.5 Q5: operation-to-capability linkage

The source must connect the privilege basis to the concrete operation. A task table, designed scenario, mock service, harness, or architecture walkthrough may pass Q5 when it explicitly makes this connection. Such evidence is normally Present-partial with a qualifier such as subset, conditional, proxy, design_only, or mixed.

If Q4 and Q5 are established, set hpat_eligibility to Established. If a capability is present but the source does not connect it to the operation, set hpat_eligibility to Not established. If the source is contradictory or cannot distinguish the linkage, set hpat_eligibility to Indeterminate.

Indeterminate candidates are retained but excluded from the Established HPAT denominator.

## 4. Eligibility and evidence-status separation

hpat_eligibility answers whether a candidate belongs to the HPAT population. privilege_evidence_status answers how completely the source reports the privilege linkage. They are separate.

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

### 4.1 Controlled privilege-basis values

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

`other_access_basis` requires a source-faithful explanation in `privilege_basis_description` and a later adjudication decision; it is not a license to add a new category during coding. `none_established` may appear only when `hpat_eligibility=Not established`. `indeterminate_basis` may appear only when `hpat_eligibility=Indeterminate`.

The following source-label variants map to the v3.1.2 controlled vocabulary:

| Source-label variant | v3.1.2 controlled value |
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

### 4.2 Privilege-basis existence versus technical permission scope

The privilege gate asks whether the source establishes that the model-mediated operation would exercise a protected or principal-bound access relation. `granted_permission_scope` asks how the system constrains that access at runtime. These judgments deliberately differ:

| Source establishes | Privilege gate | Permission-scope coding |
|---|---|---|
| Authenticated account can access a private folder; resource/action scope is not described | Established | Applicable; `Not reported` for unreported scope dimensions |
| Named API key is used for a concrete call; destination and lifetime are not described | Established | Applicable; `Present-partial` or `Not reported` according to the reported dimensions |
| A private file is named, but the source does not show the agent has access | Not established or Indeterminate | Permission is applicable to the candidate, but no HPAT is created |
| A task prompt says “send email” without account/session/credential evidence | Not established | Permission remains applicable to the candidate and is not inferred |
| A policy-governed memory write is model-mediated and the policy authorizes the state interface | Established | Applicable; separately code the reported enforcement dimensions |

Privilege-basis existence must never be used to fill an unreported permission-scope dimension. Conversely, an incomplete permission-scope record does not invalidate an otherwise established privilege linkage.

## 5. Source units, atomicity, and candidate discovery

### 5.1 Source unit types

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

source_extraction_unit_id must identify an actual source anchor, such as a named table row, figure step, trace segment, scenario, appendix item, algorithm, protocol test, or page-local passage. A generated row number is not an extraction anchor.

### 5.2 Source-native atomicity

source_native_atomicity is one of:

~~~
single_operation
source_aggregate
unresolved
~~~

single_operation means that the source resolves one operation and target or postcondition.

source_aggregate means that the source deliberately reports a family of variants as one unit.

unresolved means that the source does not permit stable atomicity without invention.

Candidate discovery is exhaustive within the source-reported distinct security-relevant operation units or operation classes that the source makes available for review. It does not mean that a coder must enumerate every repeated run in a large benchmark, every trace instance, or every member of a source-native aggregate. When a source reports a large run set, enumerate its distinct source-native operation classes and preserve the run-level denominator as an aggregate. Representative sampling by the coder is not permitted. A source-native aggregate must not be reverse-split unless the source separately identifies the operations, targets, or postconditions. A row that separately reports deletion, modification, permission change, and service disruption must not be collapsed into a generic shell operation.

### 5.3 Conditions and repeated runs

Baseline, guarded, attacked, repaired, repeated, or model-specific runs remain conditions on one candidate when the actor, operation, target, privilege basis, and reported postcondition do not change. They become separate candidates when any of those elements changes or when the source supplies independent operation-level locators or postcondition oracles.

## 6. Record layers and authority

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

Decisions do not replace substantive records. Derived displays are generated from authoritative records and must not be hand-edited.

## 7. Study record contract

Required fields:

~~~
study_id
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
~~~

hpat_scope_status values:

~~~
zero_qualified_hpat
aggregate_only
one_or_more_qualified_hpats
indeterminate
~~~

candidate_operation_count and qualified_hpat_count are derived after the completion review. hpat_scope_status is a derived study summary and does not imply that every source unit is a qualified HPAT. It replaces the ambiguous v2.1 term `transition_scope_status` for v3.1.2 records.

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

### 7.1 Public study-record projection

`data/study_records.csv` publishes the identity, bibliographic, canonical-source, full-text, zero-HPAT, and coder-provenance fields needed to interpret the released coding records. It does not duplicate study classifications or corpus labels whose values do not alter the released candidate, HPAT, evidence, decision, control, or contribution-role records.

## 8. Candidate Operation record contract

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
consequentiality_status
model_mediation_status
model_mediation_evidence
hpat_eligibility
privilege_basis_type
privilege_basis_description
privilege_evidence_status
privilege_partial_qualifier
source_locator
~~~
Operational review progress is outside the public coding-record schema.

## 9. Candidate-level audit Decision contract

Candidate Operations are eligibility objects, not transitions. Every candidate with `consequentiality_status=consequential` and `model_mediation_status=established` receives candidate-level audit Decisions before or alongside the independent privilege decision. No intermediate transition or relation-record layer is created.

The audit preserves only source-grounded material needed to explain eligibility, reporting gaps, and zero-HPAT outcomes. It may address:

~~~
privilege_basis
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

Each item is stored as a Decision under Section 17 with `record_scope=candidate_field`, `target_record_type=candidate_operation`, and `target_record_id=candidate_operation_id`. The Decision records the evidence status, source locator, source-faithful value or summary, missing relation or condition, and reason. Candidate audit Decisions do not populate an HPAT field, establish an HPAC relation, create a chain node, or enter an HPAT relation denominator.

For a non-HPAT candidate, a direct report of execution, effect, state, authorization, or permission remains auditable evidence about reporting practice. It is not full relation coding and must not be presented as an HPAT finding. If the candidate later qualifies after adjudication, its evidence artifacts may support the newly created HPAT Decisions without changing the original locators or source-faithful content.

## 10. HPAT Transition record contract

### 10.1 Required skeleton

~~~
hpat_id
candidate_operation_id
adjudicated_operation_id
study_id
scenario_id
operation_id
experimental_condition_id
source_extraction_unit_id
source_unit_type
source_native_atomicity
transition_record_granularity
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
privilege_basis_type
privilege_evidence_status
operation_type
target_resource
operation_stage_events[]
execution_disposition
effect_outcome
external_effect_description
resulting_state_description
security_consequence
security_relevance_basis
empirical_chain_id
codebook_version
coder
review_status
~~~

Equivalent fields in a derived view must retain exact mappings in the manifest. An HPAT is created only after the Candidate Operation passes all eligibility gates. It is the only atomic transition record in the framework. Empty substantive fields require a decision explaining Not reported, Not applicable, or Indeterminate.

### 10.2 Runtime position

~~~
observation_context
interpretation_planning
action_selection
action_execution
external_effect_state
feedback
~~~

primary_runtime_position records where the concrete operation is situated. It does not replace operation_stage_events.

### 10.3 Realization context

~~~
pre_execution_proposal
state_grounded_generated_artifact
interactive_runtime
other_source_defined
~~~

### 10.4 Granularity and selection basis

transition_record_granularity is concrete_instance or scenario_class.

selection_basis is one of:

~~~
exhaustive_instances
exhaustive_scenario_classes
source_reported_case
preregistered_representative_case
unknown
~~~

An author-selected example is not exhaustive unless the source says so. A representative example does not substitute for an aggregate denominator.

## 11. Cross-transition Relation record contract

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
influences
produces_state
persists_to
retrieved_or_reused_by
propagates_to
delegates_to
contained_by
recovered_by
amplified_by
~~~

The source and target are directional. `source_hpat_id` or `target_hpat_id` may be empty only when that endpoint is an explicitly described context or state node. Every Cross-transition Relation record must include at least one qualified HPAT endpoint. Relations among non-HPAT candidates may be preserved as candidate-level audit Decisions, but they are not HPAC chain relations. Text propagation does not automatically establish delegation, authority transfer, or permission transfer.

## 12. Authorization and technical permission

### 12.1 Authorization

authorization_basis records the task, objective, policy, approval, confirmation, or constraint that the source connects to the operation. Environmental content has no authority merely because the agent observes it.

authorization_judgment values:

~~~
authorized
conditional_pending_confirmation
unauthorized
undetermined
~~~

When the source does not report the basis or judgment, use evidence_status Not reported. Harmful, unsafe, attacked, benign, and user-requested labels do not determine authorization. User-requested misuse may be authorized in the task sense while remaining unsafe.

### 12.2 Technical permission

The permission record is structured around the following fields. Every dimension is applicable to a qualified HPAT whose operation could exercise technical access, but a source may leave any dimension unreported. Candidate-level reporting of these dimensions is retained only as diagnostic audit Decisions under Section 9.

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

## 13. Operation stages and execution disposition

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
| proposed, issued_or_attempted, runtime_accepted | runtime_completed | Runtime accepted or completed the operation; effect remains separate. |
| proposed, issued_or_attempted, runtime_accepted, executed_at_mechanism_boundary | runtime_completed | The mechanism boundary executed the operation; external effect remains separate. |

Runtime completion never by itself establishes external effect, resulting state, attribution, containment, or recovery.

## 14. Relation applicability contract

Applicability is decided before evidence status. `Not applicable` means that a relation is structurally outside the source-reported transition or study condition. It must never mean that the relation was not measured, was measured unsuccessfully, or was omitted by the source.

The following rules govern full relation coding for every qualified HPAT. Candidate Operations use the same distinctions only to classify candidate-level reporting Decisions under Section 9; those audit Decisions do not become HPAC relations.

| Relation or field | Applicable when | `Not applicable` only when | Do not use `Not applicable` when |
|---|---|---|---|
| Influence | The source reports content, instruction, context, or state that could shape the candidate's selection or realization | The source treats the operation as externally fixed and no influence source is in scope | The source simply does not report the planning path |
| Authorization | Always | Never for a model-mediated consequential candidate | The source does not report a task, policy, approval, or constraint; use `Not reported` |
| Technical permission | The candidate uses or is proposed to use any technical access, account, credential, service, tool, protected resource, or policy-governed state | The source establishes that the operation is wholly non-technical and cannot exercise access control | Scope, lifetime, or enforcement is missing; record the missing dimensions as `Not reported` |
| Operation and execution | Always | Never for a model-mediated consequential candidate | The source reports only a proposal or a failed attempt; record the appropriate stage and disposition |
| External effect | The operation is issued, attempted, accepted, executed, or the source evaluates an outside consequence | A pre-action proposal is blocked or rejected and the source has no effect condition or external target | An issued or executed operation lacks effect evidence; use `unresolved` or `Not reported` |
| Resulting state | The source identifies a meaningful persistent, shared, or observable postcondition | The operation is transient and no persistent or observable postcondition is meaningful in the reported setting | A meaningful state object exists but was not checked; use `Not reported` or `unresolved` |
| Persistence | The setting can retain relevant state across steps, tasks, sessions, or actors | The source establishes a single-step, non-retaining setting | Persistence is possible but unreported |
| Reuse | The setting has stored or transmitted material that could enter a later context or decision | No later decision point or reusable store exists in the source setting | Reuse is possible but not observed or reported |
| Propagation | The setting includes an actor, tool, resource, user, environment, or shared-state boundary across which influence or effect could move | No such boundary exists in the reported unit | A boundary exists but propagation is unreported |
| Amplification | The source defines a baseline and a possible change in scope, frequency, intensity, or consequence | No baseline or comparative dimension exists in the source design | A baseline exists but amplification is unreported |
| Technical attribution | The candidate has an actor, principal, delegated identity, account, or equivalent accountable technical component | The operation has no differentiable actor or identity by design | Actor or identity linkage is simply missing |
| Containment | An effect, ongoing exposure, propagation, residual access, or residual state has occurred or the source explicitly evaluates post-effect limitation | The source has neither a realized/exposed consequence nor a post-effect containment condition | The source provides prevention only, or does not report post-effect controls |
| Recovery | There is an effect, state, or postcondition requiring reversal, repair, restoration, or compensation, or the source explicitly evaluates recovery | There is no recoverable effect/state and no recovery condition | Recovery is relevant but unreported |
| Post-recovery validation | A recovery action is executed | No recovery action occurs | A recovery action occurs without a validation check; use `Not reported` |

The declared denominator for a relation projection must count only records for which that relation is applicable. The artifact must retain the applicability reason and evidence status separately.

## 15. External effect and resulting state

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
| Runtime return, success flag, or execution trace | Runtime acceptance or completion claim |
| Post-operation observation | Observed effect or state in the reported setting |
| Deterministic oracle or independent confirmation | The specified postcondition within its scope |

Never infer effect or state from a proposal, trace, model output, or runtime success alone. A generated action artifact establishes what the artifact contains, not that a real service accepted it.

## 16. Controls, attribution, containment, and recovery

### 16.1 Control semantics

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

### 16.2 Control Record contract

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

`technical_attribution` and `attribution_linkage` must not be stored as a Control record field. `containment_scope`, `recovery_action`, and `post_recovery_validation` may be present only when their applicability conditions in Section 14 are met.

### 16.3 Technical attribution

technical_attribution or attribution_linkage is established only when the source connects the operation to an acting principal, delegated identity, technical account, or equivalent accountable identity. A model ID, attacker label, trajectory, or author explanation alone is insufficient. Technical attribution is not legal or ethical responsibility.

### 16.4 Containment

Containment limits a realized or ongoing effect, propagation, access, residual state, or residual exposure. Effect-prevention or pre-action blocking is not automatically containment.

A tested post-effect limit with relevant validation may be Present-direct. A design claim or unverified isolation is usually Present-partial. An experimental sandbox that protects researchers is not automatically a control implemented by the evaluated system.

### 16.5 Recovery

Tested recovery requires:

1. an identified effect, state, or postcondition requiring recovery;
2. an executed reversal, repair, restoration, or compensation;
3. a post-recovery state check;
4. residual harm or unrecovered state recorded where applicable.

Rollback APIs, checkpoints, plans, sandbox reset, sanitization, deactivation, quota expiry, retry, replanning, task restart, or environment reinitialization do not automatically establish validated security recovery.

## 17. Evidence status and decision contract

### 17.1 Required Decision fields

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

### 17.2 Evidence statuses

| Status | Meaning |
|---|---|
| Present-direct | The source directly establishes the field for the relevant object and condition. |
| Present-partial | The source establishes a subset, conditional case, proxy, design-level claim, or mixed support sufficient for the recorded judgment. |
| Absent-explicit | The source explicitly reports failure, absence, or non-existence of the relation. |
| Not reported | The relation is applicable, but the source does not provide enough information. |
| Not applicable | The relation is structurally outside the record's scope. |
| Indeterminate | Evidence conflicts or available material cannot support a defensible distinction. |

Silence is Not reported, not Absent-explicit. Evidence status is not a global quality score.

### 17.3 Partial qualifiers

Use subset, conditional, proxy, design_only, mixed, or unknown. The qualifier describes the reason for partial coverage. It does not downgrade a clearly established HPAT linkage into Indeterminate.

### 17.4 Evidence artifact fields

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

### 17.5 Claim-support ceiling

For operation, effect, state, and postcondition claims:

| Level | Evidence object | Highest supported claim |
|---|---|---|
| E0 | Author narrative or scenario description | Intended or claimed setup |
| E1 | Model output, plan, refusal, or proposed action | Proposal or decision |
| E2 | Action trace, click, command, or tool call | Issued or attempted operation |
| E3 | Runtime return, success flag, or execution trace | Runtime acceptance or completion |
| E4 | Post-operation observation | Observed effect or state in the reported environment |
| E5 | Deterministic oracle or independent confirmation | Specified postcondition within the checked scope |

The ceiling limits claims; it does not convert a low-level artifact into a negative finding.

## 18. Conditional modules

Add a module only when its trigger is present. If applicable but unreported, retain the module decision as Not reported.

| Module | Trigger | Required fields |
|---|---|---|
| Delegation | A principal grants or transfers a task, authority, or capability | delegator, original task, delegated subtask, authority scope, constraints, context preservation, depth, linkage |
| Attribute or usage control | The source uses subject, object, action, environment, purpose, or ongoing obligations | attributes, policy version, lifetime, quota, attenuation, revocation |
| Persistent state | Effect or influence remains relevant across steps, tasks, sessions, or actors | state origin, creating HPAT, horizon, pre-state, post-state |
| Reuse | Stored or transmitted material later re-enters context or decision | reuse description, later transition link |
| Propagation | Influence or effect crosses tool, resource, agent, user, environment, or shared-state boundary | edge, source, target, crossing condition |
| Amplification | A baseline and an increase in scope, frequency, intensity, or consequence are established | baseline, measure, description |
| Experimental condition | Multiple models, runtimes, baselines, or controls are compared | variants, environment, run count, source-native result |

## 19. Splitting, merging, and aggregation

### 19.1 Split conditions

Split candidates or HPATs when any of the following changes:

- acting principal, actor, delegation context, or authorization basis;
- privilege basis, permission or resource scope, or protected target;
- operation target or recipient when effect or authorization differs;
- effect or resulting-state verification object;
- control, containment, or recovery target;
- source-native operation row or independent postcondition oracle.

When separately reported, split memory write and later retrieval, delegation grant and downstream action, initial effect and later propagation, harmful operation and recovery, different recipients requiring different authorization, and independently checked benchmark operations.

### 19.2 Merge conditions

Multiple clicks or low-level calls may remain one HPAT when they are inseparable steps of one source-native operation with the same principal, privilege basis, target, authorization, effect, and postcondition. Store the low-level calls as evidence artifacts.

Scenario-class merging requires the same principal, delegation context, authorization, technical permission, operation and target class, effect or postcondition, control semantics, and evidence mode. If any differs, split.

### 19.3 Aggregates

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

## 20. Study and corpus aggregation

Study-level derived fields may include highest_established_operation_stage, operation_stage_display, relation-status views, unobserved relations, strongest demonstrated relation, and display symbols for tables or figures. These are generated from decisions and authoritative records.

An aggregate denominator must state whether it counts studies, candidates, qualified HPATs, source rows, scenarios, runs, or another source-native unit. A study counts once or multiple times only under an explicitly declared aggregation rule. Indeterminate candidates are retained but excluded from an Established HPAT denominator.

### 20.1 Analytical populations

The codebook defines two statistical populations with different purposes. They do not constitute two transition frameworks.

**Candidate diagnostic population.** This population contains Candidate Operations for which consequentiality and model mediation are established. It supports only eligibility and reporting audits, including the proportion that passes the independent privilege gate, reasons privilege linkage is not established, candidate-level reporting of authorization or technical permission, and explanations for zero-HPAT studies. Candidate-wide statistics must be explicitly labeled `candidate diagnostic` or `candidate-wide audit`. They must not be presented as HPAT, HPAC, transition-relation, or security-mechanism findings.

**HPAT synthesis population.** This population contains qualified HPAT records with an established independent privilege linkage. It is the primary transition population for HPAC synthesis, full relation coding, Sections 3-5 analytical claims, HPAC chain relations, Control records, and HPAT relation projections.

The default population for any unlabeled transition-level synthesis is the HPAT synthesis population. A candidate diagnostic result and an HPAT synthesis result may be compared only when both denominators and purposes are stated. Candidate Operations are eligibility objects; HPATs are the atomic transition units used for HPAC synthesis.

### 20.2 Display projection

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

## 21. Coding workflow and reliability

### Pass 0: freeze inputs

Freeze the canonical source list, stable source locators, study IDs, and codebook version before coding.

### Pass 1: blind candidate discovery

Read each source and enumerate candidate operations using source-native units. Do not consult a prior eligibility label while discovering candidates. Record source unit, atomicity, operation, target, condition, and locator.

### Pass 2: eligibility gates

Apply Q1-Q5. Record model-mediation evidence and privilege basis separately. Preserve Not established and Indeterminate candidates in the ledger.

### Pass 3: candidate audit and HPAT relation coding

For every candidate with `consequentiality_status=consequential` and `model_mediation_status=established`, complete the candidate-level audit Decisions in Section 9. These Decisions preserve whether the source reports privilege basis, authorization, technical permission, operation, execution, effect, state, attribution, containment, or recovery. They do not create a transition or full relation record.

For `hpat_eligibility=Established`, create an HPAT record and perform full relation coding under Sections 10-16. For `Not established` and `Indeterminate` candidates, retain the Candidate Operation and audit Decisions without creating an HPAT, Cross-transition Relation, or Control record. This distinction is mandatory for every corpus aggregation.

### Pass 4: study aggregation

Compute candidate diagnostic statistics separately from HPAT synthesis statistics. Full relation projections and derived HPAC displays use the HPAT population. Every projection must declare its population, relation-specific applicability denominator, treatment of `Not reported`, `Absent-explicit`, and `Indeterminate`, and partial-qualifier composition. Preserve applicable versus not-applicable distinctions.

### Pass 5: second coder and adjudication

The second coder receives the same frozen source package and blank templates without the first coder's labels. The reliability target size is `ceil(0.20 * N_final_corpus)`, drawn without replacement from the complete final corpus after excluding any pre-specified calibration set. Freeze the population list, random seed, selection script or procedure, stratum assignment, and selected study IDs before the second coder begins. Use the first coder's completed study-scope labels only to stratify the draw; do not disclose those labels to the second coder. Include at least one study from every non-empty zero-HPAT, one-or-more-HPAT, aggregate-only, and indeterminate stratum, then allocate the remaining sample proportionally. Do not sample only HPAT-positive studies.

Reliability has two distinct layers:

1. Unitization reliability: candidate discovery and split-merge decisions.
2. Classification reliability: model mediation, privilege eligibility, and candidate-audit evidence status on matched Candidate Operations; applicability, evidence status, and selected relation fields only on candidates independently classified as HPATs by both coders.

Candidate matching key is `study_id + source_extraction_unit_id + normalized operation description + target/resource/recipient + scenario_or_condition`. Matching begins automatically on source unit and study, then is reviewed manually whenever operations are split, merged, or only partially overlap. An unmatched candidate is a unitization disagreement and is never forced into a categorical agreement calculation.

Report unitization reliability as the matched-candidate Dice/F1 coefficient `2M / (A + B)`, where `M` is the number of adjudicated one-to-one candidate matches and `A` and `B` are the candidate counts produced independently by the two coders. Also report `A`, `B`, `M`, unmatched counts by coder, and every split, merge, or partial-overlap pattern. Do not report Cohen's kappa for unmatched candidate discovery.

For matched categorical fields, report raw agreement and Cohen's kappa. For sparse or strongly imbalanced fields, including containment and recovery, also report Gwet's AC1 with the prevalence distribution. The prespecified fields, matching rule, sample selection, and metric set may not be changed after inspecting the results.

If the coders disagree on HPAT eligibility, record that disagreement in the eligibility analysis and do not force the candidate into the HPAT relation-agreement denominator. Report the number of matched candidates classified as HPAT by both coders and use that double-qualified set as the denominator for relation-field reliability. Adjudicated HPAT labels may determine the final corpus record, but they must not be substituted for either coder's blind label in reliability calculations.

Log both labels, unmatched candidate mappings, field-specific disagreement reasons, the adjudicated value, adjudicator identity, and the rule applied. A copied first-coder label is not an independent pass.

## 22. Boundary examples

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

## 23. Worked boundary examples

### 23.1 Zero-HPAT candidate

~~~
operation_description: Transfer funds
source_unit_type: scenario_walkthrough
consequentiality_status: consequential
model_mediation_status: established
hpat_eligibility: Not established
privilege_basis_type: none_established
privilege_evidence_status: Not reported
decision_reason: The source describes a consequential tool call but does not connect it to an account, credential, authenticated session, protected resource, or principal-bound capability.
~~~

The candidate remains in the audit ledger and does not enter the HPAT denominator.

### 23.2 Qualified HPAT with partial evidence

~~~
operation_description: Read private email folder
source_unit_type: task_table_row
source_native_atomicity: single_operation
consequentiality_status: consequential
model_mediation_status: established
hpat_eligibility: Established
privilege_basis_type: configured_capability;resource_scoped_access
privilege_evidence_status: Present-partial
privilege_partial_qualifier: design_only
decision_reason: The source assigns the concrete model task to the CUA and identifies the private email resource and configured access, but does not report per-run permission lifetime or revocation.
~~~

### 23.3 Executed HPAT with verified postcondition

~~~
operation_stage_events: proposed;issued_or_attempted;runtime_accepted;executed_at_mechanism_boundary
execution_disposition: runtime_completed
effect_outcome: occurred
resulting_state_description: independently confirmed postcondition in the controlled environment
claim_support_ceiling: E5
~~~

A verified effect does not retroactively establish authorization, technical permission scope, containment, or recovery.

## 25. Public artifact requirements

Subject to safety review, the public coding projection contains the formal codebook, study and candidate records, qualified HPAT records, source-linked evidence, transition-field decisions, control records, cross-transition relations, a validation script, and a deterministic manifest. It excludes source PDFs and non-public safety-sensitive material.

The README describes the released record scope, evidence limits, and validation command. It does not claim to reproduce a source judgment beyond the evidence and decision records that are released.

## 26. Validation checklist

Before a coding release is complete, verify:

- every included study has a stable public source URL or a documented availability status;
- candidate discovery is exhaustive within the stated source units;
- every candidate has consequentiality, model-mediation, and privilege decisions;
- every model-mediated consequential candidate has the required candidate-level audit Decisions;
- every Established HPAT has model-mediation evidence and operation-to-capability evidence;
- no Indeterminate candidate enters the HPAT denominator;
- no non-HPAT candidate is represented as a transition, HPAC chain endpoint, or HPAC Control record;
- every candidate-wide result is labeled as diagnostic or audit and is not presented as an HPAT finding;
- every full relation projection, HPAC chain analysis, and HPAT finding uses the qualified HPAT population unless an explicitly labeled comparison states otherwise;
- every positive relation has an evidence artifact, locator, and coverage qualifier;
- Present-partial has a partial qualifier or adjudication note;
- runtime completion is not used as effect or state evidence;
- external effect is not used as resulting-state evidence without a state observation;
- controls, attribution, containment, and recovery are not inferred from one another;
- aggregate numerators and denominators retain source-native units;
- derived tables and figures are generated from records rather than hand-edited;
- coder identity and codebook version are recorded where the public schema carries them;
- manifest hashes and validation outputs are deterministic under a frozen release date.

## 27. Freeze statement

This document is the formal v3.1.2 coding contract for HPAC/HPAT. Candidate Operations are eligibility objects; HPATs are the sole atomic transition units used for HPAC synthesis. No new eligibility category, privilege basis, source-unit type, transition layer, partial qualifier, applicability rule, matching rule, population purpose, or relation meaning may be introduced during coding without a versioned amendment and re-adjudication of affected records. Wording clarifications that do not change a decision boundary may be recorded as editorial changes. All substantive changes require a new codebook version.
