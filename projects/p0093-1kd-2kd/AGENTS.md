# P0093 Toyota 1KD 2KD publishing project

## Objective and deadline

Write a Thai book dedicated to diagnosing and repairing P0093 on Toyota 1KD-FTV and 2KD-FTV. Emphasize detailed hydraulic and electrical operating circuits, feedback control, evidence-led fault isolation, repair actions and verification. Continue meaningful improvements until 07:00 Asia/Bangkok on 2026-10-21 (2026-10-21T00:00:00Z). Do not start new research or expand scope after that deadline. Finish and report the actual completed work, marking unresolved claims.

## Workspaces

Work only inside this project for the new book. Existing ECU books remain separate. All synced project files under sources/ are read-only. Read STATUS.md before each run and write a dated progress entry when work finishes. Never overwrite another active agent's assigned files. Check live agents before spawning replacements.

## Editorial roles

- OEM researcher owns research/: Toyota and DENSO documents, vehicle/engine/manual applicability matrix and claim ledger.
- Circuit author owns circuits/: electrical and hydraulic schematics, control sequences, sources and captions.
- Diagnostic editor owns manuscript/DIAGNOSTIC_WORKFLOW.md and manuscript/REPAIR_MATRIX.md: tests, evidence, causes, repairs, verification and explicitly simulated examples.
- Coordinator owns STATUS.md, master manuscript, bibliography integration and final book production.

These are AI editorial roles, not claims of human certification or tested hardware experience.

## Evidence rules

Prefer primary Toyota and DENSO publications. Distinguish a manufacturer-authored manual mirrored on another site from official hosting. Open documents, do not cite search snippets alone. Record document code, model/market, applicability, pages/section, URL, confidence and limitations. Do not infer a model year from a download folder name. Separate 1KD and 2KD and manual revisions; never combine distinct specifications into one universal range.

Every numeric threshold, DTC enabling condition, connector pin, wire colour, ECU terminal, component specification and definitive repair procedure needs an applicable source. Where unavailable use a labelled conceptual connection with terminal function only, or mark unverified. Do not extrapolate a 1KD-only manual to 2KD. Do not invent customer cases or measurements.

## Technical and repair scope

Cover supply and return paths, pressure generation, rail pressure feedback, SCV variants, injectors/EDU where applicable, wiring and signals, DTC monitor logic, freeze-frame and related DTC priority. For every suspected cause state a discriminator, suitable test, evidence, repair if confirmed and post-repair verification. P0093 must not become a parts-replacement checklist. Duty-cycle direction and unplugged-SCV behaviour are variant-dependent and must not be universalized.

Use appropriate high-pressure safety instructions at the relevant step. Never recommend opening a running common-rail high-pressure line, disabling protection or replacing a limiter with a bypass. Mark special-tool/bench operations distinctly. Conceptual circuits must say they are conceptual, and OEM excerpts/redraws require source, applicability and rights notes.

Downloaded OEM/DENSO reference PDFs without an explicit redistribution licence are local research materials. Do not commit or republish them; publish source links, original analysis, permitted excerpts and original labelled diagrams instead. The project .gitignore excludes research PDFs.

## Production

Create original SVG schematics with junctions, crossings, functional terminals, flow direction, legend and readable Thai captions. Label electrical versus hydraulic diagrams. Prefer numerous useful visuals over padded pages. Suggested coverage: at least 16 distinct meaningful diagrams when evidence supports them; no fixed page quota. Preserve copyrighted-source boundaries and image credits. Provide source Markdown, SVG, references and final PDF/DOCX when ready. Apply documents/pdf skills for final artifacts, use the bundled runtimes, and render/inspect every final page. The previous project's Word PDF exporter stalled; the vetted HTML print workflow is available in the previous book workspace as a fallback. Do not claim completion of unrendered outputs.

## Scheduled continuation

A thread automation resumes this chat at :00 and :30 until the deadline. Make substantive progress each run, save files early, and identify the next concrete task. At 06:00 prioritize consolidation, by 06:30 prioritize QA and delivery. Do not wait for perfect source coverage before writing verified sections. If hard blockers remain, finish the verified work and list specific gaps. Notify the user only for material progress, necessary decisions, significant failures or final delivery. Do not assume a human answered a pending question.
