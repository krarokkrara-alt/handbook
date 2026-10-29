// รวมเล่ม ECU HANDBOOK แจกฟรี เล่ม 1 จากไฟล์ .md ในโฟลเดอร์หนังสือ เป็น HTML และ PDF
// วิธีใช้: node ecu-handbook-vol1+free/tools/build_book.cjs
// ผลลัพธ์: ecu-handbook-vol1+free/build/ECU_Handbook_Vol1_Free.html และ .pdf
const fs = require('fs');
const path = require('path');

const NODE_MODULES = 'C:/Users/Admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const { marked } = require(path.join(NODE_MODULES, 'marked'));
const { chromium } = require(path.join(NODE_MODULES, 'playwright'));

const BOOK = path.resolve(__dirname, '..');
const OUT = path.join(BOOK, 'build');
const NAME = 'ECU_Handbook_Vol1_Free';
// หัวข้อที่ต้องขึ้นหน้าใหม่เสมอ (นอกเหนือจากต้นบท)
const NEW_PAGE_HEADINGS = ['เกี่ยวกับผู้เขียน'];

// ไฟล์บทเรียงตามเลขนำหน้า (00-, 02-, 06- ...) ไฟล์ใหม่ที่ขึ้นต้นด้วยเลขจะถูกรวมเองอัตโนมัติ
const chapters = fs.readdirSync(BOOK)
  .filter(f => /^\d{2}-.*\.md$/.test(f))
  .sort();

const slug = (() => {
  let n = 0;
  return () => `s${++n}`;
})();

const toc = [];
let body = '';
for (const file of chapters) {
  let md = fs.readFileSync(path.join(BOOK, file), 'utf8');
  const tokens = marked.lexer(md);
  for (const t of tokens) {
    if (t.type === 'heading' && t.depth <= 2) {
      const id = slug();
      toc.push({ depth: t.depth, text: t.text.replace(/\*\*/g, ''), id });
      t.__id = id;
    }
  }
  const renderer = new marked.Renderer();
  const html = marked.parser(tokens, {
    renderer: Object.assign(renderer, {
      heading(token) {
        const id = token.__id ? ` id="${token.__id}"` : '';
        const cls = NEW_PAGE_HEADINGS.includes(token.text) ? ' class="new-page"' : '';
        return `<h${token.depth}${id}${cls}>${this.parser.parseInline(token.tokens)}</h${token.depth}>\n`;
      },
    }),
  });
  body += `<section class="chapter" data-file="${file}">\n${html}\n</section>\n`;
}

const present = chapters.map(f => f.slice(0, 2)).filter(n => n !== '00').map(Number);
const missing = [1, 2, 3, 4, 5, 6, 7, 8, 9].filter(n => !present.includes(n));
const today = new Date().toISOString().slice(0, 10);

const tocHtml = toc.map(e =>
  `<li class="d${e.depth}"><a href="#${e.id}">${e.text}</a></li>`).join('\n');

const html = `<!doctype html>
<html lang="th"><head><meta charset="utf-8">
<title>ECU HANDBOOK แจกฟรี เล่ม 1</title>
<style>
@page { size: A4; margin: 18mm 16mm 20mm 16mm; }
html { font-family: "Leelawadee UI", "Tahoma", sans-serif; font-size: 10.5pt; line-height: 1.6; color: #111; }
body { margin: 0; }
h1 { font-size: 20pt; color: #0d3b66; border-bottom: 3px solid #f4c430; padding-bottom: 4px; margin: 0 0 10px; }
h2 { font-size: 14.5pt; color: #0d3b66; margin: 18px 0 6px; break-after: avoid; }
h3 { font-size: 12pt; margin: 14px 0 4px; break-after: avoid; }
p, li { orphans: 2; widows: 2; }
img[src$="author-photo.jpg"] { width: 45mm; }
img { max-width: 100%; max-height: 210mm; display: block; margin: 8px auto 4px; break-inside: avoid; }
p:has(> img) { break-inside: avoid; break-after: avoid; margin-bottom: 0; }
p > em:only-child { display: block; font-size: 9pt; color: #444; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9.5pt; break-inside: auto; }
th, td { border: 1px solid #bbb; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #eef3f8; }
tr { break-inside: avoid; }
blockquote { margin: 10px 0; padding: 6px 12px; background: #fff7e0; border-left: 4px solid #e0a800; break-inside: avoid; }
blockquote p { margin: 4px 0; }
code { font-family: Consolas, monospace; font-size: 9pt; background: #f2f2f2; padding: 0 3px; }
hr { border: none; border-top: 1px solid #ccc; margin: 14px 0; }
.chapter { break-before: page; }
.new-page { break-before: page; }
p:has(> img[src$="author-photo.jpg"]) + p { text-align: center; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: center; text-align: center; }
.cover .t1 { font-size: 30pt; font-weight: bold; color: #0d3b66; }
.cover .t2 { font-size: 16pt; margin-top: 8px; }
.cover .t3 { font-size: 13pt; margin-top: 30px; }
.cover .note { font-size: 10pt; color: #8a5a00; margin-top: 40px; }
.toc { break-before: page; }
.toc ul { list-style: none; padding: 0; }
.toc li.d1 { font-weight: bold; margin-top: 8px; }
.toc li.d2 { margin-left: 18px; }
.toc a { color: #111; text-decoration: none; }
</style></head><body>
<div class="cover">
  <div class="t1">ECU HANDBOOK แจกฟรี เล่ม 1</div>
  <div class="t2">คู่มือซ่อม ECU รถยนต์ จากพื้นฐานสู่ขั้นสูง</div>
  <div class="t3">Mytech</div>
  <div class="note">ฉบับร่างรวมเล่ม ${today}<br>มีบทที่ ${present.join(', ')} · บทที่ยังไม่มี: ${missing.join(', ') || '-'}<br>หนังสือแจกฟรี ห้ามจำหน่าย</div>
</div>
<div class="toc"><h1>สารบัญ</h1><ul>${tocHtml}</ul></div>
${body}
</body></html>`;

fs.mkdirSync(OUT, { recursive: true });
const htmlPath = path.join(BOOK, `${NAME}.html`);
fs.writeFileSync(htmlPath, html, 'utf8');

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME, headless: true });
  const page = await browser.newPage();
  await page.goto('file:///' + htmlPath.replaceAll('\\', '/'), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const broken = await page.evaluate(() =>
    [...document.images].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src')));
  await page.pdf({
    path: path.join(OUT, `${NAME}.pdf`),
    format: 'A4',
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-size:8pt;color:#666;text-align:center;font-family:Tahoma">ECU HANDBOOK แจกฟรี เล่ม 1 · หน้า <span class="pageNumber"></span> / <span class="totalPages"></span></div>',
    margin: { top: '18mm', bottom: '20mm', left: '16mm', right: '16mm' },
  });
  await browser.close();
  // ย้าย HTML ไปไว้ใน build หลังพิมพ์ (ต้องอยู่ในโฟลเดอร์หนังสือตอนพิมพ์ เพื่อให้ path รูปถูก) และเติม base ให้รูปยังเปิดได้
  fs.writeFileSync(path.join(OUT, `${NAME}.html`), html.replace('<head>', '<head><base href="../">'), 'utf8');
  fs.unlinkSync(htmlPath);
  console.log('chapters:', chapters.join(', '));
  console.log('broken images:', broken.length ? broken.join(', ') : 'none');
  console.log('pdf:', path.join(OUT, `${NAME}.pdf`));
})();
