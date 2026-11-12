"""Tests for ledger rules, statistics, and metadata publication."""
import builtins
import csv
import json
import io
import runpy
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import build_unified_metadata as metadata
from release_checks import agreement_stats, derive_eligibility, independent_summary, material_checks, read_csv, release_report

ROOT = Path(__file__).resolve().parents[1]


class RuleTests(unittest.TestCase):
    def report_with_table(self, relative, rows):
        def changed_table(root, name):
            return rows if name == relative else read_csv(root, name)

        with patch("release_checks.read_csv", side_effect=changed_table):
            return release_report(ROOT)

    def test_gate_failure_takes_precedence_over_uncertainty(self):
        self.assertEqual(derive_eligibility(["Established", "Established", "Not established", "Indeterminate"]), "Not established")
        self.assertEqual(derive_eligibility(["Established", "Established", "Indeterminate", "Indeterminate"]), "Indeterminate")
        self.assertEqual(derive_eligibility(["Established"] * 4), "Established")

    def test_identical_single_category_kappa_is_undefined(self):
        result = agreement_stats(["Established"] * 3, ["Established"] * 3)
        self.assertEqual(result["agreement_rate"], 1)
        self.assertIsNone(result["cohens_kappa"])

    def test_actual_release_material_invariants(self):
        checks = material_checks(ROOT)
        self.assertEqual([name for name, passed in checks.items() if not passed], [])

    def test_release_report_omits_internal_progress_labels(self):
        report = release_report(ROOT)
        labels = {"semantic_status", "semantic_status_scope", "structural_status", "full_codebook_schema_status"}
        self.assertFalse(labels.intersection(report), "Internal progress labels remain in the report")

    def test_proposed_accounting_is_checked(self):
        accounting = read_csv(ROOT, "prisma/reports/integrated_source_accounting_277.csv")
        accounting[-1]["count"] = "278"
        report = release_report(ROOT, source_accounting=accounting)
        self.assertIn("unified_source_accounting_correct", report["errors"])

    def test_unified_checks_do_not_require_old_component_report(self):
        def current_tables_only(root, relative):
            if relative == "prisma/reports/integrated_source_accounting_243.csv":
                raise FileNotFoundError(relative)
            return read_csv(root, relative)

        with patch("release_checks.read_csv", side_effect=current_tables_only):
            self.assertEqual(release_report(ROOT)["errors"], [])

    def test_published_eligibility_reliability_uses_gate_derived_values(self):
        summary = independent_summary(ROOT)
        self.assertNotIn("eligibility_as_reported", summary)
        self.assertEqual(summary["eligibility"]["denominator"], 568)
        self.assertAlmostEqual(summary["eligibility"]["agreement_rate"], 0.7376760563380281)
        self.assertAlmostEqual(summary["eligibility"]["cohens_kappa"], 0.44947277351703324)

        stored = json.loads((ROOT / "reliability/reliability_summary.json").read_text(encoding="utf-8"))
        self.assertNotIn("eligibility_as_reported", stored)
        self.assertEqual(stored["eligibility"], summary["eligibility"])

        raw_rows = [row for row in read_csv(ROOT, "reliability/eligibility_comparison.csv")
                    if row.get("coding_population", "original_226") == "original_226"]
        self.assertEqual(len(raw_rows), 568)
        self.assertTrue(all("first_eligibility_reported" in row and "second_eligibility_reported" in row for row in raw_rows))

    def test_post_cutoff_links_require_public_publication_identities(self):
        invalid_urls = (
            "source/PA-006.pdf",
            "https://localhost/source/PA-006.pdf",
            "https://arxiv.org/abs/not-an-identifier",
            "https://doi.org/10.1145",
            "https://www.usenix.org/",
        )
        for invalid_url in invalid_urls:
            with self.subTest(source_url=invalid_url):
                route = read_csv(ROOT, "integration/supplementary_evidence_route.csv")
                row = next(row for row in route if row["source_type"] == "post_cutoff_study")
                row["source_url"] = invalid_url
                report = release_report(ROOT, source_route=route)
                self.assertIn("post_cutoff_public_source_identities_valid", report["errors"])

    def test_source_mapping_keys_must_be_unique_and_nonempty(self):
        for relative in ("integration/corpus_alignment.csv", "integration/supplementary_evidence_route.csv"):
            for defect in ("duplicate", "empty"):
                with self.subTest(table=relative, defect=defect):
                    rows = read_csv(ROOT, relative)
                    mapped = [row for row in rows if row.get("source_type", "post_cutoff_study") == "post_cutoff_study"]
                    mapped[0]["coding_study_id"] = mapped[1]["coding_study_id"] if defect == "duplicate" else ""
                    report = self.report_with_table(relative, rows)
                    self.assertIn("coding_source_mapping_keys_unique", report["errors"])

        route = read_csv(ROOT, "integration/supplementary_evidence_route.csv")
        next(row for row in route if row["source_type"] == "post_cutoff_study")["coding_study_id"] = read_csv(ROOT, "integration/corpus_alignment.csv")[0]["coding_study_id"]
        report = self.report_with_table("integration/supplementary_evidence_route.csv", route)
        self.assertIn("coding_source_mapping_keys_unique", report["errors"])

    def test_source_mapping_covers_original_and_supplementary_studies(self):
        alignment = read_csv(ROOT, "integration/corpus_alignment.csv")
        alignment.pop(0)
        report = self.report_with_table("integration/corpus_alignment.csv", alignment)
        self.assertIn("ledger_study_ids_resolve_to_source", report["errors"])

        route = read_csv(ROOT, "integration/supplementary_evidence_route.csv")
        next(row for row in route if row["source_type"] == "post_cutoff_study")["coding_study_id"] = "UNMAPPED-STUDY"
        report = self.report_with_table("integration/supplementary_evidence_route.csv", route)
        self.assertIn("ledger_study_ids_resolve_to_source", report["errors"])

    def test_each_scientific_ledger_requires_a_mapped_study(self):
        for relative in ("data/final_candidate_ledger.csv", "data/final_eligibility_ledger.csv", "data/final_hpat_ledger.csv", "data/final_relation_ledger.csv", "data/evidence_artifacts.csv"):
            with self.subTest(table=relative):
                rows = read_csv(ROOT, relative)
                rows[0]["study_id"] = "UNMAPPED-STUDY"
                report = self.report_with_table(relative, rows)
                self.assertIn("ledger_study_ids_resolve_to_source", report["errors"])

    def test_source_mapping_requires_a_public_url_in_its_source_field(self):
        for relative, field in (("integration/corpus_alignment.csv", "coding_source_url"), ("integration/supplementary_evidence_route.csv", "source_url")):
            with self.subTest(table=relative):
                rows = read_csv(ROOT, relative)
                row = next(row for row in rows if row.get("source_type", "post_cutoff_study") == "post_cutoff_study")
                row[field] = ""
                report = self.report_with_table(relative, rows)
                self.assertIn("coding_source_urls_present", report["errors"])


