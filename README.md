# Oakland Service Initiative website

Complete editable source for the Oakland Service Initiative website, serving Oakland County through education, hospitality, community events, and nature.

Current website: https://oakland-service-initiative-preview.lukanatinv.chatgpt.site/

## Preview the website

The finished website is in `dist/`. It can be served without a build step:

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000 in your browser.

## Edit and rebuild

- `index.template.html`: homepage, shared header, and footer.
- `*.template.html`: individual page content.
- `content.json`: impact figures, contact details, event records, and team information.
- `dist/*.css` and `dist/*.js`: styles and browser interactions.
- `dist/assets/`: photos, logos, and fonts.
- `tools/build_site.py`: generates the pages and sitemap.
- `archive/`: earlier content retained for reference, outside the published website.

To rebuild generated HTML after changing a template or `content.json`:

```sh
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 tools/build_site.py
```

Serve `dist/` using any static web host. If moving to a different domain, update the `origin` value in `tools/build_site.py` and the absolute social image URL in `index.template.html`, then rebuild. Root-relative links assume the website is served at the domain root.

## Join form

The application form opens the visitor’s email app with a draft addressed to OSI. The visitor must send the email there. It does not store applications or send email from a server.

## Source snapshot

Imported from the exact source of published Site version 44, commit `9014d90f487dad906fa58810d2a30bd9c6c833ff`. Sites account credentials, repository authentication, local working files, and deployment archives are excluded. Updating this GitHub repository does not automatically update the hosted Sites website.

## Photos and branding

OSI photos, logos, and third-party partner marks retain their existing ownership. This repository does not add an open-source license or grant additional rights to those assets.
