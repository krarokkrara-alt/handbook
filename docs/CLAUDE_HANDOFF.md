# ส่งงานหนังสือให้ Claude Code

เมื่อเสร็จแต่ละเล่มให้รันจากราก repository:

```powershell
python tools/claude_handoff.py --task books/chatgpt-created/mytech-wiring-lpg-tuning
```

คำสั่งเขียนคิวและเรียก `claude -p` ให้ตรวจต่อ หากมี CLI และลงชื่อเข้าใช้ไว้แล้ว ผลจะอยู่ในโฟลเดอร์หนังสือ/CLAUDE_REVIEW.md ไม่ยกเว้นระบบสิทธิ์หรือเปิด auto-push

ถ้าต้องการตรวจคิวใหม่อัตโนมัติ ให้เปิดเทอร์มินัลหนึ่งครั้งและคงไว้:

```powershell
python tools/watch_claude_tasks.py
```

watcher ตรวจคิวทุก 2 วินาทีใน checkout นี้ ต้องดึง commit ใหม่มายัง checkout นี้เองหากงานสร้างจากอีกเครื่อง ไม่มีคำสั่ง git pull อัตโนมัติที่อาจชนงานแก้ไขอยู่ การมีไฟล์ใน GitHub ไม่ทำให้ Claude Code session ที่เปิดอยู่เริ่มเทิร์นเอง

SessionStart hook แสดง handoff ล่าสุดเมื่อเริ่ม Claude Code session ใหม่; CLAUDE.md ระบุงานรับช่วงไว้ หากไม่มี CLI คิวเป็น awaiting_cli และยังไม่เริ่ม Claude จริง ต้องติดตั้งและลงชื่อเข้าใช้ Claude Code CLI บนเครื่องที่ทำงานก่อน

อ้างอิงคำสั่ง CLI: https://code.claude.com/docs/en/headless
