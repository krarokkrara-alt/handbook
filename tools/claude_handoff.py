"""Queue a completed task and invoke a new Claude Code review when available."""
from pathlib import Path
import argparse,json,hashlib,shutil,subprocess,datetime,os
ROOT=Path(__file__).resolve().parents[1]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--task','--book',dest='book',required=True);ap.add_argument('--instruction',action='append');ap.add_argument('--queue-only',action='store_true');args=ap.parse_args()
 book=(ROOT/args.book).resolve()
 if not book.is_relative_to(ROOT) or not book.is_dir():raise SystemExit('Task must be an existing directory inside this repository')
 files=[p for p in book.rglob('*') if p.is_file() and p.name!='CLAUDE_REVIEW.md']
 digest=hashlib.sha256(''.join(p.relative_to(ROOT).as_posix()+hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)).encode()).hexdigest()
 folder=ROOT/'CLAUDE_AUTO_START';folder.mkdir(exist_ok=True);latest=folder/'latest.json'
 old=json.loads(latest.read_text(encoding='utf-8')) if latest.exists() else {}
 if old.get('revision')==digest and old.get('status')=='completed':print('Already reviewed');return 0
 data={'task_path':book.relative_to(ROOT).as_posix(),'created_by':'ChatGPT','revision':digest,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'queued','next_tasks':args.instruction or ['Inspect the completed task and its README or brief','Check correctness, completeness and relevant evidence','Record actionable findings in CLAUDE_REVIEW.md; do not publish or push']}
 def save():latest.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 save();(folder/'LATEST.md').write_text('# Ready for Claude Code\n\nTask: '+data['task_path']+'\n\nCreated by: ChatGPT\nRevision: '+digest+'\n\nRead latest.json for tasks. This file is a queue signal, not proof Claude has started.\n',encoding='utf-8')
 cli=shutil.which('claude')
 if args.queue_only:return 0
 if not cli:data['status']='awaiting_cli';save();print('Queued: Claude CLI not available; no Claude run started');return 2
 prompt='Continue the completed task at '+data['task_path']+'. Read CLAUDE_AUTO_START/latest.json and CLAUDE.md. Inspect text sources; report technical issues, screenshot/version mismatches and unverified claims. Do not publish or push. Return a concise Thai review.'
 data['status']='running';save()
 try:
  command=[cli,'-p',prompt,'--allowedTools','Read,Glob,Grep','--output-format','text']
  if os.name=='nt' and Path(cli).suffix.lower() in ['.cmd','.bat']:command=[os.environ.get('COMSPEC','cmd.exe'),'/d','/c',*command]
  result=subprocess.run(command,cwd=ROOT,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=900)
  (book/'CLAUDE_REVIEW.md').write_text(result.stdout or result.stderr,encoding='utf-8')
  data['status']='completed' if result.returncode==0 else 'failed';data['exit_code']=result.returncode;save();return result.returncode
 except (OSError,subprocess.TimeoutExpired) as exc:data['status']='failed';data['error']=str(exc);save();return 1
if __name__=='__main__':raise SystemExit(main())
