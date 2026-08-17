# Eligibility criteria — title/abstract stage

**Literature cutoff:** 2026-07-31 inclusive.

The review concerns computer-use-agent (CUA) security and tightly bounded adjacent mechanisms.

## Retain for report-level assessment

A record is retained when title/abstract metadata establishes at least one of the following evidence roles:

1. **Direct CUA security evidence.** Security, safety, privacy, authorization, threat, evaluation, safeguard, containment, recovery, or governance evidence in computer-use, GUI, OS, Web, browser, desktop, or mobile-agent settings.
2. **Necessary CUA foundation.** A broad environment, benchmark, survey, platform, or system contribution needed to define the computer-use setting, action space, evaluation environment, or operational boundary. Narrow capability benchmarks and incremental method papers do not qualify merely because they use a GUI/Web/mobile agent.
3. **Adjacent executable-use security mechanism.** Tool/function/API/skill invocation, MCP, persistent memory, inter-agent communication/delegation, authorization/permission, information flow, provenance, runtime control, or related mechanisms when the reported security relation is explicit and can directly bear on executable computer use.
4. **Transferable attack/evaluation/control evidence.** Prompt injection or broader agent-security work only when the executable agent/tool/application relation and the security evidence contribution are sufficiently specific to support CUA synthesis.

## Exclude at title/abstract stage

Records are excluded when metadata establishes that they are:

- general LLM/model/application security without an executable-agent or CUA mechanism;
- generic agent security/safety without a concrete executable-use relation;
- capability-only CUA training, planning, grounding, navigation, efficiency, or adaptation work without a necessary foundational role;
- narrow application/domain benchmarks that do not define the general CUA setting;
- unrelated robotics, cyber-physical, medical, networking, or other application-domain work;
- nonresearch, position/tutorial/guide material, or records without a sufficiently substantive evidence role.

## Boundary handling

`UNCLEAR` records are retained for report-level assessment. Title-only records are not automatically included; strong title-level candidates without an abstract are routed to `UNCLEAR`.
