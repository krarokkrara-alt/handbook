// ต่อเล่ม Wiring ECU 3ZZ-FE: คงหน้าเดิมจาก source/ สร้างสารบัญ ภาคต่อ และประวัติผู้เขียนจาก pages/*.html
// ลำดับเล่ม: ปก, สารบัญใหม่, หน้า 3–25 เดิม, ภาคต่อ (ไฟล์เลขต่ำกว่า 090), ภาคผนวกเดิม, ไฟล์เลข 090 ขึ้นไป
// วิธีใช้: node projects/wiring-ecu-3zz/build_book.cjs
const fs = require('fs');
const path = require('path');

const NODE_MODULES = 'C:/Users/Admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const { chromium } = require(path.join(NODE_MODULES, 'playwright'));
const { PDFDocument, StandardFonts, rgb } = require(path.join(NODE_MODULES, 'pdf-lib'));

const ROOT = __dirname;
const SRC_PDF = path.join(ROOT, 'source', 'Mytech-Wiring-ECU-book_v1.pdf');
const OUT_PDF = process.env.BOOK_OUT || path.join(ROOT, 'build', 'Mytech-Wiring-ECU-3ZZ-FE.pdf');
const TITLE = 'Wiring ECU 3ZZ-FE';
const OLD_LAST_BODY = 25; // หน้าสุดท้ายของเนื้อหาเดิมก่อนภาคผนวก
const OLD_TOC = [
  [3, '1 เครื่องมือและจุดอ้างอิงการวัด'], [4, '2 Air Flow'], [9, '3 มอเตอร์ควบคุมรอบเดินเบา'],
  [12, '4 คอยล์จุดระเบิดและ IGT'], [16, '5 หัวฉีดน้ำมันเชื้อเพลิง'], [17, '6 VVT-i'],
  [18, '7 การระบุ ECU และการอ่านวงจร'], [20, '8 แบบฝึก Simulator'], [24, '9 ใบงานและการประเมิน'],
  [25, 'รายการตรวจรับเนื้อหา'],
];

const CSS = fs.readFileSync(path.join(ROOT, 'book.css'), 'utf8');

function inlineAssets(html) {
  return html.replace(/<img([^>]*?)src="([^"]+)"/g, (m, a, src) => {
    if (/^(data:|https?:)/.test(src)) return m;
    const file = path.join(ROOT, src);
    if (!fs.existsSync(file)) throw new Error(`ไม่พบไฟล์ภาพ ${src}`);
    const ext = path.extname(file).slice(1).toLowerCase();
    const mime = { svg: 'image/svg+xml', jpg: 'image/jpeg', jpeg: 'image/jpeg', png: 'image/png' }[ext];
    return `<img${a}src="data:${mime};base64,${fs.readFileSync(file).toString('base64')}"`;
  });
}

function wrapPage(inner, number) {
  return `<section class="page"><div class="running">${TITLE}</div>${inner}<div class="folio">${String(number).padStart(2, '0')}</div></section>`;
}

