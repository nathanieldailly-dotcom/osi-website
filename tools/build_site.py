from pathlib import Path
from html import escape
import json,re
from PIL import Image
base=Path(__file__).resolve().parents[1]
data=json.loads((base/'content.json').read_text())
assets=json.loads((base/'dist/assets/asset-index.json').read_text())
lookup={item['name']:item['outputs'] for item in assets}
# The green community logo follows the user’s supplied reference.
lookup['logo']=[{'file':'osi-community-green.png','width':1536,'height':1024}]
lookup['city']=[{'file':'rochester-hills.webp','width':420,'height':357}]
lookup['absolute-logo']=[{'file':'absolute-logo.webp','width':334,'height':148}]
lookup['museum']=[{'file':'museum-farmhouse.webp','width':784,'height':500}]
lookup['international-academy-logo']=[{'file':'international-academy-logo.webp','width':192,'height':182}]
def img(name,alt,cls=''):
 sizes=lookup[name]; largest=sizes[-1]; chosen=sizes[-2] if len(sizes)>1 else largest
 srcset=', '.join(f"assets/{s['file']} {s['width']}w" for s in sizes)
 eager=name in ['hero','logo-mark']
 sizesattr='(max-width: 700px) 100vw, 60vw' if name=='hero' else '(max-width: 700px) 85vw, 40vw'
 if name in ['city','logo-mark']: sizesattr='160px'
 return f'<img src="assets/{chosen["file"]}" srcset="{srcset}" sizes="{sizesattr}" width="{largest["width"]}" height="{largest["height"]}" alt="{escape(alt,quote=True)}" class="{cls}" loading="{"eager" if eager else "lazy"}" decoding="async"'+(' fetchpriority="high"' if name=='hero' else '')+'>'
html=(base/'index.template.html').read_text()
html=re.sub(r'\{\{image:([^|]+)\|([^|]+)\|([^}]+)?\}\}',lambda m:img(m[1],m[2],m[3] or ''),html)
entries=[]
for e in data['events']+data.get('undatedEvents',[]):
 picclass='bbcc-photo' if e['id']=='bbcc-event' else 'founding' if e['kind']=='founding' else ('city' if e.get('image')=='city' else ('collaborator' if e.get('image') in ['absolute-logo','international-academy-logo'] else ('museum' if e.get('image')=='museum' else '')))
 visual=img(e['image'],e['alt']) if e.get('image') else '<strong>BBCC</strong><span>Birmingham Bloomfield<br>Community Coalition</span>'
 if e.get('imageCreditUrl'): visual+=f'<p class="image-credit">{escape(e["imageCredit"])} · <a href="{escape(e["imageCreditUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Source: BBCC</a></p>'
 link=e.get('link')
 more=f'<a class="text-link" href="{link}"'+(' target="_blank" rel="noopener noreferrer"' if link and link.startswith('https:') else '')+f'>{e.get("label","")}</a>' if link else ''
 hours=f'<div class="event-hours"><strong>{escape(e["hours"])}</strong><span>volunteer hours</span></div>' if e.get('hours') else ''
 date=escape(e.get('date') or 'Community volunteering')
 entries.append(f'<article id="{e["id"]}" class="timeline-entry reveal" tabindex="-1"><figure class="timeline-picture {picclass}">{visual}</figure><div class="timeline-copy"><p class="eyebrow">{date}</p><h3>{e["title"]}</h3>{hours}<p>{e["description"]}</p>{more}</div></article>')
values={**data['impact'],**data['contact'],'timeline':'\n'.join(entries),'recognition':data['recognition'],'learningUrl':data['learningResource']}
def member_profiles(members):
 profiles=[]
 for member in members:
  name=escape(member['name']); role=escape(member['role']); bio=('<p>'+escape(member['bio'])+'</p>') if member.get('bio') else ''
  portrait=img(member['image'],member.get('alt',member['name']),'team-portrait') if member.get('image') else '<div class="team-monogram" aria-hidden="true">'+escape(''.join(word[0] for word in member['name'].split())[:2])+'</div>'
  profiles.append(f'<article class="team-profile">{portrait}<div class="team-profile-copy"><p class="eyebrow">{role}</p><h3>{name}</h3>{bio}</div></article>')
 return profiles
