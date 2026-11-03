# Claude Code — งานทุกหัวข้อ

อ่าน CLAUDE_AUTO_START/LATEST.md และ CLAUDE_AUTO_START/latest.json ก่อน รับงานใน task_path ตาม next_tasks ไม่จำกัดว่าเป็นหนังสือ ตรวจ README/brief และหลักฐานของหัวข้อนั้น บันทึกผลและข้อเสนอใน task_path/CLAUDE_REVIEW.md ไม่อ้างผลตรวจที่ไม่ได้ทำ และไม่ publish/push เองหากผู้ใช้ไม่ได้สั่ง

เมื่องานใหม่เสร็จ ใช้ `python tools/claude_handoff.py --task <folder>` เพื่อส่งคิวต่อ ดู CLAUDE_AUTO_START/README.md การเริ่มอัตโนมัติต้องมี Claude CLI และ watcher ทำงาน การมีโฟลเดอร์อย่างเดียวไม่ปลุก session ที่เปิดอยู่
