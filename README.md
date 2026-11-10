# Oakland Service Initiative website

Complete editable source for the Oakland Service Initiative website, serving Oakland County through education, hospitality, community events, and nature.

Public website: https://oaklandserviceinitiative.com/

## Preview the website

The finished website is in `dist/`. It can be served without a build step:

```sh
python3 tools/preview_site.py
```

Open http://127.0.0.1:8000 in your browser. The preview server resolves clean URLs such as `/events` to the corresponding HTML files in `dist/`.

## Edit and rebuild

- `index.template.html`: homepage, shared header, and footer.
- `*.template.html`: individual page content.
- `content.json`: impact figures, contact details, event records, and team information.
- `dist/*.css` and `dist/*.js`: styles and browser interactions. Edit the individual stylesheets and rebuild the generated `dist/site.css`.
- `dist/assets/`: photos, logos, and fonts.
- `tools/build_site.py`: generates the pages, shared stylesheet, sitemap, and robots file.
- `archive/`: earlier content retained for reference, outside the published website.

Rebuild after changing a template, stylesheet, script, or `content.json`:

```sh
python3 tools/build_site.py
```

Serve `dist/` at the domain root using a static host that maps clean URLs to their `.html` files, as on the public site. To change the canonical domain, update `origin` in `tools/build_site.py` and rebuild. The build uses Python’s standard library. The optional original-image preparation script requires Pillow and the original photos.

## Join form

The application form opens the visitor’s email app with a draft addressed to OSI. The visitor must send the email there. It does not store applications or send email from a server.

## Source snapshot

Imported from the exact source of published Site version 44, commit `9014d90f487dad906fa58810d2a30bd9c6c833ff`. Sites account credentials, repository authentication, local working files, and deployment archives are excluded. Updating this GitHub repository does not automatically update the hosted Sites website.

## Photos and branding

OSI photos, logos, and third-party partner marks retain their existing ownership. This repository does not add an open-source license or grant additional rights to those assets.
