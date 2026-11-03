# CLAUDE_AUTO_START — คิวส่งงานทุกหัวข้อ

โฟลเดอร์นี้เป็นจุดรับงานกลางสำหรับ Claude Code ใช้กับหนังสือ โค้ด เอกสาร หรือโครงการอื่น โดย latest.json ระบุ task_path และ next_tasks; LATEST.md เป็นสรุปที่อ่านได้

ส่งงานใหม่:

```powershell
python tools/claude_handoff.py --task projects/example --instruction "ตรวจและทำงานต่อจาก README"
```

เปิดตัวเฝ้าคิวหนึ่งครั้งบนเครื่องที่ติดตั้งและลงชื่อเข้าใช้ Claude Code CLI:

```powershell
python tools/watch_claude_tasks.py
```

ตัวเฝ้าคิวอ่านคิวทุก 2 วินาทีและเริ่ม Claude Code แบบใหม่ ไม่ใช่การส่งข้อความเข้า session ที่เปิดอยู่ ต้องมีไฟล์คิวล่าสุดใน checkout นี้ การเปลี่ยนชื่อโฟลเดอร์หรือ push GitHub อย่างเดียวไม่เริ่ม Claude ขณะที่ watcher ไม่ทำงาน

สถานะ awaiting_cli = ยังไม่ได้เริ่ม, running = เรียกแล้ว, completed = คำสั่งจบสำเร็จ (ไม่ใช่การรับรองคุณภาพเนื้อหา), failed = ต้องตรวจข้อผิดพลาด
