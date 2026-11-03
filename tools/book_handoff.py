import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name("claude_handoff.py")),run_name="__main__")
