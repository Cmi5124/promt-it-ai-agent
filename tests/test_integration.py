"""Integration gates; static policy checks are never model behavioral runs."""
from hashlib import sha256
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from pack_utils import distribution_files, instruction_errors, local_reference_errors
from repository_checks import CONTRACT_FILES, contract_errors, preservation_errors, publication_errors


class IntegrationTest(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder=Path(self.temp.name)
        self.root=self.folder/'source'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc'))

    def test_preserve_upstream_and_imported_content(self):
        """I01 | audited upstream and imports | compare SHA-256 | protected files and skill functionality unchanged."""
        self.assertEqual(preservation_errors(self.root),[])

    def test_contract_synchronized_current_documents(self):
        """I02 | approved current contract | compare eight documents | same artifact limits and no repeat approval."""
        self.assertEqual(contract_errors(self.root),[])
        self.assertEqual(instruction_errors(self.root),[])

    def test_old_artifact_prohibition_is_rejected(self):
        """I03 | current task template | restore absolute no-change sentence | conflict detected."""
        p=self.root/'templates/TEST-ONLY.md'
        p.write_text(p.read_text(encoding='utf-8')+'\nKhông sửa code hay tạo thay đổi.\n',encoding='utf-8')
        self.assertTrue(contract_errors(self.root))

    def test_version_and_legal_metadata(self):
        """I04 | integrated manifests and licenses | inspect versions and legal scope | repo 1.1.0 candidate skill 1.2.1 Apache copies match."""
        meta=json.loads((self.root/'manifest.json').read_text(encoding='utf-8'))
        self.assertEqual(meta['repository_version'],'1.1.0')
        self.assertEqual(meta['skill_version'],'1.2.1')
        self.assertEqual(meta['release_state'],'candidate')
        self.assertEqual((self.root/'LICENSE').read_bytes(),(self.root/'skills/adaptive-project-ops/LICENSE').read_bytes())
        self.assertIn('license: Apache-2.0',(self.root/'skills/adaptive-project-ops/SKILL.md').read_text(encoding='utf-8'))

    def test_public_tree_static_review(self):
        """I05 | source publish tree | heuristic path/secret/history scan | no flags in reviewed source."""
        self.assertEqual(publication_errors(self.root),[])

    def test_synthetic_sensitive_text_is_rejected(self):
        """I06 | synthetic marker only | introduce fake credential and home path | detect without printing contents."""
        p=self.root/'synthetic.txt'
        marker='sk-'+'X'*30
        p.write_text(marker+'\n'+'C:'+chr(92)+'Users'+chr(92)+'Synthetic',encoding='utf-8')
        findings=publication_errors(self.root)
        self.assertTrue(any('credential' in e for e in findings))
        self.assertTrue(any('home path' in e for e in findings))
        self.assertFalse(any(marker in e for e in findings))

    def test_build_reproducibility(self):
        """I07 | fixed canonical source | build twice in fresh external directories | both ZIP hashes reproducible."""
        hashes=[]
        for number in (1,2):
            target=self.folder/f'build-{number}'
            run=subprocess.run([sys.executable,'scripts/build_release.py','--output-dir',str(target)],cwd=self.root,capture_output=True,timeout=30,check=False,env=dict(os.environ,PYTHONIOENCODING='utf-8',PYTHONDONTWRITEBYTECODE='1'))
            self.assertEqual(run.returncode,0,run.stdout.decode()+run.stderr.decode())
            hashes.append({p.name:sha256(p.read_bytes()).hexdigest() for p in target.glob('*.zip')})
        self.assertEqual(len(hashes[0]),2)
        self.assertEqual(hashes[0],hashes[1])

    def test_all_repository_links(self):
        """I08 | integrated docs and archives | validate local Markdown references | zero required broken links."""
        self.assertEqual(local_reference_errors(self.root),[])

    def test_ci_has_no_actions_secrets_or_write(self):
        """I09 | local workflow candidate | inspect permission and OS policy | two OS no external actions secrets write or release."""
        text=(self.root/'.github/workflows/validate.yml').read_text(encoding='utf-8')
        self.assertIn('os: [ubuntu-latest, windows-latest]',text)
        self.assertIn('contents: read',text)
        for forbidden in ('uses:','secrets.','contents: write','pull_request_target','pip install','gh release'):
            self.assertNotIn(forbidden,text)

    def test_incomplete_scope_does_not_grant_authority(self):
        """I10 | static current contract | check unauthorized artifacts and product protections | limits and lifecycle retained."""
        for name in CONTRACT_FILES:
            text=(self.root/name).read_text(encoding='utf-8')
            for required in ('chỉ trong đường dẫn/phạm vi được cấp phép','không ghi đè dữ liệu hiện có','không tự đưa artifact vào Git','production configuration','Git permissions mặc định NONE'):
                self.assertIn(required,text)

    def test_immutable_snapshot_tamper_detected(self):
        """I11 | protected snapshot fixture | alter v1.0.0 bytes | preservation failure."""
        p=self.root/'versions/v1.0.0.md'
        p.write_bytes(p.read_bytes()+b'\n')
        self.assertTrue(preservation_errors(self.root))

    def test_publication_scan_environment_failure(self):
        """I12 | mocked permission failure | enumerate source tree | error propagates rather than false PASS."""
        with patch('repository_checks.distribution_files',side_effect=PermissionError('synthetic denied')):
            with self.assertRaises(PermissionError): publication_errors(self.root)


if __name__=='__main__':
    unittest.main()