profiles=member_profiles(data.get('team',{}).get('members',[]))
values['leadershipProfiles']='<div class="team-profile-grid">'+''.join(member_profiles(data.get('team',{}).get('leadership',[])))+'</div>'
event_cards=[]
for e in data['events']+data.get('undatedEvents',[]):
 if e['kind']=='founding': continue
 category='medical' if e['id']=='absolute-event' else 'environment' if e['id']=='burgess-milestone' else 'food' if e['id']=='international-academy-food-service-day' else 'community'
 link='medical.html' if category=='medical' else e.get('link','events.html')
 external=' target="_blank" rel="noopener noreferrer"' if link.startswith('https:') else ''
 visual=img(e['image'],e['alt']) if e.get('image') else '<strong>BBCC</strong><span>Birmingham Bloomfield<br>Community Coalition</span>'
 if e.get('imageCreditUrl'): visual+=f'<p class="image-credit">{escape(e["imageCredit"])} · <a href="{escape(e["imageCreditUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Source: BBCC</a></p>'
 event_cards.append(f'<article id="{e["id"]}" class="directory-event" data-category="{category}"><div class="directory-photo {"bbcc-photo" if e["id"]=="bbcc-event" else "logo-photo" if e.get("image") in ["city","absolute-logo","international-academy-logo"] else ""}">{visual}</div><div class="directory-copy"><p class="eyebrow">{escape(e.get("date") or "Date not recorded")} / {category.title()}</p><h2>{escape(e["title"])}</h2><p>{escape(e["description"])}</p><a class="text-link" href="{escape(link,quote=True)}"{external}>Explore this event</a></div></article>')
scout_profiles=[]
for candidate in data.get('team',{}).get('eagleScoutCandidates',[]):
 name=escape(candidate)
 initials=escape(''.join(word[0] for word in candidate.split())[:2])
 scout_profiles.append(f'<article class="team-profile"><div class="team-monogram" aria-hidden="true">{initials}</div><div class="team-profile-copy"><p class="eyebrow">Eagle Scout candidate</p><h3>{name}</h3></div></article>')
values['scoutProfiles']='<div class="team-profile-grid">'+''.join(scout_profiles)+'</div>'

partnership_sections=[]
for partnership in data.get('communityPartnerships',[]):
 visual=img(partnership['image'],partnership['alt'])
 if partnership.get('imageCreditUrl'):
  visual+=f'<figcaption class="image-credit">{escape(partnership["imageCredit"])} · <a href="{escape(partnership["imageCreditUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Source: BBCC</a></figcaption>'
 partnership_sections.append(f'<section id="{escape(partnership["id"],quote=True)}" tabindex="-1" class="community-partnership sage-bg section"><div class="wrap two-columns"><figure class="bbcc-photo">{visual}</figure><div><p class="eyebrow">{escape(partnership["date"])} / Community partnership</p><h2>{escape(partnership["title"])}</h2><div class="feature-stat"><strong>{escape(partnership["hours"])}</strong><p>volunteer hours</p></div><p>{escape(partnership["description"])}</p><a class="text-link" href="{escape(partnership["link"],quote=True)}" target="_blank" rel="noopener noreferrer">{escape(partnership["label"])}</a></div></div></section>')
values['communityPartnerships']=''.join(partnership_sections)

values['eventCards']=''.join(event_cards)
values['teamProfiles']='<div class="team-profile-grid">'+''.join(profiles)+'</div>' if profiles else '<div class="team-profiles-pending"><h3>Founder profiles coming soon.</h3><p>Check back to meet the people who helped start Oakland Service Initiative.</p></div>'

sponsor_items=[]
for sponsor in data.get('sponsorsAndCommunityPartners',[]):
 name=escape(sponsor['name'])
 logo=''
 if sponsor.get('logo'):
  logo_class="sponsor-logo sponsor-logo-wide" if sponsor["width"] / sponsor["height"] > 3 else "sponsor-logo"
  logo=f'<span class="{logo_class}"><img src="{escape(sponsor["logo"],quote=True)}" width="{sponsor["width"]}" height="{sponsor["height"]}" alt="{escape(sponsor["alt"],quote=True)}" loading="lazy" decoding="async"></span>'
 sponsor_items.append(f'<li>{logo}<strong>{name}</strong></li>')
values['sponsorList']=''.join(sponsor_items)

heart=[[0,1,0,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,1,1,0],[0,0,1,0,0]]
values['leds']=''.join(f'<rect x="{187+c*30}" y="{115+r*30}" width="16" height="16" rx="3" fill="{"#e8977e" if heart[r][c] else "#52675a"}"/>' for r in range(5) for c in range(5))
for key,value in values.items():html=html.replace('{{'+key+'}}',str(value))
assert '{{' not in html, 'Unresolved template placeholder'
(base/'dist/index.html').write_text(html)
# Separate story documents use shared navigation and footer, with links back home.
source_template=(base/'index.template.html').read_text()
head=source_template.split('<body>',1)[0]
header=re.search(r'<header class="site-header">[\s\S]*?</header>',source_template).group()
footer=re.search(r'<footer[\s\S]*?</footer>',source_template).group()
def home_navigation(markup):
 return re.sub(r'href="#([^"]+)"',lambda m:'href="/#'+m[1]+'"',markup)