(async () => {
  const src = await PDFDocument.load(fs.readFileSync(SRC_PDF));
  const srcCount = src.getPageCount();
  const appendixCount = srcCount - OLD_LAST_BODY;
  const files = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => /^\d+.*\.html$/.test(f)).sort();
  const pages = files.map(f => ({ file: f, html: fs.readFileSync(path.join(ROOT, 'pages', f), 'utf8') }));
  const body = pages.filter(p => parseInt(p.file, 10) < 90);
  const tail = pages.filter(p => parseInt(p.file, 10) >= 90);

  const firstNew = OLD_LAST_BODY + 1;
  const firstAppendix = firstNew + body.length;
  const firstTail = firstAppendix + appendixCount;
  body.forEach((p, i) => { p.num = firstNew + i; });
  tail.forEach((p, i) => { p.num = firstTail + i; });

  const heading = p => {
    const t = p.html.match(/<h1[^>]*>(.*?)<\/h1>/s);
    return t && !t[0].includes('data-notoc') ? [p.num, t[1].replace(/<[^>]+>/g, '')] : null;
  };
  const toc = [...OLD_TOC, ...body.map(heading).filter(Boolean), [firstAppendix, 'ภาคผนวก ผังอ้างอิงและรายการตรวจรับ'], ...tail.map(heading).filter(Boolean), [firstTail + 1, 'ประวัติการทำงานและกิตติกรรมประกาศ']];
  const half = Math.ceil(toc.length / 2);
  const col = list => `<ol class="toc">${list.map(([n, t]) => `<li><b>${String(n).padStart(2, '0')}</b>${t}</li>`).join('')}</ol>`;
  const tocPage = wrapPage(`<h1>การใช้หนังสือและสารบัญ</h1>
<p>หนังสือเล่มนี้ใช้ฝึกสังเกตตำแหน่งอุปกรณ์ การต่อเครื่องมือวัด และการบันทึกผล ก่อนเชื่อมโยงเข้าสู่การอ่านวงจร ECU และการจำลองสัญญาณด้วย Simulator ผู้เรียนควรทำตามลำดับบทและบันทึกเงื่อนไขทุกครั้ง เพื่อให้เปรียบเทียบผลได้ถูกต้อง</p>
<p>ผลตัวอย่างในภาพเป็นค่าที่ได้จากการทดลองแต่ละครั้ง ไม่ใช่เกณฑ์มาตรฐานผ่านหรือไม่ผ่านสำหรับรถทุกรุ่น จุดตรวจที่ 1 ถึง 5 เป็นลำดับในบทเรียน ไม่ใช่หมายเลขขาปลั๊กตามคู่มือ</p>
<p>หน้า ${firstNew} เป็นต้นไปคือภาคต่อ Wiring 3ZZ-FE ทุกค่าบอกที่มา <span class="tag m">วัดจริง</span> คือค่าจากภาพในบทเรียน <span class="tag w">ผังรถ</span> คืออ่านจากผัง Altis ในภาคผนวก <span class="tag p">ผังหลักการ</span> คือหลักวงจรทั่วไป <span class="tag x">ยังไม่ยืนยัน</span> คือต้องตรวจกับรถจริงก่อนใช้</p>
<div class="toc-cols">${col(toc.slice(0, half))}${col(toc.slice(half))}</div>`, 2);

  const seq = [{ key: 'toc', html: tocPage }];
  [...body, ...tail].forEach(p => seq.push({ key: p.file, html: wrapPage(inlineAssets(p.html), p.num) }));

  const doc = `<!doctype html><html lang="th"><head><meta charset="utf-8"><title>${TITLE}</title><style>${CSS}</style></head><body>${seq.map(p => p.html).join('\n')}</body></html>`;
  fs.mkdirSync(path.join(ROOT, 'tmp'), { recursive: true });
  fs.mkdirSync(path.dirname(OUT_PDF), { recursive: true });
  const htmlFile = path.join(ROOT, 'tmp', 'new_pages.html');
  fs.writeFileSync(htmlFile, doc);

  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  await page.goto('file:///' + htmlFile.replace(/\\/g, '/'));
  await page.evaluate(() => document.fonts.ready);
  const over = await page.evaluate(() => [...document.querySelectorAll('section.page')].map((s, i) => {
    const folio = s.querySelector('.folio').getBoundingClientRect().top;
    const last = [...s.children].filter(c => !c.classList.contains('folio'))
      .reduce((m, c) => Math.max(m, c.getBoundingClientRect().bottom), 0);
    return { i, over: Math.round(last - folio + 6) };
  }).filter(x => x.over > 0));
  over.forEach(o => console.log(`ล้นหน้า: ${seq[o.i].key} เกิน ${o.over}px`));
  const pdfBytes = await page.pdf({ preferCSSPageSize: true, printBackground: true });
  await browser.close();

  const fresh = await PDFDocument.load(pdfBytes);
  if (fresh.getPageCount() !== seq.length) throw new Error(`หน้า Chrome ${fresh.getPageCount()} ไม่เท่ากับ ${seq.length}`);

  const out = await PDFDocument.create();
  out.setTitle(TITLE);
  out.setAuthor('Supunya Pharaphong (Mytech)');
  const font = await out.embedFont(StandardFonts.Helvetica);
  const addFresh = async i => { const [p] = await out.copyPages(fresh, [i]); out.addPage(p); };
  const addSrc = async n => {
    const [p] = await out.copyPages(src, [n - 1]);
    out.addPage(p);
    // หน้าเดิมไม่มีเลขหน้า เติมเลขให้ตรงกับสารบัญ
    p.drawText(String(out.getPageCount()).padStart(2, '0'), { x: p.getWidth() - 50, y: 22, size: 11.5, font, color: rgb(0.33, 0.33, 0.33) });
  };
  await addSrc(1);
  await addFresh(0);
  for (let n = 3; n <= OLD_LAST_BODY; n++) await addSrc(n);
  for (let i = 0; i < body.length; i++) await addFresh(1 + i);
  for (let n = OLD_LAST_BODY + 1; n <= srcCount; n++) await addSrc(n);
  for (let i = 0; i < tail.length; i++) await addFresh(1 + body.length + i);

  fs.writeFileSync(OUT_PDF, await out.save());
  console.log('หน้า:', out.getPageCount(), 'หน้า ไฟล์', (fs.statSync(OUT_PDF).size / 1048576).toFixed(1), 'MB');
})().catch(e => { console.error(e); process.exit(1); });
