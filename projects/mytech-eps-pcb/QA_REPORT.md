# QA report — 14 November 2026

- Rebuilt from the packaged source folder with `python scripts/build.py` successfully. Fixed a missing output/pdf directory creation found during the first clean rebuild.
- `python scripts/validate.py` passed: 54 pages, page-label presence, SHA-256 asset hashes and complete image decoding.
- Text-width checks: zero overflowing lines in the core and Europe generators.
- The 42-page baseline was visually inspected; all 12 added European pages and the replacement cover were rendered and visually inspected. Latest page 2 and page 51 were rechecked after navigation/ST-family clarifications.
- Three research agents searched sources directly. Technical reviewer found no remaining must-fix in the Europe draft after preserving supplier-coordinate uncertainty and clarifying chip-family versus actual-suffix evidence.
- Exact Honda TS4-Z51 internal PCB, OEM full-board schematic, real board measurements and per-revision compatibility remain unverified. Do not promote supplier maps or reference schematics into those claims.
- Third-party reuse permission was not obtained. See SOURCES_AND_RIGHTS.md before downstream redistribution.
