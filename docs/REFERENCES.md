# เอกสารอ้างอิงและเครดิต

คัดรายการจากต้นฉบับเต็ม รหัส S ของภาคซ่อม ECU และภาคหน่วยความจำอ้างถึงคนละชุด ให้ดูหัวข้อกำกับรายการเสมอ

[ทะเบียนเครดิตภาพ](../data/photo_credits.json) • [ข้อมูลวงจร](../circuits/circuits.json)

## เอกสารอ้างอิงวงจรไฟฟ้า

รหัส S ในภาคสองใช้รายการอ้างอิงการซ่อม ECU ส่วนรหัส S ในภาคสามใช้รายการอ้างอิงงานหน่วยความจำท้ายเล่มนี้

[C1] TI TIDA 01167 battery protection

https://www.ti.com/tool/TIDA-01167

[C2] NXP MPC5604P hardware design guide

https://www.nxp.com/docs/en/user-guide/MPC5604PQRUG.pdf

[C3] TI LM1815 VR conditioner

https://www.ti.com/lit/ds/symlink/lm1815.pdf

[C4] TI LM1949 injector drive and flyback clamp

https://www.ti.com/lit/ds/symlink/lm1949.pdf

[C5] NXP TJA1050 SO8

https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf

### เอกสารอ้างอิงวงจรไฟฟ้าต่อ

[C6] ST L9637 SO8

https://www.st.com/resource/en/datasheet/l9637.pdf

[C7] ST M95320 W SO8

https://www.st.com/resource/en/datasheet/m95320-w.pdf

[C8] Microchip 24LC256 SOIC

https://ww1.microchip.com/downloads/en/DeviceDoc/21203R.pdf

[C9] ST M93C66 W SO8

https://www.st.com/resource/en/datasheet/m93c46-w.pdf

[C10] Speeduino Hardware v0.4.3d Rev 4d

https://github.com/speeduino/Hardware/blob/main/v0.4/THT/Latest/v0.4.3d.pdf

วงจร 27 ถึง 30 วาดใหม่ ปรับการจัดวาง และคัดเฉพาะบางภาคจาก Speeduino โดย Codex เมื่อ 16 ตุลาคม 2569 ใช้ CERN-OHL-S-2.0 เช่นเดียวกับต้นทาง ผู้พัฒนา Speeduino ไม่ได้รับรองหนังสือเล่มนี้

ต้นทาง https://github.com/speeduino/Hardware • ใบอนุญาต https://opensource.org/license/CERN-OHL-S-2.0 • ต้นฉบับที่แก้ไขแนบใน ECU_Circuit_Drawings.zip

### อ้างอิงเบอร์ชิปและหน้าที่

[X1] ST Serial EEPROM selection guide

https://www.st.com/resource/en/selection_guide/sgeeprom0921_web.pdf

[X2] ST M95320 W R DF datasheet

https://www.st.com/resource/en/datasheet/m95320-w.pdf

[X3] ST M24C64 W R F DF datasheet

https://www.st.com/resource/en/datasheet/m24c64-w.pdf

[X4] ST M93C46 M93C56 M93C66 M93C76 M93C86 datasheet

https://www.st.com/resource/en/datasheet/m93c46-w.pdf

[X5] Microchip 93LC66B and A B C organization

https://www.microchip.com/en-us/product/93LC66B

[X6] Microchip 24LC256

https://www.microchip.com/en-us/product/24LC256

### อ้างอิงเบอร์ชิปและหน้าที่ต่อ

[X7] Microchip 25LC256

https://www.microchip.com/en-us/product/25LC256

[X8] NXP Philips TJA1050 datasheet

https://www.nxp.com/docs/en/data-sheet/TJA1050.pdf

[X9] ST L9637 datasheet

https://www.st.com/resource/en/datasheet/l9637.pdf

[X10] Infineon TLE6220GP datasheet

https://www.infineon.com/assets/row/public/documents/10/49/infineon-tle6220gp-ds-en.pdf

[X11] Infineon TLE4274 datasheet

https://www.infineon.com/assets/row/public/documents/10/49/infineon-tle4274-datasheet-en.pdf

[X12] Infineon TLE42754D

https://www.infineon.com/part/TLE42754D

### อ้างอิงเบอร์ชิปและหน้าที่ต่อ

[X13] ST L9788 datasheet

