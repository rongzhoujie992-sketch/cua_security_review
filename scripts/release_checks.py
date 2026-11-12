"""Deterministic rules shared by release generation and validation."""
from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

GATES = {"Established", "Not established", "Indeterminate"}
GATE_FIELDS = ("q2_consequentiality", "q3_model_mediation", "q4_privilege_basis", "q5_operation_capability_link")
RELATIONS = ("Influence", "Authorization", "Technical Permission", "Operation Execution", "External Effect", "Resulting State", "Technical Attribution", "Containment", "Recovery")
STATUSES = {"Present-direct", "Present-partial", "Not reported", "Indeterminate", "Not applicable", "Absent-explicit"}
MAIN = "original_226"
SUPPLEMENT = "post_cutoff_34"


def read_csv(root: Path, relative: str) -> list[dict[str, str]]:
    with (root / relative).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def public_source_url_valid(value: str) -> bool:
    """Recognize DOI, arXiv and official publication pages used by this release."""
    if not value or any(character.isspace() for character in value):
        return False
    try:
        link = urlsplit(value)
        if (link.scheme not in {"https", "http"} or link.username or link.password
                or link.port or link.query or link.fragment):
            return False
    except ValueError:
        return False
    patterns = {
        "arxiv.org": r"/abs/\d{4}\.\d{4,5}(?:v[1-9]\d*)?",
        "doi.org": r"/10\.\d{4,9}/\S+",
        "www.usenix.org": r"/conference/[^/]+/presentation/[^/]+/?",
        "conf.researchr.org": r"/details/[^/]+/[^/]+/\d+/[^/]+/?",
    }
    pattern = patterns.get(link.hostname)
    return bool(pattern and re.fullmatch(pattern, link.path))


def derive_eligibility(values: list[str]) -> str:
    if len(values) != 4 or any(value not in GATES for value in values):
        raise ValueError(f"Eligibility requires four valid gates: {values!r}")
    if "Not established" in values:
        return "Not established"
    return "Established" if all(value == "Established" for value in values) else "Indeterminate"


def agreement_stats(first: list[str], second: list[str]) -> dict:
    if len(first) != len(second):
        raise ValueError("Unaligned comparison values")
    pairs = [(a, b) for a, b in zip(first, second) if a and b]
    n = len(pairs)
    a, b = Counter(x for x, _ in pairs), Counter(y for _, y in pairs)
    agreements = sum(x == y for x, y in pairs)
    expected_numerator = sum(count * b[label] for label, count in a.items())
    result = {
        "denominator": n, "agreements": agreements,
        "agreement_rate": agreements / n if n else None,
        "cohens_kappa": (agreements * n - expected_numerator) / (n * n - expected_numerator)
        if n and expected_numerator != n * n else None,
        "first_distribution": dict(a), "second_distribution": dict(b),
    }
    if not n or expected_numerator == n * n:
        result["kappa_not_estimable_reason"] = "no paired nonmissing observations" if not n else "identical single-category marginals; expected agreement equals one"
    return result


def independent_summary(root: Path, population: str = MAIN) -> dict:
    def select(name: str) -> list[dict[str, str]]:
        return [r for r in read_csv(root, f"reliability/{name}.csv")
                if r.get("coding_population", MAIN) == population]

    q_rows = select("q1_q5_comparison")
    e_rows = select("eligibility_comparison")
    result = {"comparison_scope": "strict_one_to_one_only", "coding_population": population,
              "candidate_pair_denominator": len(q_rows), "q1_q5": {}, "eligibility": {}, "relations": {}}
    for i in range(1, 6):
        result["q1_q5"][f"q{i}"] = agreement_stats([r[f"first_q{i}"] for r in q_rows], [r[f"second_q{i}"] for r in q_rows])
    result["eligibility"] = agreement_stats([r["first_eligibility"] for r in e_rows], [r["second_eligibility"] for r in e_rows])
    result["eligibility_derivation"] = {
        "rule": "v3.3.0 section 3: all Q2-Q5 Established; any Not established fails; otherwise Indeterminate",
        "input": "unchanged pre-adjudication Q2-Q5; raw reported values remain in the comparison table and are not summarized",
        "first_corrected_rows": sum(r.get("first_eligibility_reported", r["first_eligibility"]) != r["first_eligibility"] for r in e_rows),
        "second_corrected_rows": sum(r.get("second_eligibility_reported", r["second_eligibility"]) != r["second_eligibility"] for r in e_rows),
    }
    for name in RELATIONS:
        all_rows = [r for r in select("relation_comparison") if r["relation_name"] == name]
        comparable = [r for r in all_rows if r["comparable_for_relation_reliability"] == "yes"]
        values = agreement_stats([r["first_evidence_status"] for r in comparable], [r["second_evidence_status"] for r in comparable])
        values["all_strict_pair_relation_rows"] = len(all_rows)
        values["comparable_denominator_both_relation_records"] = values.pop("denominator")
        values["missing_first_relation_records"] = sum(r["first_relation_record_present"] != "yes" for r in all_rows)
        values["missing_second_relation_records"] = sum(r["second_relation_record_present"] != "yes" for r in all_rows)
        result["relations"][name] = values
    matching = [r for r in read_csv(root, "provenance/matching_inventory.csv") if r.get("coding_population", MAIN) == population]
    result["matching_inventory_total_groups"] = len(matching)
    result["matching_inventory_match_types"] = dict(Counter(r["match_type"] for r in matching))
    return result


