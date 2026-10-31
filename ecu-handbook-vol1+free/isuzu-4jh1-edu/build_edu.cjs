// ต่อเล่ม ISUZU 4JH1 EDU: คงหน้า 1, 3–18 เดิมจาก PDF ที่อยู่ใน build/ สร้างสารบัญและหน้าใหม่จาก pages/*.html
// วิธีใช้: node ecu-handbook-vol1+free/isuzu-4jh1-edu/build_edu.cjs
const fs = require('fs');
const path = require('path');

const NODE_MODULES = 'C:/Users/Admin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const { chromium } = require(path.join(NODE_MODULES, 'playwright'));
const { PDFDocument } = require(path.join(NODE_MODULES, 'pdf-lib'));

const ROOT = __dirname;
const SRC_PDF = path.join(ROOT, 'source', 'ISUZU_4JH1_EDU_v1.pdf');
const OUT_PDF = process.env.EDU_OUT || path.join(ROOT, '..', 'build', 'ISUZU_4JH1_EDU.pdf');
const VIDEO_URL = 'https://vt.tiktok.com/ZSg7Pkp69/';
const OLD_TOC = [
  [3, 'กล่อง EDU และรายละเอียดชิ้นงาน'], [4, 'ตำแหน่งอุปกรณ์บนเครื่องยนต์'],
  [5, 'ผังขั้วต่อและวงจรอ้างอิง'], [6, 'การต่อสายที่หน้าปลั๊ก'], [7, 'วงจรรวมของระบบ'],
  [8, 'วงจรบริเวณ Spill Valve'], [9, 'เครื่องกำเนิดสัญญาณ'], [10, 'รูปคลื่นหลังป้อนสัญญาณ'],
  [11, 'แรงดันบริเวณ Spill Valve'], [12, 'แผงวงจรด้านอุปกรณ์'], [13, 'แผงวงจรอีกด้าน'],
  [14, 'การวัดบนบอร์ด'], [15, 'จุดวัด Hi Volt กลางบอร์ด'], [16, 'ค่ารูปคลื่นที่หน้าจอแสดง'],
  [17, 'IGBT ในชุดบอร์ดทดสอบ'], [18, 'Power MOSFET และวงจรขับเกต'],
];

const CSS = fs.readFileSync(path.join(ROOT, 'book.css'), 'utf8');

function inlineAssets(html) {
  // รูปและ SVG เรียกด้วย path สัมพัทธ์จาก isuzu-4jh1-edu/
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
  return `<section class="page"><div class="running">ISUZU 4JH1 EDU</div>${inner}<div class="folio">${String(number).padStart(2, '0')}</div></section>`;
}