https://www.st.com/resource/en/datasheet/l9788.pdf

[X14] NXP MPC5554 datasheet

https://www.nxp.com/docs/en/data-sheet/MPC5554.pdf

[X15] NXP MC9S12DP256 datasheet

https://www.nxp.com/docs/en/data-sheet/MC9S12DP256.pdf

[X16] Infineon TC1796 datasheet

https://www.infineon.com/dgdl/Infineon-SAK-TC1796-256F150E%2BBE-DS-v01_00-EN.pdf?fileId=5546d46249a28d

### อ้างอิงการซ่อม ECU

[S1] NXP Hardware Design Guide MPC5604P ครอบคลุมภาคจ่ายไฟและการเชื่อมต่อ CAN https://www.nxp.com/docs/en/user-guide/MPC5604PQRUG.pdf

[S2] Texas Instruments TIDA 01167 Automotive Battery Input Protection ตัวอย่างภาคป้องกันไฟยานยนต์ https://www.ti.com/tool/TIDA-01167

[S3] Pico Automotive CAN and CAN FD bus decoding การจับและถอดรหัสบัส https://www.picoauto.com/library/picoscope-automotive-training/knowledge-base/can-and-can-fd-bus-decoding

[S4] Pico Automotive How to Connect a PicoScope Automotive Oscilloscope หลักการต่อและตรวจสัญญาณ https://www.picoauto.com/library/product-news/how-to-connect-a-picoscope-automotive-oscilloscope

[S5] Pico Automotive A guide to oscilloscope diagnostics https://www.picoauto.com/download/documents/manuals/DO253-11_oscilloscope_guide.pdf

### อ้างอิงงานหน่วยความจำ

[S1] STMicroelectronics M95320 W R DF Datasheet ตัวอย่างชิปฝึกและผังขา https://www.st.com/resource/en/datasheet/m95320-w.pdf

[S2] STMicroelectronics AN2014 How to best use serial EEPROMs หลักการใช้งานและไฟเลี้ยง https://www.st.com/resource/en/application_note/an2014-how-to-best-use-stmicroelectronics-serial-eeproms-stmicroelectronics.pdf

[S3] NXP S32K1xx Reference Manual Security Overview ตัวอย่างการตรวจโปรแกรมและข้อมูลเฉพาะตัว https://community.nxp.com/pwmxy87654/attachments/pwmxy87654/s32sdk/2479/1/S32K1xx_RM_Rev13.pdf

[S4] Infineon AURIX Security Solutions ตัวอย่าง HSM และพื้นที่รักษาความปลอดภัย https://www.infineon.com/product-information/aurix-security-solutions

[S5] Infineon AURIX TC3xx Non Volatile Memory Subsystem ตัวอย่างโครงสร้างหน่วยความจำและ ECC https://documentation.infineon.com/aurixtc3xx/docs/qbu1702561828906

[S6] Microchip Getting Started with Serial EEPROM ภาพรวมบัสและการเลือกหน่วยความจำ https://www.microchip.com/en-us/products/memory/serial-eeprom/getting-started

[S7] STMicroelectronics Automotive Serial EEPROM Documentation เอกสารสำหรับชิปยานยนต์ตามรุ่น https://www.st.com/en/memories/automotive-serial-eeprom/documentation.html

## เครดิตภาพถ่ายจริง

[P1] Inside ECU.JPG

ผู้ถ่าย Snewkirk7953

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:Inside_ECU.JPG

https://creativecommons.org/licenses/by-sa/3.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P2] Keysight InfiniiVision DSOX 4024A and digital multimeter and power supply in laboratory use.jpg

ผู้ถ่าย Radarvector; ไฟล์ครอบตัดเผยแพร่โดย Pittigrilli

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Keysight_InfiniiVision_DSOX_4024A_and_digital_multimeter_and_power_supply_in_laboratory_use.jpg

https://creativecommons.org/licenses/by-sa/4.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P3] Surecom EP-427 - board - National Semiconductor 93C56-7948.jpg

ผู้ถ่าย Raimond Spekking

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Surecom_EP-427_-_board_-_National_Semiconductor_93C56-7948.jpg

https://creativecommons.org/licenses/by-sa/4.0

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P4] IC-package-QFP.jpg

ผู้ถ่าย Sphl at Japanese Wikipedia

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:IC-package-QFP.jpg