def render(markup):
 markup=re.sub(r'\{\{image:([^|]+)\|([^|]+)\|([^}]+)?\}\}',lambda m:img(m[1],m[2],m[3] or ''),markup)
 for key,value in values.items(): markup=markup.replace('{{'+key+'}}',str(value))
 assert '{{' not in markup, 'Unresolved story template placeholder'
 return markup
stories=[('about','Why We Started','/#work','Our Programs','OSI began in 2023 to turn concern for Oakland County’s health and community into action through education, hospitality, and nature.'),('education','Education','community.html','Explore Community','Hands-on micro:bit education with Oakland Service Initiative.'),('community','Community','events.html','Explore Events','Food assistance, planting, and community events with Oakland Service Initiative.'),('medical','Medical','events.html','Explore Events','Health and hospice volunteering with Absolute Home Health and Hospice.'),('events','Events','/#program-pages','Events & Team','Documented OSI community festivals, food assistance, environmental projects, and medical volunteering.'),('community-events','Community Events','events.html','Explore Events','The Rochester Heritage Festival on May 30–31, 2026. Explore OSI’s planting activities, community connections, and photos from our largest event.'),('food-assistance','Food Assistance','environmental-service.html','Explore Environmental Service','Food assistance through harvesting and volunteering with Gleaners. 5,000+ meals helped prepare or create.'),('environmental-service','Environmental Service','food-assistance.html','Explore Food Assistance','More than $3,000 worth of plants planted. Explore OSI’s 500-plant project at Burgess-Shadbush Nature Center.'),('meet-the-team','Meet the Team','/#involved','Get Involved','Meet the people behind Oakland Service Initiative and its community service in the Oakland region since 2023.')]
for slug,title,next_url,next_label,description in stories:
 page_head=re.sub(r'<title>.*?</title>','<title>'+title+' — Oakland Service Initiative</title>',head)
 page_head=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="'+escape(description,quote=True)+'">',page_head)
 page_head=re.sub(r'<meta property="og:title" content="[^"]*">','<meta property="og:title" content="'+title+' — Oakland Service Initiative">',page_head)
 page_head=re.sub(r'<meta property="og:description" content="[^"]*">','<meta property="og:description" content="'+escape(description,quote=True)+'">',page_head)
 story=(base/(slug+'.template.html')).read_text()
 page_header=home_navigation(header)
 if slug in ['meet-the-team','events','about']: page_header=page_header.replace('href="'+slug+'.html"','href="'+slug+'.html" aria-current="page"')
 breadcrumb='<a href="/#mission">Our mission</a>' if slug=='meet-the-team' else '<a href="/#work">Our Work</a>'
 next_links='' if slug in ['meet-the-team','about'] else '<div class="wrap detail-next"><a class="button green" href="/#work">Back to Our Work</a><a class="text-link" href="'+next_url+'">'+next_label+'</a></div>'
 if slug=='about':
  page=page_head+'<body class="detail-page story-page"><a class="skip-link" href="#main">Skip to content</a>'+page_header+'<main id="main" class="detail-main about-main" tabindex="-1">'+story+'</main>'+home_navigation(footer)+'</body></html>'
 else:
  page=page_head+'<body class="detail-page"><a class="skip-link" href="#main">Skip to content</a>'+page_header+'<main id="main" class="detail-main" tabindex="-1"><nav class="wrap detail-breadcrumb" aria-label="Breadcrumb">'+breadcrumb+'<span aria-hidden="true">/</span><span aria-current="page">'+title+'</span></nav>'+story+next_links+'</main>'+home_navigation(footer).replace('href="/#home">Back to top','href="#main">Back to top')+'</body></html>'
 (base/'dist'/(slug+'.html')).write_text(render(page))

print('Built static site with',len(entries),'documented timeline entries.')

origin='https://oakland-service-initiative-preview.lukanatinv.chatgpt.site'
for page in (base/'dist').glob('*.html'):
 url=origin+('/' if page.name=='index.html' else '/'+page.name)
 markup=page.read_text()
 markup=re.sub(r'\s*<link rel="canonical"[^>]*>','',markup)
 markup=re.sub(r'\s*<meta property="og:url"[^>]*>','',markup)
 markup=markup.replace('</head>','  <link rel="canonical" href="'+url+'">\n  <meta property="og:url" content="'+url+'">\n</head>')
 page.write_text(markup)
urls=[origin+'/']+[origin+'/'+p.name for p in sorted((base/'dist').glob('*.html')) if p.name!='index.html']
(base/'dist/sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+url+'</loc></url>' for url in urls)+'</urlset>\n')
(base/'dist/robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+origin+'/sitemap.xml\n')
