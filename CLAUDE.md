# Claude Code handoff

เริ่มด้วยอ่าน handoffs/LATEST.md และ latest.json ถ้าสถานะ queued/awaiting_cli ให้ตรวจหนังสือใน book_path ตาม next_tasks แล้วบันทึกผลในโฟลเดอร์หนังสือ/CLAUDE_REVIEW.md แยกข้อผิดจริง ข้อเสนอ และสิ่งที่ยังไม่ยืนยัน ไม่อ้างว่าทดสอบรถจริง ไม่เดา pinout หรือค่าแผนที่จูน ไม่แก้เล่มอื่น และไม่ push/เผยแพร่เองเว้นแต่ผู้ใช้สั่ง

ทุกครั้งที่หนังสือเสร็จ ใช้ tools/book_handoff.py ตาม docs/CLAUDE_HANDOFF.md
