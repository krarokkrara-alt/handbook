# Independent PCB research — 14 November 2026

Researcher: pcb_independent_search. Scope: actual internal EPS PCB and visible components. No claim below identifies the Honda Z51 board.

## Exact Z51 result
Searches for 39980-TS4-Z51 / 39980-TS4-Z5 / S4S6-113282 / HTS4X-10-14M did not yield a verified code-to-PCB chain. External TS4 parts listings exist, but none establishes the internal board. Do not label another board as Z51.

## Case A — Toyota 89650-12340, actual repair photographs
Source: https://devicerepairguy.co.nz/toyota-electric-power-steering-unit-repair/
Author's own repair case; page identifies Toyota 89650-12340, JTEKT/Denso/EPS12V. This is firsthand repair evidence, not an OEM schematic or a universal fault diagnosis.

Local original assets:
- output/research-independent-assets/toyota-relay-position.jpg
  Original: https://devicerepairguy.co.nz/wp-content/uploads/2026/04/Relay-position-on-the-board.jpg
- output/research-independent-assets/toyota-relay.jpg
  Original: https://devicerepairguy.co.nz/wp-content/uploads/2026/04/The-Relay.jpg
- output/research-independent-assets/toyota-power-underside.jpg
  Original: https://devicerepairguy.co.nz/wp-content/uploads/2026/04/Transistors-screwed-under-the-board.jpg

Observed directly in photos: green main PCB, large winding/choke, large electrolytic capacitor, black relay removed beside housing; solder joints and constrained PCB/heatsink packaging. The underside image does not expose readable semiconductor device numbers, so do NOT label exact MOSFET types or positions from it.

Important correction: Article text calls relay C811-T-C-12 / AGB36101. The photo is blurred, but visible characters are consistent with CB1a-T-P-12V / ACB36101. The article spelling must NOT be copied as a confirmed part number. Second line ACB36101 is much more plausible and aligns with Panasonic's actual part pairing. For publication say: 'ภาพรีเลย์ที่ผู้ซ่อมแสดง; ตัวอักษรในบทความคลาดเคลื่อน ต้องอ่านบนอะไหล่จริงก่อนสั่ง'.

Manufacturer verification (not proof of installation in Honda):
- https://industry.panasonic.com/global/en/products/control/relay/vehicle/number/acb36101
- https://na.industrial.panasonic.com/products/relays-contactors/mechanical-power-relays/automotive/series/2822/model/2975
- Official catalog https://industry.panasonic.com/ac/cdn/e/control/relay/vehicle/catalog/mech_eng_cb.pdf
Panasonic verifies ACB36101 = CB1a-T-P-12V, sealed PC-board automotive relay, 1 Form A, 12 V DC coil, coil resistance 103 ohm ±10% at 20°C. These are component datasheet values, not ECU in-circuit pass/fail values. Plug-in CB1a-T-12V is a DIFFERENT mounting variant and should not be substituted silently.

Potential workshop lesson: relay coil resistance must be checked on the identified component with parallel circuit effects excluded; continuity sound does not assess load contact performance. Author reports other relays require invasive disassembly because PCB/power hardware/heatsink are interlocked. Do not portray a blanket relay replacement as an OEM-approved cure.

## Case B — Hyundai/Kia Emmetec W-S0095 EPS-C PCB map
Source: https://www.emmetec.com/en-us/eps/devices/95
Supplier-listed applications: Hyundai i30 ver A 2012–2017, Veloster 2011–2018, Elantra 2010–2015; Kia Cee'd 2012–2018.

Local original assets (downloaded and visually inspected):
- output/research-independent-assets/hyundai-095-1F.jpg
  https://emmetec.blob.core.windows.net/70px/095_1F.jpg
- output/research-independent-assets/hyundai-095-1R.jpg
  https://emmetec.blob.core.windows.net/70px/095_1R.jpg
- output/research-independent-assets/hyundai-emmetec.html (source snapshot)

