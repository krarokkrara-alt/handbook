"""Verify published files using only the Python standard library."""
from pathlib import Path
from zipfile import ZipFile
from urllib.parse import unquote
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
errors = []
manifest = json.loads((ROOT / "data/publication_manifest.json").read_text(encoding="utf-8"))
for item in manifest["files"]:
    path = ROOT / item["path"]
    if not path.is_file():
        errors.append(f"Missing book: {item['path']}")
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != item["sha256"] or path.stat().st_size != item["bytes"]:
        errors.append(f"Book differs from publication manifest: {item['path']}")
    if path.suffix == ".docx":
        with ZipFile(path) as archive:
            bad = archive.testzip()
            if bad:
                errors.append(f"Invalid DOCX member: {bad}")

circuits = json.loads((ROOT / "circuits/circuits.json").read_text(encoding="utf-8"))
if len(circuits) != 30:
    errors.append("Expected 30 circuit sheets")
for circuit in circuits:
    if not (ROOT / "circuits/svg" / (circuit["key"] + ".svg")).is_file():
        errors.append(f"Missing schematic: {circuit['key']}")

for markdown in ROOT.rglob("*.md"):
    text = markdown.read_text(encoding="utf-8")
    for target in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        relative = unquote(target.split("#", 1)[0].strip("<>"))
        if not (markdown.parent / relative).exists():
            errors.append(f"Broken link in {markdown.relative_to(ROOT)}: {target}")

for edition, expected in [("full", 118), ("course", 31)]:
    text = (ROOT / "manuscripts" / (edition + ".md")).read_text(encoding="utf-8")
    actual = len(re.findall(r"!\[[^\]]*\]\(", text))
    if actual != expected:
        errors.append(f"Image count for {edition}: expected {expected}, got {actual}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: book hashes, DOCX integrity, 30 circuit sheets, 149 image references, and local Markdown links")
