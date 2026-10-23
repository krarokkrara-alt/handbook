from pathlib import Path
import urllib.request,urllib.parse,urllib.error,json,hashlib,re,time
from PIL import Image
P=Path(__file__).resolve().parent;(P/'photos').mkdir(exist_ok=True)
items=[('resistors','Electronic-Axial-Lead-Resistors-Array.jpg'),('ceramic','Electronic-Component-Ceramic-Capacitor.jpg'),('electrolytic','Electronic-Component-Elec-Capacitors.jpg'),('mosfet','Electronic-Component-Through-Hole-Transistor.jpg'),('led','Electronic-Component-Red-LED.jpg')]
extra=P/'extra_photos.json'
if extra.exists():items+=json.loads(extra.read_text(encoding='utf8'))
saved=json.loads((P/'photo_manifest.json').read_text(encoding='utf8')) if (P/'photo_manifest.json').exists() else []
manifest=[]
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'ECUComponentCourse/1.0 (educational handout)'})
 for attempt in range(3):
  try:
   with urllib.request.urlopen(req,timeout=40) as r:data=r.read()
   time.sleep(4)
   return data
  except urllib.error.HTTPError as e:
   if e.code!=429 or attempt==2:raise
   delay=max(30,int(e.headers.get('Retry-After','30')))
   print('Rate limit; wait',delay,'seconds',flush=True);time.sleep(delay)
for key,title in items:
 prior=next((x for x in saved if x['id']==key and (P/x['file']).exists()),None)
 if prior:manifest.append(prior);print(key,'cached',flush=True);continue
 api='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode({'action':'query','format':'json','prop':'imageinfo','iiprop':'url|extmetadata','titles':'File:'+title})
 data=json.loads(get(api));page=next(iter(data['query']['pages'].values()));info=page['imageinfo'][0];meta=info.get('extmetadata',{})
 license_name=meta.get('LicenseShortName',{}).get('value','')
 if not any(x in license_name.lower() for x in ['public domain','cc0','cc by']):raise ValueError('Check licence: '+title+' '+license_name)
 url=info['url'];target=P/'photos'/(key+Path(title).suffix.lower())
 if not target.exists():target.write_bytes(get(url))
 with Image.open(target) as im:im.verify()
 record={'id':key,'title':title,'page_url':info['descriptionurl'],'image_url':url,'author_html':meta.get('Artist',{}).get('value',''),'license':license_name,'license_url':meta.get('LicenseUrl',{}).get('value',''),'credit_html':meta.get('Credit',{}).get('value',''),'description_html':meta.get('ImageDescription',{}).get('value',''),'file':'photos/'+target.name,'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'changes':'No changes to downloaded image file; resized in document layout only.','checked_date':'2026-10-23'}
 manifest.append(record);(P/'photo_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
 print(key,license_name,target.stat().st_size)
