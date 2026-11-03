from pathlib import Path
import json,time,subprocess,sys,shutil
root=Path(__file__).resolve().parents[1];latest=root/'CLAUDE_AUTO_START/latest.json';seen=None
if not shutil.which('claude'):raise SystemExit('Install/sign in to Claude Code CLI first; no watcher started')
while True:
 if latest.exists():
  job=json.loads(latest.read_text(encoding='utf-8'));key=job.get('revision')
  if key!=seen and job.get('status') in ['queued','awaiting_cli']:
   seen=key;subprocess.run([sys.executable,str(root/'tools/claude_handoff.py'),'--task',job.get('task_path',job.get('book_path'))],cwd=root)
 time.sleep(2)