def material_checks(root: Path) -> dict[str, bool]:
    candidates = read_csv(root, "data/final_candidate_ledger.csv")
    eligibility = read_csv(root, "data/final_eligibility_ledger.csv")
    hpats = read_csv(root, "data/final_hpat_ledger.csv")
    artifacts = read_csv(root, "data/evidence_artifacts.csv")
    relations = read_csv(root, "data/final_relation_ledger.csv")
    adjudications = read_csv(root, "provenance/adjudication_ledger.csv")
    matching = read_csv(root, "provenance/matching_inventory.csv")
    c_by_id = {r["final_candidate_id"]: r for r in candidates}
    e_by_id = {r["final_candidate_id"]: r for r in eligibility}
    h_by_id = {r["hpat_id"]: r for r in hpats}
    candidate_adjudications = {r["final_candidate_id"]: r for r in adjudications if r["record_type"] == "candidate"}
    relation_adjudications = {(r["hpat_id"], r["relation_name"]): r for r in adjudications if r["record_type"] == "relation"}
    group_ids = {r["matching_group_id"] for r in matching}

    def valid_derivation(row: dict, field: str) -> bool:
        return row["q1_concrete_operation"] != "Established" or row[field] == derive_eligibility([row[f] for f in GATE_FIELDS])

    q_rows = read_csv(root, "reliability/q1_q5_comparison.csv")
    q_by_id = {(r.get("coding_population", MAIN), r["matching_group_id"]): r for r in q_rows}
    e_rows = read_csv(root, "reliability/eligibility_comparison.csv")
    independent_ok = True
    for row in e_rows:
        q = q_by_id[(row.get("coding_population", MAIN), row["matching_group_id"])]
        for coder in ("first", "second"):
            independent_ok &= row[f"{coder}_eligibility"] == derive_eligibility([q[f"{coder}_q{i}"] for i in range(2, 6)])
    result = {
        "candidate_gate_derivation_correct": all(valid_derivation(r, "final_eligibility") for r in candidates),
        "eligibility_gate_derivation_correct": all(valid_derivation(r, "hpat_eligibility") for r in eligibility),
        "candidate_and_eligibility_values_aligned": all(
            k in e_by_id and all(r[f] == e_by_id[k][f] for f in ("q1_concrete_operation",) + GATE_FIELDS)
            and r["final_eligibility"] == e_by_id[k]["hpat_eligibility"] for k, r in c_by_id.items()),
        "qualified_candidates_projected_exactly": {r["final_candidate_id"] for r in candidates if r["final_eligibility"] == "Established"} == {r["candidate_operation_id"] for r in hpats},
        "artifact_candidate_keys_resolve": all(r["candidate_operation_id"] in c_by_id for r in artifacts),
        "artifact_candidate_hpat_study_aligned": all(r["hpat_id"] in h_by_id and r["candidate_operation_id"] == h_by_id[r["hpat_id"]]["candidate_operation_id"] and r["study_id"] == h_by_id[r["hpat_id"]]["study_id"] for r in artifacts),
        "artifact_scope_complete": all(r["scope_and_condition"].strip() for r in artifacts),
        "matching_covers_all_final_groups": all(r["canonical_group_id"] in group_ids for r in candidates),
        "adjudication_covers_all_final_candidates": set(c_by_id) <= set(candidate_adjudications),
        "adjudication_covers_all_final_relations": {(r["hpat_id"], r["relation_name"]) for r in relations} <= set(relation_adjudications),
        "candidate_adjudication_values_aligned": all(
            r["final_candidate_id"] in candidate_adjudications and all(
                r[field] == candidate_adjudications[r["final_candidate_id"]][f"q{i}_final"]
                for i, field in enumerate(("q1_concrete_operation",) + GATE_FIELDS, 1))
            and r["final_eligibility"] == candidate_adjudications[r["final_candidate_id"]]["final_eligibility"] for r in candidates),
        "relation_adjudication_values_aligned": all(relation_adjudications.get((r["hpat_id"], r["relation_name"]), {}).get("adjudicated_relation_status") == r["evidence_status"] for r in relations),
        "relation_statuses_legal": all(r["evidence_status"] in STATUSES for r in relations),
        "claim_support_ceiling_legal": all(r["claim_support_ceiling"] in {f"E{i}" for i in range(6)} for r in relations),
        "independent_eligibility_derivation_correct": independent_ok,
        "q1_failed_rows_marked_as_source_unit_audit": all(r["canonical_unit_role"] == "source_unit_reviewed_no_candidate" and not r["hpat_id"] for r in candidates if r["q1_concrete_operation"] != "Established"),
    }
    stored_summary = json.loads((root / "reliability/reliability_summary.json").read_text(encoding="utf-8"))
    current_summary = independent_summary(root)
    result["independent_reliability_recomputed"] = (
        "eligibility_as_reported" not in stored_summary
        and all(stored_summary.get(key) == value for key, value in current_summary.items())
    )
    result["supplementary_gate_decisions_preserved"] = all(
        row.get("adjudicated_value") == row.get(f"q{row.get('target_field', ' ')[1:2]}_final")
        for row in adjudications if row["record_type"] == "candidate_gate")
    return result


