from pathlib import Path
p=Path(__file__).resolve().parents[1]/'CLAUDE_AUTO_START/LATEST.md'
if p.exists():print(p.read_text(encoding='utf-8'))
