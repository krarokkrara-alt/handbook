from pathlib import Path
import subprocess, sys, shutil
root = Path(__file__).resolve().parents[1]
(root / 'output/pdf').mkdir(parents=True, exist_ok=True)
for script in ('build_mytech_core.py', 'order_mytech.py', 'build_europe.py', 'merge_europe.py'):
    subprocess.run([sys.executable, str(root / script)], cwd=root, check=True)
target = root / 'docs/mytech-eps-pcb-handbook.pdf'
target.parent.mkdir(exist_ok=True)
shutil.copy2(root / 'output/pdf/mytech-eps-pcb-handbook-europe.pdf', target)
print(target)
