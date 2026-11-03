import importlib.util,tempfile,unittest,json,sys
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('handoff',Path(__file__).with_name('claude_handoff.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class HandoffTest(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(dir=m.ROOT);self.root=Path(self.temp.name);(self.root/'books/demo').mkdir(parents=True);(self.root/'books/demo/README.md').write_text('example');self.original=m.ROOT;m.ROOT=self.root
 def tearDown(self):m.ROOT=self.original;self.temp.cleanup()
 def test_missing_cli_keeps_queue(self):
  with patch.object(sys,'argv',['x','--task','books/demo']),patch.object(m.shutil,'which',return_value=None):self.assertEqual(m.main(),2)
  self.assertEqual(json.loads((self.root/'CLAUDE_AUTO_START/latest.json').read_text())['status'],'awaiting_cli')
 def test_success_records_review_and_deduplicates(self):
  result=m.subprocess.CompletedProcess([],0,'review passed','')
  with patch.object(sys,'argv',['x','--task','books/demo']),patch.object(m.shutil,'which',return_value='claude.exe'),patch.object(m.subprocess,'run',return_value=result) as call:
   self.assertEqual(m.main(),0);self.assertEqual(m.main(),0);self.assertEqual(call.call_count,1)
  self.assertEqual((self.root/'books/demo/CLAUDE_REVIEW.md').read_text(),'review passed')
 def test_outside_repository_rejected(self):
  with patch.object(sys,'argv',['x','--task','../']):
   with self.assertRaises(SystemExit):m.main()
if __name__=='__main__':unittest.main()

