# Book handoff policy

เมื่อสร้างหรือแก้หนังสือเสร็จ ให้สรุปผลในแชต และรัน `python tools/claude_handoff.py --task <repository-relative-folder>` ทุกครั้ง เพื่อเขียน CLAUDE_AUTO_START/latest.json และ CLAUDE_AUTO_START/LATEST.md แล้วเรียก Claude Code ถ้ามี CLI และสิทธิ์ใช้งานพร้อม หากยังเรียกไม่ได้ ต้องรายงานว่า queued ไม่ใช่ completed ห้ามระบุว่า Claude รับงานแล้วโดยไม่มีผลเรียกจริง

รักษาไฟล์เล่มอื่นและงานผู้ใช้ที่ไม่เกี่ยวข้อง เครดิตภาพ/หน้าจอและข้อจำกัดตรงรุ่นต้องติดไปกับไฟล์ที่เผยแพร่