Images have an existing supplier grid A–E / 1–4. Preserve that grid and its orientation. 1F and 1R have different viewpoints; do not mirror them to infer coordinates.
Observed: 1F shows two large electrolytics in C1/C2 region, wound components, large Tyco relay around B2, connectors; 1R shows dense logic ICs, small-signal parts, solder/power connection areas. Many IC top markings are dark/illegible, so component identities come from supplier mapping, NOT independently read chip numbers.

Supplier mapping (not chip markings):
- 1F B2: W-01005 relay
- 1F C1/C2: W-05263 capacitor
- 1R B2: W-01040 CAN chip
- 1R B1: W-05043 voltage regulator
- 1R B2: W-05264 EEPROM
- 1R D2: W-05458 motor-control chip
These W codes are Emmetec catalog IDs, not semiconductor part numbers and not reference designators printed on the PCB. This is useful for an actual-board identification lesson but NOT a Z51 replacement BOM.

Downloaded component catalog images for inspection:
- output/research-independent-assets/mt061398.png: CAN-chip photo (https://emmetec.blob.core.windows.net/400px/mt061398.png). Marking not clear enough to transcribe reliably.
- output/research-independent-assets/mt066992.png: regulator photo (https://emmetec.blob.core.windows.net/400px/mt066992.png). Marking not readable.
Additional mt075748 / mt089705 may finish downloading separately; only use after inspection.

Recommended book captions:
'Toyota 89650-12340: ภาพเคสซ่อมของ Device Repair Guy ไม่ใช่ PCB Honda Z51'
'Hyundai/Kia W-S0095: พิกัดอุปกรณ์ตามแคตตาล็อก Emmetec ไม่ใช่เบอร์ชิปและไม่ใช่ผัง Z51'

## Other leads (not developed to avoid duplicate agent research)
- Civic TR8-M91 PCB: https://www.gabisaonline.com.br/modulos/bcm/placa-circuito-do-modulo-central-de-controle-da-direcao-eletrica-elesys-39980tr8m91-honda-new-civic-013-014-015-016 ; two downloaded originals in output/pcb-research/gabisa-tr8-side1.jpg and side2.jpg. Different family from TS4-Z51.
- LifeAfter40 Civic EX 2012 has internals; author says replacement 39980-TR3-A11. Direct image download returned HTTP 403, so no image file claimed downloaded.
- TRW photo credited by Elektronikpraxis: https://www.elektronikpraxis.de/die-elektrische-servolenkung-a-9c755ea92907796e0ec5bb872dde70de/ ; general integrated module, not Civic board.

## Editorial restrictions
No exact Z51 IC pinout, rail voltage, test-point location, MOSFET substitution or fault component is established. Board photographs and supplier classifications support examples only. Use manufacturer datasheets for numeric electrical claims after identifying the actual component. No universal low-ohm/diode threshold should be invented.

## Addendum — motor gate-driver candidate in supplier image
Downloaded and inspected output/research-independent-assets/mt089705.png (https://emmetec.blob.core.windows.net/400px/mt089705.png). Emmetec labels it W-05458 motor-control chip at 1R D2. Image shows Infineon and partly legible TLE7183... / SCD4; exact line is dark, so treat identity as a candidate, not a fully verified marking.
Official Infineon reference:
- https://www.infineon.com/part/TLE7183F
- https://www.infineon.com/assets/row/public/documents/10/49/infineon-tle7183f-ds-en.pdf
The datasheet has Figure 6 Application Circuit and ordering markings TLE7183SCD1 through TLE7183SCD5. It is a 3-phase external MOSFET gate driver with diagnosis/current-sense functions. This gives an authentic manufacturer schematic to explain a plausible device family, NOT a reconstructed Hyundai ECU circuit and NOT a Honda Z51 chip identification.
Also inspected output/research-independent-assets/mt075748.png (EEPROM image): no readable marking, therefore no part number claim.
