"""Regression checks for portable resources, Git metadata and instruction contracts."""
from __future__ import annotations

from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from pack_utils import (SKILL_NAME, SKILL_PATH, FULL_ARCHIVE_PREFIX, distribution_files, instruction_errors,
                        local_reference_errors, manifest_errors, template_errors, template_names)


class PackagingTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.root = self.folder / "bundle"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc"))

    def command(self, *args):
        return subprocess.run([sys.executable, *args], cwd=self.root, capture_output=True, timeout=30,
                              env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1"), check=False)

    def validate(self):
        return self.command("scripts/validate_pack.py")

    def assert_valid(self):
        run = self.validate()
        self.assertEqual(run.returncode, 0, run.stdout.decode() + run.stderr.decode())

    def test_pristine_validator(self):
        """P01 | pristine bundle | validator | PASS before Git initialization."""
        self.assert_valid()

    def test_validator_after_git_init(self):
        """P02 | temp bundle and installed Git | git init then validator | PASS with same source hashes."""
        git = shutil.which("git")
        if git is None:
            self.skipTest("Git executable unavailable")
        self.assert_valid()
        run = subprocess.run([git, "init", "-q", str(self.root)], capture_output=True, timeout=15, check=False)
        self.assertEqual(run.returncode, 0, run.stderr.decode(errors="replace"))
        self.assert_valid()

    def test_worktree_git_file(self):
        """P03 | synthetic worktree .git file | validator | metadata ignored without reading target."""
        (self.root / ".git").write_text("gitdir: ../unavailable-metadata/worktrees/test\n", encoding="utf-8")
        self.assert_valid()

    def test_git_metadata_pruned(self):
        """P04 | .git with invalid Markdown bytes | validator | never traverses Git metadata."""
        directory = self.root / ".git" / "objects"
        directory.mkdir(parents=True)
        (directory / "invalid.md").write_bytes(b"\xff\xfe")
        self.assert_valid()

    def test_unlisted_file_detected(self):
        """P05 | pristine bundle | add unexpected.txt | FAIL with new-file evidence."""
        (self.root / "unexpected.txt").write_text("synthetic", encoding="utf-8")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b"new=['unexpected.txt']", run.stdout)

    def test_gitignored_file_still_detected(self):
        """P06 | .gitignore ignores .env | add synthetic .env | manifest still rejects file."""
        (self.root / ".env").write_text("SYNTHETIC=not-a-secret\n", encoding="ascii")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b"new=['.env']", run.stdout)

    def test_changed_file_detected(self):
        """P07 | tracked README | append one byte | FAIL with changed hash evidence."""
        path = self.root / "README.md"
        path.write_bytes(path.read_bytes() + b"\n")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b"changed=['README.md']", run.stdout)

    def test_missing_file_detected(self):
        """P08 | tracked README | move outside bundle | FAIL with missing-file evidence."""
        (self.root / "README.md").rename(self.folder / "held-readme.md")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b"missing=['README.md']", run.stdout)

    def test_template_copies_match_canonical(self):
        """P09 | root canonical templates | compare all ten copies | exact bytes and no missing dependency."""
        self.assertEqual(len(template_names(self.root / SKILL_PATH)), 10)
        self.assertEqual(template_errors(self.root), [])

    def test_template_divergence_detected(self):
        """P10 | standalone template copy | append one byte | validator reports divergence."""
        path = self.root / SKILL_PATH / "assets/templates/RELEASE_GATE.md"
        path.write_bytes(path.read_bytes() + b"\n")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b"Template divergence: RELEASE_GATE.md", run.stdout)

    def test_all_local_references(self):
        """P11 | full bundle and nested skill | inspect all local Markdown references | zero broken links."""
        self.assertEqual(local_reference_errors(self.root), [])
        self.assertEqual(local_reference_errors(self.root / SKILL_PATH), [])

    def test_broken_markdown_link_detected(self):
        """P12 | required reference | add absent Markdown target | precise link failure."""
        path = self.root / SKILL_PATH / "references/00-task-contract.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[missing](../assets/templates/MISSING.md)\n", encoding="utf-8")
        self.assertTrue(any("MISSING.md" in error for error in local_reference_errors(self.root)))

    def test_outside_package_reference_rejected(self):
        """P13 | existing external fixture | link outside package | reject without importing external content."""
        (self.folder / "outside.md").write_text("synthetic", encoding="utf-8")
        (self.root / "README.md").write_text("[outside](../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("outside.md" in error for error in local_reference_errors(self.root)))

    def test_standalone_copy_and_cli(self):
        """P14 | copy only skill into isolated location | validate resources and run CLI | independent success."""
        installed = self.folder / "installed" / SKILL_NAME
        shutil.copytree(self.root / SKILL_PATH, installed)
        self.assertEqual(local_reference_errors(installed), [])
        self.assertEqual(manifest_errors(installed), [])
        for name in template_names(installed):
            self.assertEqual((installed / "assets/templates" / name).read_bytes(), (self.root / "templates" / name).read_bytes())
        index = self.folder / "index.json"
        index.write_text('[{"name":"parser"}]', encoding="utf-8")
        run = subprocess.run([sys.executable, str(installed / "scripts/reuse_catalog.py"), "--index", str(index), "search", "parser"],
                             cwd=installed, capture_output=True, timeout=10, check=False)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout)[0]["name"], "parser")

    def test_instruction_contract_and_not_run(self):
        """P15 | core/task/integrations/adaptive/A01-A44 | static consistency check | consistent contract and all models NOT_RUN."""
        self.assertEqual(instruction_errors(self.root), [])

    def test_instruction_conflict_detected(self):
        """P16 | valid Gemma adapter | reintroduce old command prohibition | static check rejects conflict."""
        path = self.root / "integrations/adaptive/gemma4-system-prompt.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nkhông tạo/sửa file, chạy lệnh hay hành động thay đổi state\n", encoding="utf-8")
        self.assertTrue(any("prohibition conflict" in error for error in instruction_errors(self.root)))

    def test_prepare_syncs_canonical(self):
        """P17 | edited canonical fixture | --prepare | byte-identical copy and refreshed valid manifests."""
        path = self.root / "templates/RELEASE_GATE.md"
        path.write_bytes(path.read_bytes() + b"\n")
        run = self.command("scripts/build_release.py", "--prepare")
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(template_errors(self.root), [])
        self.assert_valid()

    def test_build_zip_integrity(self):
        """P18 | validated bundle | build two archives outside root | CRC, matching skill and zero local link errors."""
        target = self.folder / "archives"
        run = self.command("scripts/build_release.py", "--output-dir", str(target))
        self.assertEqual(run.returncode, 0, run.stdout.decode() + run.stderr.decode())
        extracted = self.folder / "extracted"
        for path in target.glob("*.zip"):
            with ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                self.assertFalse(any(".git" in Path(n).parts or "__pycache__" in Path(n).parts for n in archive.namelist()))
                archive.extractall(extracted)
        full, skill = extracted / FULL_ARCHIVE_PREFIX, extracted / SKILL_NAME
        self.assertEqual(manifest_errors(full), [])
        self.assertEqual(manifest_errors(skill), [])
        self.assertEqual(local_reference_errors(full), [])
        self.assertEqual(local_reference_errors(skill), [])
        for path in distribution_files(skill):
            self.assertEqual(path.read_bytes(), (full / SKILL_PATH / path.relative_to(skill)).read_bytes())

    def test_builder_refuses_invalid_source(self):
        """P19 | modified unprepared source | build archives | nonzero and no ZIP produced."""
        (self.root / "unexpected.txt").write_text("synthetic", encoding="utf-8")
        target = self.folder / "archives"
        run = self.command("scripts/build_release.py", "--output-dir", str(target))
        self.assertNotEqual(run.returncode, 0)
        self.assertFalse(target.exists())

    def test_builder_preserves_existing_output(self):
        """P20 | existing artifact | same output name | BLOCKED without overwrite."""
        target = self.folder / "archives"
        target.mkdir()
        previous = target / "adaptive-project-ops_skill_v1.2.1.zip"
        previous.write_bytes(b"synthetic-original")
        run = self.command("scripts/build_release.py", "--output-dir", str(target))
        self.assertEqual(run.returncode, 2)
        self.assertEqual(previous.read_bytes(), b"synthetic-original")

    def test_environment_folder_not_silently_ignored(self):
        """P21 | unlisted .venv fixture | validator | still rejects non-Git metadata files."""
        directory = self.root / ".venv"
        directory.mkdir()
        (directory / "marker.txt").write_text("synthetic", encoding="ascii")
        run = self.validate()
        self.assertEqual(run.returncode, 1)
        self.assertIn(b".venv/marker.txt", run.stdout)

    def test_git_text_checkout_stability(self):
        """P22 | hashed text and LF checkout rules | prepare manifests | every packaged text uses LF."""
        run = self.command("scripts/build_release.py", "--prepare")
        self.assertEqual(run.returncode, 0, run.stderr)
        for path in distribution_files(self.root):
            if path.suffix in {".md", ".py", ".json", ".yaml", ".yml", ".txt"} or path.name in {".gitignore", ".gitattributes", "LICENSE"}:
                with self.subTest(path=path.relative_to(self.root)):
                    self.assertNotIn(b"\r\n", path.read_bytes())

    def git_checkout_fixture(self, autocrlf):
        """Commit and check out only an isolated temporary copy, without prepare."""
        git = shutil.which("git")
        if git is None:
            self.skipTest("Git executable unavailable")
        empty = self.folder / "empty-git-config"
        empty.mkdir()
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                   GIT_ATTR_NOSYSTEM="1", PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")

        def execute(cwd, *args):
            cwd.resolve().relative_to(self.folder.resolve())
            run = subprocess.run([git, "-c", f"core.hooksPath={empty}", "-c", f"core.attributesFile={os.devnull}",
                                  "-c", f"init.templateDir={empty}", "-c", "commit.gpgsign=false", *args],
                                 cwd=cwd, capture_output=True, timeout=30, env=env, check=False)
            self.assertEqual(run.returncode, 0, run.stdout.decode(errors="replace") + run.stderr.decode(errors="replace"))
            return run.stdout

        execute(self.root, "init", "-q", "--initial-branch=fixture")
        execute(self.root, "config", "core.autocrlf", "false")
        execute(self.root, "add", "--all")
        execute(self.root, "-c", "user.name=Packaging Regression", "-c", "user.email=fixture@example.invalid",
                "commit", "-q", "-m", "Temporary checkout fixture")
        checked = self.folder / "checked"
        execute(self.folder, "clone", "-q", "--local", "--no-hardlinks", "--no-checkout", str(self.root), str(checked))
        execute(checked, "config", "core.autocrlf", autocrlf)
        execute(checked, "checkout", "-q", "fixture")
        manifest = json.loads((self.root / "manifest.json").read_text(encoding="utf-8"))
        for name in ("LICENSE", (SKILL_PATH / "LICENSE").as_posix()):
            with self.subTest(autocrlf=autocrlf, path=name):
                content = (checked / name).read_bytes()
                self.assertEqual(content, execute(self.root, "show", "HEAD:" + name))
                self.assertNotIn(b"\r\n", content)
                self.assertEqual(sha256(content).hexdigest(), manifest["files"][name])
        self.assertEqual(manifest_errors(checked), [])
        self.assertEqual(manifest_errors(checked / SKILL_PATH), [])
        run = subprocess.run([sys.executable, "scripts/validate_repository.py"], cwd=checked,
                             capture_output=True, timeout=30, env=env, check=False)
        self.assertEqual(run.returncode, 0, run.stdout.decode() + run.stderr.decode())

    def test_real_git_checkout_without_autocrlf(self):
        """P23 | isolated temporary Git commit | real checkout core.autocrlf=false | LICENSE blob/hash and both manifests preserved."""
        self.git_checkout_fixture("false")

    def test_real_git_checkout_with_autocrlf(self):
        """P24 | isolated temporary Git commit | real checkout core.autocrlf=true | LICENSE blob/hash and both manifests preserved."""
        self.git_checkout_fixture("true")

    def test_license_content_tamper_rejected(self):
        """P25 | valid root and standalone licenses | append synthetic bytes separately | validator rejects LICENSE content drift."""
        for name in (Path("LICENSE"), SKILL_PATH / "LICENSE"):
            with self.subTest(path=name):
                path = self.root / name
                original = path.read_bytes()
                try:
                    path.write_bytes(original + b"synthetic-license-tamper\n")
                    run = self.validate()
                    self.assertEqual(run.returncode, 1, run.stdout.decode() + run.stderr.decode())
                    self.assertIn(b"LICENSE", run.stdout)
                finally:
                    path.write_bytes(original)

    def test_incorrect_license_checksum_rejected(self):
        """P26 | valid root and standalone manifests | replace only recorded LICENSE checksum | both manifest checks and validator reject mismatch."""
        for bundle in (self.root, self.root / SKILL_PATH):
            with self.subTest(bundle=bundle.relative_to(self.root)):
                path = bundle / "manifest.json"
                original = path.read_bytes()
                license_bytes = (bundle / "LICENSE").read_bytes()
                manifest = json.loads(original)
                manifest["files"]["LICENSE"] = "0" * 64
                try:
                    path.write_text(json.dumps(manifest), encoding="utf-8")
                    self.assertTrue(any("LICENSE" in error for error in manifest_errors(bundle)))
                    run = self.validate()
                    self.assertEqual(run.returncode, 1, run.stdout.decode() + run.stderr.decode())
                    self.assertIn(b"LICENSE", run.stdout)
                    self.assertEqual((bundle / "LICENSE").read_bytes(), license_bytes)
                finally:
                    path.write_bytes(original)


if __name__ == "__main__":
    unittest.main()
