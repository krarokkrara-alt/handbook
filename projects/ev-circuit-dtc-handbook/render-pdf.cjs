const fs=require('fs');
const {spawn}=require('child_process');
const {pathToFileURL}=require('url');
const path=require('path');
async function run(){
 const inputHtml=fs.readFileSync('EV-CIRCUIT-DTC-HANDBOOK.html','utf8');
 for(const src of new Set([...inputHtml.matchAll(/(?:src|href)="(assets\/[^"?#]+)"/g)].map(x=>x[1]))){
  const b=fs.readFileSync(src);if(b.length<32)throw Error('Empty image: '+src);
  if(b[0]===255&&b[1]===216&&!(b[b.length-2]===255&&b[b.length-1]===217))throw Error('Incomplete JPEG: '+src);
 }
 const chrome=spawn('C:/Program Files/Google/Chrome/Application/chrome.exe',['--headless=new','--disable-gpu','--no-first-run','--no-default-browser-check','--remote-debugging-port=0','--user-data-dir='+path.resolve('.render-profile'),'about:blank'],{windowsHide:true,stdio:['ignore','ignore','pipe']});
 const endpoint=await new Promise((resolve,reject)=>{let out='';chrome.stderr.on('data',b=>{out+=b;let m=out.match(/DevTools listening on (ws:\/\/[^\s]+)/);if(m)resolve(m[1]);});chrome.on('error',reject);setTimeout(()=>reject(Error('Chrome startup timed out')),25000).unref()});
 const ws=new WebSocket(endpoint);await new Promise(r=>ws.addEventListener('open',r,{once:true}));let n=0,pending=new Map();
 ws.addEventListener('message',e=>{const a=JSON.parse(e.data);if(a.id&&pending.has(a.id)){const [r,j]=pending.get(a.id);pending.delete(a.id);a.error?j(Error(JSON.stringify(a.error))):r(a.result)}});
 function call(method,params={},sessionId){return new Promise((r,j)=>{const id=++n;pending.set(id,[r,j]);ws.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})}))})}
 try {
 const {targetId}=await call('Target.createTarget',{url:'about:blank'});const {sessionId}=await call('Target.attachToTarget',{targetId,flatten:true});const c=(m,p)=>call(m,p,sessionId);
 await c('Page.enable');await c('Page.navigate',{url:pathToFileURL(path.resolve('EV-CIRCUIT-DTC-HANDBOOK.html')).href});
 await c('Runtime.evaluate',{expression:'new Promise(resolve=>{if(document.readyState==="complete")resolve(true);else addEventListener("load",()=>resolve(true),{once:true})})',awaitPromise:true});
 await c('Runtime.evaluate',{expression:'document.fonts.ready',awaitPromise:true});
 await c('Emulation.setEmulatedMedia',{media:'print'});
 const result=await c('Runtime.evaluate',{expression:`JSON.stringify([...document.querySelectorAll('.page')].map((p,i)=>{let f=p.querySelector('.foot').getBoundingClientRect(),m=p.querySelector('main').getBoundingClientRect();let svgOverflow=[...p.querySelectorAll('svg text')].filter(t=>{let s=t.ownerSVGElement.getBoundingClientRect(),r=t.getBoundingClientRect();return r.left<s.left-2||r.right>s.right+2||r.top<s.top-2||r.bottom>s.bottom+2}).length;return {page:i+1,height:p.getBoundingClientRect().height,contentBottom:m.bottom-p.getBoundingClientRect().top,available:f.top-p.getBoundingClientRect().top,overflow:m.bottom>f.top-8,actualPhotoIds:[...p.querySelectorAll('[data-image-type="C"]')].map(x=>x.getAttribute('data-image-id')),images:[...p.querySelectorAll('img')].map(x=>({src:x.getAttribute('src'),loaded:x.complete&&x.naturalWidth>0})),svgTextOutsideViewBox:svgOverflow,wide:[...p.querySelectorAll('td,th')].filter(x=>x.scrollWidth>x.clientWidth+2).length}}))`,returnByValue:true});
 const audit=JSON.parse(result.result.value);fs.writeFileSync('layout-audit.json',JSON.stringify(audit,null,2));
 console.log(JSON.stringify({pages:audit.length,overflows:audit.filter(x=>x.overflow),failedImages:audit.flatMap(x=>x.images.filter(z=>!z.loaded)),wide:audit.filter(x=>x.wide)},null,2));
 if(audit.some(x=>x.overflow||x.images.some(z=>!z.loaded)||new Set(x.actualPhotoIds).size<2))throw Error('Layout / actual-photo check failed');
 const pdf=await c('Page.printToPDF',{printBackground:true,preferCSSPageSize:true,displayHeaderFooter:false,generateTaggedPDF:true});const bytes=Buffer.from(pdf.data,'base64');fs.writeFileSync('EV-CIRCUIT-DTC-HANDBOOK.pdf',bytes);
 const count=[...bytes.toString('latin1').matchAll(/\/Type\s*\/Page\b/g)].length;console.log('PDF pages='+count+'; bytes='+bytes.length);if(count!==50)throw Error('Wrong PDF page count');
 await c('Emulation.setEmulatedMedia',{media:'screen'});await c('Emulation.setDeviceMetricsOverride',{width:1000,height:1200,deviceScaleFactor:1,mobile:false});
 fs.mkdirSync('previews',{recursive:true});
 for(const pageNo of [1,3,9,19,21,32,33,37,42,43,47,50]){
  const r=await c('Runtime.evaluate',{expression:`(()=>{let p=document.getElementById('page-${pageNo}');p.scrollIntoView();let r=p.getBoundingClientRect();return {x:r.x+scrollX,y:r.y+scrollY,width:r.width,height:r.height,scale:1}})()`,returnByValue:true});
  const img=await c('Page.captureScreenshot',{format:'png',captureBeyondViewport:true,clip:r.result.value});fs.writeFileSync('previews/page-'+String(pageNo).padStart(2,'0')+'.png',Buffer.from(img.data,'base64'));
 }
 fs.writeFileSync('verification.json',JSON.stringify({pdfPages:count,pageSize:'A4 210 × 297 mm',htmlSections:audit.length,contentFooterCollisionCount:0,failedImageLoads:0,minimumActualPhotosPerPage:Math.min(...audit.map(x=>new Set(x.actualPhotoIds).size)),photographicPlacements:audit.reduce((s,x)=>s+x.actualPhotoIds.length,0),svgTextOutsideViewBox:audit.filter(x=>x.svgTextOutsideViewBox),limits:'Automated layout and source-file placement checks; not engineering or print-legibility certification',created:new Date().toISOString()},null,2));
 }finally{try{await call('Browser.close')}catch{}ws.close();chrome.kill()}
}
run().catch(e=>{console.error(e);process.exitCode=1});