(async () => {
  const files = fs.readdirSync(path.join(ROOT, 'pages')).filter(f => /^\d+.*\.html$/.test(f)).sort();
  const newPages = files.map(f => ({ file: f, html: fs.readFileSync(path.join(ROOT, 'pages', f), 'utf8') }));
  const FIRST = 19;
  // หน้าคลิปวิดีโอเดิมวางก่อนไฟล์เลข 090 ขึ้นไป (ประวัติผู้เขียนและกิตติกรรมประกาศ)
  const videoIndex = newPages.findIndex(p => parseInt(p.file, 10) >= 90);
  const tocNew = [];
  newPages.forEach((p, i) => {
    const t = p.html.match(/<h1[^>]*>(.*?)<\/h1>/s);
    const num = FIRST + i + (i >= videoIndex && videoIndex >= 0 ? 1 : 0);
    if (t && !p.html.includes('data-notoc')) tocNew.push([num, t[1].replace(/<[^>]+>/g, '')]);
  });
  const videoPage = videoIndex >= 0 ? FIRST + videoIndex : FIRST + newPages.length;
  const toc = [...OLD_TOC, ...tocNew, [videoPage, 'คลิปวิดีโอประกอบหนังสือ']].sort((a, b) => a[0] - b[0]);
  const half = Math.ceil(toc.length / 2);
  const col = list => `<ol class="toc">${list.map(([n, t]) => `<li><b>${String(n).padStart(2, '0')}</b>${t}</li>`).join('')}</ol>`;
  const tocPage = wrapPage(`<h1>สารบัญและวิธีอ่านหนังสือ</h1>
<div class="toc-cols">${col(toc.slice(0, half))}${col(toc.slice(half))}</div>
<p>หน้า 3–18 คือภาพการต่อชุดทดสอบและผลวัด เพื่อให้ดูชิ้นงาน จุดวัด และหน้าจอเครื่องมือควบคู่กัน ค่าต่าง ๆ เป็นค่าที่ปรากฏขณะถ่ายภาพแต่ละภาพ ไม่ใช่เกณฑ์มาตรฐานสำหรับตัดสินกล่องดีหรือเสีย</p>
<p>หน้า 19 เป็นต้นไปคือภาคต่อ อธิบายสายไฟ ไฟต่ำ ไฟสูง และกล่อง ECM ของ 4JH1 ทุกค่าบอกที่มา ค่าที่วัดเองติดป้าย <b>วัดจริง</b> ข้อมูลจากสายไฟรถติดป้าย <b>ผังรถ</b> และส่วนในกล่องที่ยังไม่ได้ไล่ลายติดป้าย <b>ผังหลักการ</b></p>`, 2);

  const renderSeq = [];
  renderSeq.push({ key: 'toc', html: tocPage });
  newPages.forEach((p, i) => {
    const num = FIRST + i + (i >= videoIndex && videoIndex >= 0 ? 1 : 0);
    renderSeq.push({ key: p.file, html: wrapPage(inlineAssets(p.html), num), num });
  });

  const doc = `<!doctype html><html lang="th"><head><meta charset="utf-8"><title>ISUZU 4JH1 EDU</title><style>${CSS}</style></head><body>${renderSeq.map(p => p.html).join('\n')}</body></html>`;
  fs.mkdirSync(path.join(ROOT, 'tmp'), { recursive: true });
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
  over.forEach(o => console.log(`ล้นหน้า: ${renderSeq[o.i].key} เกิน ${o.over}px`));
  const pdfBytes = await page.pdf({ preferCSSPageSize: true, printBackground: true });
  await browser.close();

  const src = await PDFDocument.load(fs.readFileSync(SRC_PDF));
  const fresh = await PDFDocument.load(pdfBytes);
  if (fresh.getPageCount() !== renderSeq.length) throw new Error(`หน้า Chrome ${fresh.getPageCount()} ไม่เท่ากับ ${renderSeq.length}`);

  const out = await PDFDocument.create();
  out.setTitle('ISUZU 4JH1 EDU');
  out.setAuthor('Supunya Pharaphong (Mytech)');
  const addSrc = async n => { const [p] = await out.copyPages(src, [n - 1]); out.addPage(p); return p; };
  const addNew = async i => { const [p] = await out.copyPages(fresh, [i]); out.addPage(p); return p; };
  await addSrc(1);
  await addNew(0);
  for (let n = 3; n <= 18; n++) {
    const p = await addSrc(n);
    // หน้า 4 ภาพเดิมติดข้อความลิงก์ path ในเครื่องของผู้จัดทำตำราต้นทาง ปิดไว้
    if (n === 4) {
      const { rgb } = require(path.join(NODE_MODULES, 'pdf-lib'));
      p.drawRectangle({ x: 85, y: 268, width: 445, height: 32, color: rgb(1, 1, 1) });
    }
  }
  for (let i = 0; i < newPages.length; i++) {
    if (i === videoIndex) await addVideo();
    await addNew(i + 1);
  }
  if (videoIndex < 0) await addVideo();

  async function addVideo() {
    const p = await addSrc(19);
    const white = { r: 1, g: 1, b: 1 };
    const { rgb } = require(path.join(NODE_MODULES, 'pdf-lib'));
    p.drawRectangle({ x: 505, y: 6, width: 80, height: 34, color: rgb(white.r, white.g, white.b) });
    const png = await page_number_png(videoPage);
    const img = await out.embedPng(png);
    p.drawImage(img, { x: 505, y: 8, width: 60, height: 30 });
  }

  async function page_number_png(n) {
    const b = await chromium.launch({ executablePath: CHROME });
    const pg = await b.newPage({ viewport: { width: 240, height: 120 } });
    await pg.setContent(`<body style="margin:0;background:#fff"><div style="font:44px Tahoma;color:#555;text-align:right;padding:32px 22px 0 0">${String(n).padStart(2, '0')}</div></body>`);
    const buf = await pg.screenshot();
    await b.close();
    return buf;
  }

  fs.writeFileSync(OUT_PDF, await out.save());
  console.log('หน้า:', out.getPageCount(), 'หน้า ไฟล์', (fs.statSync(OUT_PDF).size / 1048576).toFixed(1), 'MB');
  console.log('ลิงก์วิดีโอ', VIDEO_URL, 'ต้องตรวจว่าคงอยู่หลังรวมเล่ม');
})().catch(e => { console.error(e); process.exit(1); });
