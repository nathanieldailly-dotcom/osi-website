from pathlib import Path
from html import escape
from hashlib import sha256
import json,re
base=Path(__file__).resolve().parents[1]
dist = base / 'dist'
origin = 'https://oaklandserviceinitiative.com'
site_name = 'Oakland Service Initiative'
social_image = origin + '/assets/osi-social.jpg'
home_title = 'Oakland Service Initiative | Oakland County Volunteer Programs'
home_description = 'Volunteer with Oakland Service Initiative in Oakland County, Michigan. Explore micro:bit education, food assistance, health and hospice volunteering, and local planting projects.'

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
 link, label = {
  'medical': ('/medical', 'Explore health and hospice volunteering'),
  'food': ('/food-assistance', 'Explore food assistance'),
  'environment': ('/environmental-service', 'See the planting project'),
 }.get(category, (e.get('link'), e.get('label')))
 links = []
 if link:
  links.append((link, label))
 if e.get('link', '').startswith('https://') and e['link'] != link:
  links.append((e['link'], e['label']))
 event_links = []
 for url, text in links:
  external = ' target="_blank" rel="noopener noreferrer"' if url.startswith('https://') else ''
  event_links.append(f'<a class="text-link" href="{escape(url, quote=True)}"{external}>{escape(text)}</a>')
 actions = '<div class="event-links">' + ''.join(event_links) + '</div>' if event_links else ''
 visual=img(e['image'],e['alt']) if e.get('image') else '<strong>BBCC</strong><span>Birmingham Bloomfield<br>Community Coalition</span>'
 if e.get('imageCreditUrl'): visual+=f'<p class="image-credit">{escape(e["imageCredit"])} · <a href="{escape(e["imageCreditUrl"],quote=True)}" target="_blank" rel="noopener noreferrer">Source: BBCC</a></p>'
 event_cards.append(f'<article id="{e["id"]}" class="directory-event" data-category="{category}"><div class="directory-photo {"bbcc-photo" if e["id"]=="bbcc-event" else "logo-photo" if e.get("image") in ["city","absolute-logo","international-academy-logo"] else ""}">{visual}</div><div class="directory-copy"><p class="eyebrow">{escape(e.get("date") or "Date not recorded")} / {category.title()}</p><h2>{escape(e["title"])}</h2><p>{escape(e["description"])}</p>{actions}</div></article>')
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
 assert '{{' not in markup, 'Unresolved page template placeholder'
 return markup
# Keep the cascade in the same order while serving one cacheable stylesheet.
style_sources = (
 'styles', 'fonts', 'motion', 'collective', 'aerial', 'publish', 'welcome',
 'navigation', 'hero-glass', 'program-cards', 'page-directory', 'origin', 'join',
)
styles = '\n'.join((dist / f'{name}.css').read_text(encoding='utf-8').rstrip() for name in style_sources) + '\n'
(dist / 'site.css').write_text(styles, encoding='utf-8')

def versioned_asset(name):
 digest = sha256((dist / name).read_bytes()).hexdigest()[:12]
 return f'/{name}?v={digest}'

def metadata(title, description, path):
 url = origin + path
 page_type = {'/about': 'AboutPage', '/events': 'CollectionPage'}.get(path, 'WebPage')
 graph = [{
  '@type': page_type,
  '@id': url + '#webpage',
  'url': url,
  'name': title,
  'description': description,
  'inLanguage': 'en',
  'isPartOf': {'@id': origin + '/#website'},
 }]
 if path == '/':
  graph.extend([
   {'@type': 'WebSite', '@id': origin + '/#website', 'url': url, 'name': site_name,
    'alternateName': 'OSI', 'publisher': {'@id': origin + '/#organization'}},
   {'@type': 'Organization', '@id': origin + '/#organization', 'url': url, 'name': site_name,
    'alternateName': 'OSI', 'logo': origin + '/assets/osi-community-green-mark.webp',
    'email': data['contact']['email'], 'sameAs': [data['contact']['instagram']],
    'areaServed': {'@type': 'AdministrativeArea', 'name': 'Oakland County, Michigan'}},
  ])
 schema = json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)
 schema = schema.replace('<', r'\u003c')
 title, description = escape(title, quote=True), escape(description, quote=True)
 return f'''<title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{site_name}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{social_image}">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="800">
  <meta property="og:image:alt" content="Oakland Service Initiative green community logo">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <meta name="twitter:image" content="{social_image}">
  <meta name="twitter:image:alt" content="Oakland Service Initiative green community logo">
  <script type="application/ld+json">{schema}</script>'''

