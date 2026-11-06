from pathlib import Path
from PIL import Image
import json
root=Path('/Users/nathaniellev/Desktop/Sites')
out=Path(__file__).resolve().parents[1]/'dist/assets'
assets=[
('hero','Events','3.47.55',(80,76,37,1116,1074,1162,1119,121)),
('planting-team','Events','3.47.08',(81,73,115,1113,1156,1078,1121,39)),
('nature-center','Events','3.47.13',(87,54,49,1093,1088,1131,1128,92)),
('planting-project','Events','3.47.40',None),
('protecting-plants','Events','3.47.46',(63,52,11,1091,1049,1144,1102,104)),
('planting-action','Events','3.47.50',(86,89,107,1130,1148,1109,1127,69)),
('before-after','Events','3.48.01',None),
('festival-booth','Events','3.48.22',None),
('festival-child','Events','3.48.31',None),
('festival-team','Events','3.48.37',None),
('harvest-team','OSI','2.34.00',None),
('harvest-pepper','OSI','2.34.10',None),
('harvest-crate','OSI','2.34.21',None),
('logo','Events','3.08.51',None)]
index=[]
for name,folder,time,quad in assets:
 p=next((root/folder).glob('*at '+time+'*'))
 im=Image.open(p).convert('RGB')
 if quad: im=im.transform((1000,1040),Image.Transform.QUAD,quad,Image.Resampling.BICUBIC)
 elif name=='festival-team':
  w,h=im.size; im=im.crop((0,0,w,int(h*.97)))
 elif name in ['festival-booth','festival-child']:
  w,h=im.size; im=im.crop((int(w*.055),int(h*.015),int(w*.945),int(h*.965)))
 elif name=='harvest-team': im=im.crop((5,5,im.width-5,im.height-5))
 elif name in ['harvest-pepper','harvest-crate']: im=im.crop((3,3,im.width-3,im.height-3))
 elif name=='before-after': im=im.crop((35,20,im.width-35,im.height-20))
 sizes=[]
 for width in sorted(set([min(480,im.width),min(900,im.width),min(1400,im.width)])):
  copy=im.copy(); copy.thumbnail((width,10000)); dest=out/f'{name}-{width}.webp'; copy.save(dest,'WEBP',quality=85,method=6); sizes.append({'file':dest.name,'width':copy.width,'height':copy.height,'bytes':dest.stat().st_size})
 index.append({'name':name,'original':str(p),'outputs':sizes})
city=Image.open('/Users/nathaniellev/Documents/ChatGPT/OSI Website/public/assets/partner-rochester-hills.png').convert('RGBA')
city.thumbnail((420,420)); city.save(out/'rochester-hills.webp','WEBP',quality=90)
(out/'asset-index.json').write_text(json.dumps(index,indent=2))
print('Optimized',len(index),'supplied images; originals preserved.')