def schema_review_counts(root: Path) -> dict[str, int]:
    """Report remaining source-dependent schema work separately from core integrity."""
    modes = {"author_narrative", "static_artifact_analysis", "projected_or_simulated_execution", "runtime_trace_or_return", "post_operation_observation", "deterministic_checker_or_independent_confirmation"}
    qualifiers = {"subset", "conditional", "proxy", "design_only", "mixed", "unknown"}
    bases = {"authenticated_session", "identity_bound_account", "credential_or_secret", "technical_role_or_permission", "resource_scoped_access", "delegated_capability", "configured_capability", "principal_bound_service", "policy_governed_state", "other_access_basis", "none_established", "indeterminate_basis"}
    reasons = {"core_predicate_not_established", "core_predicate_established_at_aligned_unit", "applicability_prerequisite_absent", "applicable_but_not_reported", "conflicting_or_unresolved_source_evidence", "aggregate_aligned_to_scenario_class", "aggregate_not_aligned_to_concrete_instance", "controlled_setting_direct_with_scope_limit", "adjacent_relation_not_transferable", "cross_scenario_evidence_not_transferable", "both_coder_inputs_rejected"}
    hpats = read_csv(root, "data/final_hpat_ledger.csv")
    relations = read_csv(root, "data/final_relation_ledger.csv")
    return {
        "hpat_privilege_evidence_status_outside_evidence_enum": sum(r["privilege_evidence_status"] not in STATUSES for r in hpats),
        "hpat_privilege_basis_type_outside_controlled_list": sum(not r["privilege_basis_type"] or not set(r["privilege_basis_type"].split(";")) <= bases for r in hpats),
        "artifact_observation_mode_requires_source_review": sum(r["observation_mode"] not in modes for r in read_csv(root, "data/evidence_artifacts.csv")),
        "partial_relation_qualifier_requires_structured_encoding": sum(r["evidence_status"] == "Present-partial" and r["final_coverage_qualifier"] not in qualifiers for r in relations),
        "relation_disagreement_reason_requires_controlled_class": sum(bool(r["first_evidence_status"] and r["second_evidence_status"]) and r["first_evidence_status"] != r["second_evidence_status"] and not set(r["adjudication_reason_class"].split(";")) & reasons for r in relations),
    }