class ReconstructionTests(unittest.TestCase):
    def run_reconstruction(self, script, altered=None):
        altered_path = None
        altered_text = None
        if altered:
            relative, field, value = altered
            altered_path = (ROOT / relative).resolve()
            rows = read_csv(ROOT, relative)
            rows[0][field] = value
            buffer = io.StringIO()
            writer = csv.DictWriter(buffer, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
            altered_text = buffer.getvalue()

        original_open = builtins.open

        def read_only_open(file, mode="r", *args, **kwargs):
            if any(flag in mode for flag in "wax+"):
                raise AssertionError("Reconstruction must not write files")
            if altered_path and isinstance(file, (str, Path)) and Path(file).resolve() == altered_path:
                return io.StringIO(altered_text)
            return original_open(file, mode, *args, **kwargs)

        with patch("builtins.open", side_effect=read_only_open), \
                patch("io.open", side_effect=read_only_open), \
                redirect_stdout(io.StringIO()):
            runpy.run_path(str(ROOT / script), run_name="__main__")

    def test_occurrence_reconstruction_is_read_only(self):
        self.run_reconstruction("prisma/scripts/build_occurrence_ledger.py")

    def test_dedup_reconstruction_is_read_only(self):
        self.run_reconstruction("prisma/scripts/rebuild_dedup.py")

    def test_occurrence_reconstruction_detects_changed_metadata(self):
        with self.assertRaisesRegex(AssertionError, "Occurrence ledger differs"):
            self.run_reconstruction("prisma/scripts/build_occurrence_ledger.py", (
                "prisma/dedup/global_occurrence_ledger.csv", "title", "Altered source title"))

    def test_dedup_reconstruction_detects_changed_mapping(self):
        with self.assertRaisesRegex(AssertionError, "Occurrence mapping differs"):
            self.run_reconstruction("prisma/scripts/rebuild_dedup.py", (
                "prisma/dedup/occurrence_to_record.csv", "record_id", "REC-invalid"))

    def test_dedup_reconstruction_detects_changed_edge(self):
        with self.assertRaisesRegex(AssertionError, "Dedup edges differ"):
            self.run_reconstruction("prisma/scripts/rebuild_dedup.py", (
                "prisma/dedup/dedup_edges.csv", "dedup_rule", "invalid_rule"))


class MetadataTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        temporary_root = Path(temporary.name).resolve()
        self.repo = temporary_root / "repository"
        self.supplement = temporary_root / "supplement"
        for relative in ("prisma/foundational_branch/foundational_source_ledger.csv", "prisma/tdes_branch/selected_sources_9.csv"):
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / relative, target)
        self.originals = {}
        for relative in ("integration/supplementary_evidence_route.csv", "prisma/reports/integrated_source_accounting_277.csv"):
            target = self.repo / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            original = f"Original contents of {relative}\n".encode()
            target.write_bytes(original)
            self.originals[target] = original

        post = [row for row in read_csv(ROOT, "integration/supplementary_evidence_route.csv") if row["source_type"] == "post_cutoff_study"]
        inputs = {
            "prisma/data/post_cutoff/selected_studies.csv": [
                {"Study_ID": row["coding_study_id"], "Title": row["title"], "Source_URL": row["source_url"]} for row in post],
            "prisma/source_manifest.csv": [
                {"study_id": row["coding_study_id"], "relative_path": row["source_locator"]} for row in post],
        }
        for relative, rows in inputs.items():
            target = self.supplement / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)

    def run_builder(self):
        with patch.object(metadata, "__file__", str(self.repo / "scripts/build_unified_metadata.py")), \
                patch.object(sys, "argv", ["build_unified_metadata.py", str(self.supplement)]), \
                redirect_stdout(io.StringIO()):
            metadata.main()

    def assert_originals_preserved(self):
        for target, original in self.originals.items():
            self.assertEqual(target.read_bytes(), original)
        self.assertEqual(list(self.repo.rglob("*.tmp")), [])

    def test_validation_failure_preserves_both_existing_files(self):
        selected_path = self.supplement / "prisma/data/post_cutoff/selected_studies.csv"
        selected = metadata.read(selected_path)
        selected[0]["Source_URL"] = ""
        metadata.write(selected_path, list(selected[0]), selected)
        with patch("release_checks.release_report", side_effect=lambda root, **rows: release_report(ROOT, **rows)):
            with self.assertRaisesRegex(SystemExit, "post_cutoff_source_urls_present"):
                self.run_builder()
        self.assert_originals_preserved()

    def test_success_validates_proposed_rows_before_publication(self):
        def validate(root, **prospective):
            self.assertEqual(root, self.repo)
            self.assert_originals_preserved()
            self.assertEqual(len(prospective["source_route"]), 55)
            self.assertEqual(len(prospective["source_accounting"]), 5)
            return release_report(ROOT, **prospective)

        with patch("release_checks.release_report", side_effect=validate):
            self.run_builder()
        self.assertEqual(len(read_csv(self.repo, "integration/supplementary_evidence_route.csv")), 55)
        self.assertEqual(read_csv(self.repo, "prisma/reports/integrated_source_accounting_277.csv")[-1]["count"], "277")
        expected = {
            row["coding_study_id"]: (row["source_url"], row["source_locator"])
            for row in read_csv(ROOT, "integration/supplementary_evidence_route.csv")
            if row["source_type"] == "post_cutoff_study"
        }
        actual = {
            row["coding_study_id"]: (row["source_url"], row["source_locator"])
            for row in read_csv(self.repo, "integration/supplementary_evidence_route.csv")
            if row["source_type"] == "post_cutoff_study"
        }
        self.assertEqual(len(actual), 34)
        self.assertEqual(actual, expected)
        self.assertEqual(list(self.repo.rglob("*.tmp")), [])
        self.assertFalse((self.repo / "validation.json").exists())

    def test_internal_web_link_cannot_replace_published_source_urls(self):
        selected_path = self.supplement / "prisma/data/post_cutoff/selected_studies.csv"
        selected = metadata.read(selected_path)
        selected[0]["Source_URL"] = "https://localhost/source/PA-006.pdf"
        metadata.write(selected_path, list(selected[0]), selected)
        with patch("release_checks.release_report", side_effect=lambda root, **rows: release_report(ROOT, **rows)):
            with self.assertRaisesRegex(SystemExit, "post_cutoff_public_source_identities_valid"):
                self.run_builder()
        self.assert_originals_preserved()

    def test_staging_failure_preserves_both_existing_files(self):
        original_write = metadata.write
        attempts = []

        def fail_second_write(path, fields, rows):
            attempts.append(path)
            if len(attempts) == 2:
                raise OSError("injected_staging_failure")
            original_write(path, fields, rows)

        with patch("release_checks.release_report", return_value={"errors": []}), \
                patch.object(metadata, "write", side_effect=fail_second_write):
            with self.assertRaisesRegex(OSError, "injected_staging_failure"):
                self.run_builder()
        self.assert_originals_preserved()

    def test_second_replacement_failure_restores_both_files(self):
        original_replace = Path.replace
        second_target = list(self.originals)[1]

        def fail_second_replace(source, target):
            if Path(target) == second_target:
                raise OSError("injected_replacement_failure")
            return original_replace(source, target)

        with patch("release_checks.release_report", return_value={"errors": []}), \
                patch.object(Path, "replace", new=fail_second_replace):
            with self.assertRaisesRegex(OSError, "injected_replacement_failure"):
                self.run_builder()
        self.assert_originals_preserved()


if __name__ == "__main__":
    unittest.main()