def page_head(template, title, description, path):
 scripts = ['script.js', 'motion.js']
 if path in ('/', '/about'):
  scripts.append('mission.js')
 if path == '/':
  scripts.extend(['join.js', 'program-cards.js'])
 tags = {
  'metadata': metadata(title, description, path),
  'styles': f'<link rel="stylesheet" href="{versioned_asset("site.css")}">',
  'scripts': '\n  '.join(f'<script defer src="{versioned_asset(name)}"></script>' for name in scripts),
 }
 for name, value in tags.items():
  template = template.replace('{{' + name + '}}', value)
 return template

stories = [
 ('about', 'Why We Started', 'Our Oakland County Mission', '/#work', 'Our Programs', 'Discover why Oakland Service Initiative began in 2023 and how education, hospitality, and nature guide its work in Oakland County.'),
 ('education', 'Education', 'Micro:bit Robotics Education', '/community', 'Explore Community', 'Explore hands-on robotics and programming with BBC micro:bits, and learn how Oakland County schools can participate with Oakland Service Initiative.'),
 ('community', 'Community', 'Oakland County Community Service', '/events', 'Explore Events', 'Discover Oakland Service Initiative’s food assistance, local planting projects, and community partnerships, including the Rochester Heritage Festival.'),
 ('medical', 'Medical', 'Health & Hospice Volunteering', '/events', 'Explore Events', 'Learn about Oakland Service Initiative’s work with Absolute Home Health and Hospice and how to request volunteer training information.'),
 ('events', 'Events', 'Volunteer Events & Projects', '/#program-pages', 'Events & Team', 'Explore Oakland Service Initiative’s community festivals, food assistance, environmental projects, and health and hospice volunteering.'),
 ('community-events', 'Community Events', 'Rochester Heritage Festival', '/events', 'Explore Events', 'See how Oakland Service Initiative volunteers shared hands-on planting activities at the Rochester Heritage Festival on May 30–31, 2026.'),
 ('food-assistance', 'Food Assistance', 'Food Assistance & Harvest Volunteering', '/environmental-service', 'Explore Environmental Service', 'Learn about Oakland Service Initiative’s food assistance through harvesting and volunteering with Gleaners to support the local community.'),
 ('environmental-service', 'Environmental Service', 'Environmental Service & Planting', '/food-assistance', 'Explore Food Assistance', 'See how Oakland Service Initiative volunteers added 500 plants at Burgess-Shadbush Nature Center in two days and protected the new plantings.'),
 ('meet-the-team', 'Meet the Team', 'Meet the Team', '/#involved', 'Get Involved', 'Meet the founders, leadership, and volunteers behind Oakland Service Initiative’s community service in Oakland County.'),
]
home = page_head(source_template, home_title, home_description, '/')
(dist / 'index.html').write_text(render(home), encoding='utf-8')

for slug, label, title, next_url, next_label, description in stories:
 path = '/' + slug
 metadata_head = page_head(head, title + ' | ' + site_name, description, path)
 story = (base / (slug + '.template.html')).read_text(encoding='utf-8')
 page_header = home_navigation(header)
 if slug in ('meet-the-team', 'events', 'about'):
  page_header = page_header.replace(f'href="{path}"', f'href="{path}" aria-current="page"')
 breadcrumb_link = '<a href="/#mission">Our mission</a>' if slug == 'meet-the-team' else '<a href="/#work">Our Work</a>'
 breadcrumb = '' if slug == 'about' else f'<nav class="wrap detail-breadcrumb" aria-label="Breadcrumb">{breadcrumb_link}<span aria-hidden="true">/</span><span aria-current="page">{label}</span></nav>'
 next_links = '' if slug in ('meet-the-team', 'about') else f'<div class="wrap detail-next"><a class="button green" href="/#work">Back to Our Work</a><a class="text-link" href="{next_url}">{next_label}</a></div>'
 body_class = 'detail-page story-page' if slug == 'about' else 'detail-page'
 main_class = 'detail-main about-main' if slug == 'about' else 'detail-main'
 page = (
  metadata_head + f'<body class="{body_class}"><a class="skip-link" href="#main">Skip to content</a>'
  + page_header + f'<main id="main" class="{main_class}" tabindex="-1">'
  + breadcrumb + story + next_links + '</main>' + home_navigation(footer) + '</body></html>'
 )
 (dist / (slug + '.html')).write_text(render(page), encoding='utf-8')

urls = [origin + '/'] + [origin + '/' + slug for slug, *_ in sorted(stories)]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += ''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls)
(dist / 'sitemap.xml').write_text(sitemap + '</urlset>\n', encoding='utf-8')
(dist / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {origin}/sitemap.xml\n', encoding='utf-8')
print(f'Built {len(urls)} static pages, site.css, sitemap.xml, and robots.txt.')