http://creativecommons.org/licenses/by-sa/3.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P5] Soldering a 0805.jpg

ผู้ถ่าย Aisart

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:Soldering_a_0805.jpg

https://creativecommons.org/licenses/by-sa/3.0

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P6] Kl Intel Pentium MMX embedded BGA Bottom.jpg

ผู้ถ่าย Konstantin Lanzet

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:Kl_Intel_Pentium_MMX_embedded_BGA_Bottom.jpg

https://creativecommons.org/licenses/by-sa/3.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P7] BGA joint xray.jpg

ผู้ถ่าย No machine-readable author provided. DJGB assumed (based on copyright claims).

ใบอนุญาต Public domain

https://commons.wikimedia.org/wiki/File:BGA_joint_xray.jpg

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P8] PopcornBGA.jpg

ผู้ถ่าย Textbook

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:PopcornBGA.jpg

https://creativecommons.org/licenses/by-sa/3.0

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P11] Motorsteuerung VW Golf TDI innen.jpg

ผู้ถ่าย Cschirp at German Wikipedia

ใบอนุญาต CC BY-SA 3.0 de

https://commons.wikimedia.org/wiki/File:Motorsteuerung_VW_Golf_TDI_innen.jpg

https://creativecommons.org/licenses/by-sa/3.0/de/deed.en

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P12] EDC17CP20.jpg

ผู้ถ่าย KaiBorgeest

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:EDC17CP20.jpg

https://creativecommons.org/licenses/by-sa/3.0

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P13] Beurer BC-18 - controller board - Microchip Technology 24LC08BI-0471.jpg

ผู้ถ่าย Raimond Spekking

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Beurer_BC-18_-_controller_board_-_Microchip_Technology_24LC08BI-0471.jpg

https://creativecommons.org/licenses/by-sa/4.0

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P14] Jetta ECU.JPG

ผู้ถ่าย Mkamara9540; ไฟล์ครอบตัดโดย Wikisympathisant

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Jetta_ECU.JPG

https://creativecommons.org/licenses/by-sa/4.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P15] JECS GA16DE ECU.jpg

ผู้ถ่าย RB30DE at English Wikipedia

ใบอนุญาต Public domain

https://commons.wikimedia.org/wiki/File:JECS_GA16DE_ECU.jpg

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P16] JECS RB30E ECU.jpg

ผู้ถ่าย RB30DE at English Wikipedia

ใบอนุญาต Public domain

https://commons.wikimedia.org/wiki/File:JECS_RB30E_ECU.jpg

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P17] An ECM from a 1996 Chevrolet Beretta- 2013-10-24 23-13.jpg

ผู้ถ่าย Mgiardina09

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:An_ECM_from_a_1996_Chevrolet_Beretta-_2013-10-24_23-13.jpg

https://creativecommons.org/licenses/by-sa/3.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P18] Dell E2210f - controller board - STMicroelectronics 24C16WP-4697.jpg

ผู้ถ่าย Raimond Spekking

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Dell_E2210f_-_controller_board_-_STMicroelectronics_24C16WP-4697.jpg

https://creativecommons.org/licenses/by-sa/4.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P19] Iomega Jaz V2000Si JAZ 2 - board - Atmel 25040N-0558.jpg

ผู้ถ่าย Raimond Spekking

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:Iomega_Jaz_V2000Si_JAZ_2_-_board_-_Atmel_25040N-0558.jpg

https://creativecommons.org/licenses/by-sa/4.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

[P20] 3COM Megahertz 3CCE589ET - board - Fairchild 93C66-6666.jpg

ผู้ถ่าย Raimond Spekking

ใบอนุญาต CC BY-SA 4.0

https://commons.wikimedia.org/wiki/File:3COM_Megahertz_3CCE589ET_-_board_-_Fairchild_93C66-6666.jpg

https://creativecommons.org/licenses/by-sa/4.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ

### เครดิตภาพถ่ายจริงต่อ

[P21] Fluke 115 multimeter.jpg

ผู้ถ่าย J.C. Fields User Typhoon

ใบอนุญาต CC BY-SA 3.0

https://commons.wikimedia.org/wiki/File:Fluke_115_multimeter.jpg

https://creativecommons.org/licenses/by-sa/3.0/

ย่อขนาดและแปลงรูปแบบไฟล์เพื่อจัดพิมพ์ ไม่เปลี่ยนเนื้อหาภาพ
