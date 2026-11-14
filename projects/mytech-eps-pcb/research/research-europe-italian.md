# European EPS PCB research — Fiat / Opel

Date: 14 November 2026. Researcher: pcb_independent_search.

## Selected case: Emmetec W-S0015, EPS-C
Primary supplier page: https://www.emmetec.com/en-us/eps/devices/15
Source lists Fiat Grande Punto 2005–2009, Grande Punto EVO 2009–2012, Opel Corsa D first series 2006–2014. This is an EPS-C electric-column case, NOT an EHPS hydraulic-pump ECU. It does not establish a Honda Z51 board or compatibility between all listed variations.

### Original assets saved and visually inspected
- output/europe-assets/015_1F.jpg
  https://emmetec.blob.core.windows.net/70px/015_1F.jpg
- output/europe-assets/015_1R.jpg
  https://emmetec.blob.core.windows.net/70px/015_1R.jpg
- output/europe-assets/mt061909.png — supplier image of W-05021 motor-control IC
  https://emmetec.blob.core.windows.net/400px/mt061909.png
- output/europe-assets/mt061546.png — supplier MOSFET image; top marking too faint to identify reliably
  https://emmetec.blob.core.windows.net/400px/mt061546.png
- output/europe-assets/emmetec-15.html — source HTML snapshot
- output/europe-assets/A3935-Datasheet.pdf — official manufacturer PDF, 13 pages
  https://www.allegromicro.com/~/media/Files/Datasheets/A3935-Datasheet.ashx

### What the PCB images visibly show
1F: six power packages clustered at the left of the board, three heavy motor leads (yellow/black/red), connectors on right, logic/analog ICs and passives. Supplier grid A–J / 1–6 is part of the original image and must be preserved.
1R: reverse PCB traces, large orange capacitor bank, wound filter component and relay; thermal/interface pads are visible near the power-stage region. Do not infer net topology from reverse-side pads alone.

### Supplier mapping, not independently proven PCB netlist
The page maps:
- W-05017 MOSFET at 1F A1, B1, C1, A3, B2, C3.
- W-05021 motor-control IC at 1F B4.
- W-01015 CAN chip at 1F H5.
- W-05204 regulator at 1F D4.
- W-05117 dual op amp at 1F E4.
- W-05118 quad voltage comparator at 1F E3.
- W-01021 relay at 1R F4.
These W codes are Emmetec product codes, NOT chip part numbers or board reference designators. The full-board image does not resolve every top marking clearly.

### Readable device marking and manufacturer linkage
The close-up mt061909.png clearly reads `A3935KLQT` with the Allegro logo. This is the physical top marking shown in the supplier's component photo linked to W-05021. Do not claim it was independently read from the full-board B4 image, which is smaller and less clear.

The official A3935 datasheet identifies the A3935 family as a 3-phase automotive external N-MOSFET controller. It includes six gate-drive outputs, a boost function, bootstrap high-side supply, a current-monitor differential amplifier, and fault/under-voltage protection. The source is suitable for an authentic chip-level schematic lesson tied to a real supplier PCB map.

Suffix caution: the photo's top marking is `A3935KLQT`; ordering names in manufacturer documents may include hyphens and reel packing suffixes (`A3935KLQTR-T`, etc.). Quote the observed marking as observed. Do not silently turn it into a particular currently orderable SKU or recommend a drop-in replacement. Package LQ is 36-lead QSOP. The exact board netlist and installed device revision remain unverified.

Useful manufacturer pages in the PDF:
- PDF page 1: Typical Application with external MOSFET bridge.
- PDF page 3: Functional Block Diagram (gate outputs, current sense, boost/regulator/fault blocks).
- Later electrical tables: numeric specifications under their stated test conditions. None is a Honda Z51 test specification.

Recommended book caption:
“Fiat Grande Punto / Opel Corsa D: ภาพ PCB และพิกัดตามแคตตาล็อก Emmetec W-S0015; ภาพชิปที่ผู้ขายจับคู่แสดง A3935KLQT. ใช้ datasheet Allegro อธิบายภาค gate driver ไม่ใช่ schematic ทั้งบอร์ดหรือวงจรของ Z51.”

## Secondary lead: Fiat Punto 188 W-S0012 / W-S0013
Sources:
- https://www.emmetec.com/en-us/eps/devices/12
- https://www.emmetec.com/en-us/eps/devices/13
Saved snapshots: output/europe-assets/emmetec-12.html and emmetec-13.html.

W-S0012 is listed as Punto ver A 6971/9232/6670/9234 1999–2010; source distinguishes a motor board with relays for first series 1999–2003 (V-04032). W-S0013 is Punto ver B 9236/1075/1077/9238 1999–2010 and source describes a later motor board without relays on the top, with Hall sensors (V-04033). Both EPS-C. Do not treat the broad year range as proof every Punto has the same board or that all steering faults are relay faults.

Downloaded extra files include 012_1F.jpg / 012_1R.jpg / 012_2R.jpg / 013_1R.jpg / 013_2R.jpg. For the book's selected European case, prefer the fully checked W-S0015 pair and A3935 linkage above. Some guessed image names do not appear in source HTML (e.g. 012_1R, 013_1R); do NOT use them as source-linked assets merely because a URL returned an image. Only use filenames found in the corresponding HTML and inspect them separately.

## Repair interpretation limits
- Show component locations only according to the cited supplier grid, not as confirmed circuit nodes.
- No live-voltage injection test, universal gate voltage, or MOSFET substitution is derived from photos.
- Lack of gate output may be due to disabled control, supply/boost/bootstrap/fault state, not a dead gate-driver IC.
- Before diode/ohm checks isolate supply and residual charge. Parallel circuit effects can misidentify parts.
- Manufacturer Typical Application is a real example schematic, not a reverse-engineered ECU schematic.