def release_report(
    root: Path,
    *,
    source_route: list[dict[str, str]] | None = None,
    source_accounting: list[dict[str, str]] | None = None,
) -> dict:
    candidates = read_csv(root, "data/final_candidate_ledger.csv")
    eligibility = read_csv(root, "data/final_eligibility_ledger.csv")
    hpats = read_csv(root, "data/final_hpat_ledger.csv")
    relations = read_csv(root, "data/final_relation_ledger.csv")
    artifacts = read_csv(root, "data/evidence_artifacts.csv")
    route = source_route if source_route is not None else read_csv(root, "integration/supplementary_evidence_route.csv")
    alignment = read_csv(root, "integration/corpus_alignment.csv")
    main = read_csv(root, "prisma/fulltext/final_included_studies_222.csv")
    foundations = read_csv(root, "prisma/foundational_branch/foundational_sources_12.csv")
    tdes = read_csv(root, "prisma/tdes_branch/selected_sources_9.csv")
    c_ids = [r["final_candidate_id"] for r in candidates]
    e_ids = [r["final_candidate_id"] for r in eligibility]
    h_ids = [r["hpat_id"] for r in hpats]
    a_ids = [r["evidence_artifact_id"] for r in artifacts]
    a_by_id = {r["evidence_artifact_id"]: r for r in artifacts}
    relation_keys = [(r["hpat_id"], r["relation_name"]) for r in relations]
    route_counts = Counter(r["source_type"] for r in route)
    post_cutoff = [row for row in route if row["source_type"] == "post_cutoff_study"]
    source_keys = [row.get("coding_study_id", "") for row in alignment + post_cutoff]
    source_key_counts = Counter(source_keys)
    source_urls = [row.get("coding_source_url", "") for row in alignment] + [row.get("source_url", "") for row in post_cutoff]
    refs_resolve, positive_closed = True, True
    for row in relations:
        refs = [value.strip() for value in re.split(r"[;|]", row["evidence_artifacts"]) if value.strip()]
        refs_resolve &= all(ref in a_by_id for ref in refs)
        if row["evidence_status"] in {"Present-direct", "Present-partial"}:
            positive_closed &= bool(refs) and all(ref in a_by_id and all(a_by_id[ref][field] == row[source] for field, source in (("hpat_id", "hpat_id"), ("study_id", "study_id"), ("field_name", "relation_name"), ("evidence_status", "evidence_status"))) for ref in refs)
    checks = {
        "candidate_ids_unique": len(c_ids) == len(set(c_ids)),
        "eligibility_ids_unique_and_aligned": len(e_ids) == len(set(e_ids)) and set(e_ids) == set(c_ids),
        "hpat_ids_unique": len(h_ids) == len(set(h_ids)),
        "artifact_ids_unique": len(a_ids) == len(set(a_ids)),
        "hpat_candidate_ids_resolve": {r["candidate_operation_id"] for r in hpats} <= set(c_ids),
        "supplementary_hpat_candidate_keys_resolve": all(r["candidate_operation_id"] in c_ids and r["canonical_group_id"] == r["candidate_operation_id"] for r in hpats if r["hpat_id"].startswith("HPAT-SUP-")),
        "supplementary_hpat_operation_provenance_present": all(r["adjudicated_operation_id"] and r["source_candidate_operation_ids"] for r in hpats if r["hpat_id"].startswith("HPAT-SUP-")),
        "relation_keys_unique": len(relation_keys) == len(set(relation_keys)),
        "nine_relations_per_hpat": set(r["hpat_id"] for r in relations) == set(h_ids) and all(Counter(r["relation_name"] for r in relations if r["hpat_id"] == key) == Counter(RELATIONS) for key in h_ids),
        "positive_relation_artifacts_closed": bool(positive_closed),
        "all_artifact_relation_references_resolve": bool(refs_resolve),
        "candidate_locator_reason_complete": all(r["source_locator"] and r["disposition_rationale"] for r in candidates),
        "eligibility_locator_complete": all(r["source_locator"] for r in eligibility),
        "relation_locator_reason_complete": all(r["source_locator"] and r["decision_reason"] for r in relations),
        "artifact_locator_excerpt_complete": all(r["source_locator"] and r["faithful_excerpt_or_paraphrase"] for r in artifacts),
        "supplementary_route_rows": len(route) == 55 and route_counts == {"foundational_classical": 12, "tdes_academic": 4, "tdes_official": 5, "post_cutoff_study": 34},
        "no_local_filesystem_paths": not any(marker in value for rows in (candidates, eligibility, hpats, relations, artifacts, route) for row in rows for value in row.values() for marker in ("Users\\", "中国科学院")),
        "all_hpat_relation_targets_exist": {r["hpat_id"] for r in relations} <= set(h_ids),
        "coding_source_mapping_keys_unique": all(key.strip() for key in source_keys) and len(source_keys) == len(source_key_counts),
        "ledger_study_ids_resolve_to_source": all(source_key_counts[row["study_id"]] == 1 for rows in (candidates, eligibility, hpats, relations, artifacts) for row in rows),
        "coding_source_urls_present": all(url.startswith(("https://", "http://")) and url.strip() == url for url in source_urls),
    }
    checks.update(material_checks(root))
    checks["post_cutoff_source_urls_present"] = all(row.get("source_url", "").startswith(("https://", "http://")) for row in route if row["source_type"] == "post_cutoff_study")
    checks["post_cutoff_public_source_identities_valid"] = all(
        row["title"].strip() and public_source_url_valid(row.get("source_url", ""))
        for row in route if row["source_type"] == "post_cutoff_study"
    )
    checks["prisma_component_additive_accounting_correct"] = (
        len(main) == 222 and len(foundations) == 12 and len(tdes) == 9
    )
    unified_accounting = source_accounting if source_accounting is not None else read_csv(root, "prisma/reports/integrated_source_accounting_277.csv")
    total_component = "Final unique evidence/source base"
    study_components = {"Final main CUA corpus", "Post-cutoff supplementary studies"}
    expected_accounting = {
        "Final main CUA corpus": len(main),
        "Foundational/classical security branch": len(foundations),
        "TDES supplementary sources": len(tdes),
        "Post-cutoff supplementary studies": route_counts["post_cutoff_study"],
        total_component: len(main) + len(foundations) + len(tdes) + route_counts["post_cutoff_study"],
    }
    checks["unified_source_accounting_correct"] = (
        len(unified_accounting) == len(expected_accounting)
        and {r["component"]: int(r["count"]) for r in unified_accounting} == expected_accounting
        and all(r["unit"] == ("study" if r["component"] in study_components else "source")
                and r["additive_to_unique_source_base"] == ("TOTAL" if r["component"] == total_component else "YES")
                for r in unified_accounting)
    )
    counts = {
        "studies": len(alignment) + route_counts["post_cutoff_study"],
        "prisma_main_corpus_studies": len(main), "supplementary_tdes_sources": len(tdes),
        "supplementary_foundational_sources": len(foundations), "supplementary_post_cutoff_studies": route_counts["post_cutoff_study"],
        "evidence_source_base": len(main) + len(foundations) + len(tdes) + route_counts["post_cutoff_study"],
        "candidates": len(candidates), "eligibility_rows": len(eligibility), "hpats": len(hpats),
        "qualified_hpat_studies": len({r["study_id"] for r in hpats}), "relations": len(relations),
        "expected_relations": len(hpats) * len(RELATIONS), "evidence_artifacts": len(artifacts),
        "q1_established_candidate_operations": sum(r["q1_concrete_operation"] == "Established" for r in candidates),
        "source_unit_audit_rows": sum(r["q1_concrete_operation"] != "Established" for r in candidates),
        "matching_groups": len(read_csv(root, "provenance/matching_inventory.csv")),
        "adjudication_records": len(read_csv(root, "provenance/adjudication_ledger.csv")),
    }
    schema_review = schema_review_counts(root)
    return {
        "codebook_version": "3.3.0",
        "counts": counts, "checks": checks,
        "source_dependent_schema_review": schema_review,
        "coding_population": {"main_226_study_release": len(alignment), "post_cutoff_added": route_counts["post_cutoff_study"], "unified": counts["studies"]},
        "reliability_boundary": {"main_release": "568 original-corpus strict semantic one-to-one pairs; eligibility derived from unchanged independent gates, reported values retained.", "post_cutoff": "67 supplementary strict semantic one-to-one pairs; not pooled with original-corpus pairs. Supplementary relations are an adjudicated population, not ordinary independent relation reliability."},
        "source_route": {"foundational_classical": len(foundations), "tdes": len(tdes), "post_cutoff": route_counts["post_cutoff_study"], "total_supplementary": len(route), "overall_evidence_source_base": counts["evidence_source_base"]},
        "errors": [name for name, passed in checks.items() if not passed],
    }
