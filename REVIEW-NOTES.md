# Oakland Service Initiative — private review

This is a fresh Sites project, separate from the existing OSI website. The original source and supplied photographs are preserved. The hosting manifest identifies the new Site; deployment remains owner-private.

## Content ready for review

The page covers the hero, mission, chronological journey, food assistance, planting, hospice volunteering, Rochester Heritage Festival, micro:bit education, partners and recognition, and contact. There is no gallery or submission form.

The user supplied 7,000 people at the largest event (added to the hero and festival story), the 2023 start, 12-event total, 5,000+ meals helped prepare or create, 300+ volunteer hours with Absolute Home Health and Hospice, more than $3,000 of plants planted, and $2,000 micro:bit fundraising goal. OSI members’ five Presidential Volunteer Service Awards and outdoorserviceinitiative@gmail.com were explicitly confirmed. The 300+ hours cover work with Absolute alone, one of OSI’s collaborators; they are not OSI’s total hours across all collaborators. Recognition does not claim issuer status. The meal total is not attributed solely to Gleaners. No fundraising progress, donation destination, nonprofit status, testimonials, or additional impact figures are claimed.

## Remaining factual details

- Meet the Team now has a dedicated page at `meet-the-team.html`, linked from the main navigation, About section, and footer on all pages. It has a text-only introduction and a founders section. Founder profiles show a coming-soon message because names, roles, biographies, and identified portraits have not been supplied. Confirmed profiles can be added to `content.json` under `team.members` with `name`, `role`, `bio`, and optionally an existing asset `image` and `alt`.

- A complete list of the 12 events, with dates and short descriptions. The current timeline shows the founding milestone and three dated service events. It does not invent missing entries or count the founding as an event. Absolute Home Health and Hospice volunteering is a 2024 timeline event, with its official logo and 300+ volunteer hours, as confirmed by the user on October 5, 2026. The overall total remains 12 events.
- The official event title and date for participation at Rochester Hills Museum at Van Hoosen Farm. It appears as a volunteering event in the timeline, with an official museum farmhouse photo; no date is assigned.
- The specific Lake Orion and Oakland Township organizations/entities and the nature of OSI’s relationship with each. These ambiguous names are withheld from the public-facing partner section pending confirmation. Rochester Hills is a separately confirmed event relationship.
- More detail on Gleaners volunteer activities, if desired. Current wording is limited to food-related service and does not assign an unverified number to that relationship.

## Sources and date decisions

- Rochester Heritage Festival, May 30–31, 2026: OSI announcement https://www.instagram.com/oaklandserviceinitiative/p/DYsmQPFpBtU/ and corresponding recap https://www.instagram.com/oaklandserviceinitiative/p/DZD7jzhjb_3/. The May 23 announcement date and June 1 recap date are not treated as event dates.
- Burgess-Shadbush Nature Center, June 19–20, 2026: OSI caption https://www.instagram.com/oaklandserviceinitiative/p/DaLNCkSEVld/. The June 29 posting date is not treated as an event date. The supplied graphic supports 500 plants in two days.
- Festival of the Hills, June 24, 2026: https://www.rochesterhills.org/thingstodo/festival_of_the_hills.php; OSI participation confirmed by the user.
- Museum participation: user confirmation; museum information https://www.rochesterhills.org/departments/parks_and_natural_resources/museum/index.php.
- Absolute Home Health and Hospice: https://absolutehhh.com/. Its official header logo was retrieved from https://absolutehhh.com/wp-content/uploads/2024/04/Untitled-1-1.png. The unnamed stethoscope graphic in the supplied assets is not mislabeled as its official logo.
- Instagram: https://www.instagram.com/oaklandserviceinitiative/, confirmed by the user and researched in the browser.
- Gleaners: https://www.gcfb.org/. User-provided relationship; linked as a food-service organization.
- Learning resource: https://learn.sparkfun.com/tutorials/getting-started-with-the-microbit/all. SparkFun is identified as the learning resource provider, not a sponsor.

## Editing

Edit `content.json` for impact figures, contact details, sources, and event entries; edit `index.template.html` for narrative and structure. CSS and menu behavior live in `dist/styles.css` and `dist/script.js`. `tools/build_site.py` renders the static HTML using the bundled Python/Pillow runtime. All complete content is in the resulting HTML; JavaScript only controls the mobile menu and optional subtle motion.

`tools/prepare_assets.py` makes separate WebP copies and sizes from the original photographs; it never overwrites originals. `dist/assets/asset-index.json` maps photographs to their sources. A copied Rochester Hills logo and the verified Absolute logo are also included. All graphics retain their original proportions. The hero and four planting action images have screenshot frames removed; festival screenshots have edge UI trimmed where it does not sacrifice subjects.

## Verification

- Browser checks at 375, 390, 768, and 1440 pixels; no horizontal overflow observed.
- Desktop hero, about composition, timeline, tablet food section, mobile planting, festival, micro:bit, and contact layouts visually inspected. All photographs have descriptive alternative text and explicit dimensions. Responsive variants and lazy loading are enabled; the hero is prioritized.
- Mobile Menu opens with Enter, closes with Escape, restores focus, and closes after section selection. Section and timeline links resolve to existing anchors; all 17 IDs are unique.
- All eight distinct external destinations returned HTTP 200. `link-check.json` records the destination checks. External Instagram access may still depend on the visitor’s session. Email links address the confirmed email; no message was sent.
- JavaScript syntax check passed. HTML audit checked 38 links, 20 described images, and presence of every local asset.
- Cream/forest text contrast: 11.11:1; ink/sage: 5.90:1; muted text/cream: 5.75:1. Sage link hover was corrected to retain adequate contrast.
- Reduced-motion CSS disables animation, transitions, and smooth scrolling; the menu and all content remain available. This was verified by source inspection, not by changing the user’s operating-system preference.

The deployment result and final browser diagnostics are reported in the handoff.

Latest design update: decorative arrows were removed from navigation, buttons, links, and the micro:bit composition. The hero now includes $3,000+ worth of plants planted and 7,000 people at the largest event, with a two-column statistics layout on mobile.

Food assistance and environmental service now have separate documents (`food-assistance.html` and `environmental-service.html`). Home shows only brief links under Our Work. The about section and planting timeline link directly to the appropriate page. Full stories, impact details, graphics, and photographs live only on those pages. Each page includes navigation back to Home/Our Work and to the other story. Older #food and #planting URLs land on the corresponding clickable preview on Home. Full story pages work without JavaScript. Story source is editable in the corresponding `.template.html` files.

Sponsors update, October 5, 2026: the Partners section now includes the seven entries from the original website’s sponsors/community-partners ribbon: BTC, Community Supporter (the unnamed medical logo), Greater Rochester Heritage Festival, International Academy, Kiwanis International, Shelby Township, and Rochester Hills, Michigan. Magna is also listed because the original site explicitly describes a funding partnership. Names and supplied logos are carried forward from components/osi-site.tsx and public/assets; BTC is not expanded and the unnamed medical logo is not attributed to Absolute. No unverified external destinations or additional funding figures were added. The original source and images are preserved.

Museum image: official Rochester Hills museum website, FarmhouseInSpring.jpg. Photo shows the museum location and is not presented as a photo of OSI volunteering.

Award image update, October 5, 2026: the recognition section now shows a web-sourced photograph of silver, gold, and bronze President’s Volunteer Service Award medals, replacing its decorative symbol. Source: American University, https://www.american.edu/student-affairs/volunteer/pvsa.cfm; original image: https://www.american.edu/student-affairs/volunteer/images/pvsa-award-medallions-3x.jpg. The unchanged photo is saved locally as dist/assets/pvsa-medallions.jpg and credited beneath the image. It illustrates the award generally and is not presented as a photograph of OSI members’ own medals. The user-confirmed total of five awards is preserved.

October 5, 2026 correction: the user identified the medical sponsor previously labeled Community Supporter as Health and Hospice. Updated the sponsor name and logo alternative text.

October 5, 2026: added BBCC volunteer partnership in 2024 with 40 hours to Events, Our Journey, and Community. Confirmed organization name and mission at https://bbcoalition.org/. Added user-confirmed 4,000 total volunteer hours to homepage impact; individual collaborator hours remain separate.

October 5, 2026: replaced BBCC text placeholder with the real group photo published on https://bbcoalition.org/about/ (https://bbcoalition.org/wp-content/uploads/2024/10/BBCC-About-1.jpg). Credited as a BBCC group photo; no claim that it depicts OSI’s specific 2024 volunteer event.


October 6, 2026 aerial update: the homepage replaces the animated plant SVG with an actual aerial photograph of downtown Pontiac, Oakland County, by Lrgjr72 (Wikimedia Commons, CC BY-SA 4.0). A slow pan/zoom loop is supplied as a GIF, with a smaller animated WebP used in the background. This is an animated still photograph, not drone footage. The same-license adaptations and source are credited in the footer and assets/oakland-county-aerial-credit.json. Pause and reduced-motion preferences use a static frame. Headline and introductory wording focus on Oakland County and all service areas. Existing impact figures and programs are preserved. Logo concepts are separate explorations, not an adopted brand replacement.

October 6, 2026 publication preparation: applied the approved Connected Community logo to navigation, footer, founding milestone, favicon, and social image metadata. Original PNG artwork is unchanged; the compact mark uses an SVG viewport of the same artwork. Added cross-document slides, normal-link fallback for browsers without native transitions, reduced-motion opt-out, per-page canonical links, sitemap, and robots file. Existing private audience is preserved.

The Team page now includes user-confirmed founders Amey Asundi, Nathaniel Lev, Kavin S, Rahul, and Christain Schneider. Names are preserved exactly; profiles use initials and Founding team labels without invented biographies or individual roles.

Publication verification: audited all ten pages for local destinations, assets, metadata, unique headings and IDs; SVG and sitemap parse; JavaScript syntax checks pass. Unit checks cover fallback page navigation, same-page anchors, external links, new tabs, downloads, page restoration, and reduced motion. Fresh browser visual QA was blocked by browser security URL policy; no alternative browser route was attempted.

November 3, 2026 update: the hero uses only the supplied festival photograph of Amey helping a child with an American flag behind them. Slideshow markup, controls, and behavior are removed. The loader uses a compact OSI mark, name, and native progress bar driven by image/font readiness. Four native disclosure cards (Education, Community, Nature, Hospitality) now follow the mission immediately. Hover opens the cards on mouse devices; native tap/click and keyboard activation remain available. Education uses the supplied micro:bit photograph, states $2,000 raised, and links schools to the confirmed OSI email. The education detail page and content.json now use the raised amount instead of a fundraising goal. Hospitality uses the verified Absolute logo and an email link for volunteer-training enquiries. Nature retains the distinction between $3,000+ worth of plants and the separate 500-plant project. Desktop and 390px layouts, disclosure content, email links, JavaScript syntax, and all local links/assets were checked.

November 3, 2026 homepage simplification: removed the Who we are section, homepage journey/timeline, PVSA recognition block, older Events/Team promo links, and all links revealed by mission/program hover panels. A complete restorable snapshot and readable inventory are kept in archive/2026-11-03-homepage-removals/, outside the published dist directory. Existing event records and all photographs remain intact. A new Events/Team page-directory section uses the user-supplied harvest-group photo for Events and a branded Team photo coming soon placeholder. Navigation formerly targeting removed sections now points to Mission or the Events page.

November 3, 2026 motion update: non-hero homepage content slides into view as sections enter the viewport; the mission retains its existing pop animation, and page-navigation slides remain enabled. The ring/dot overlay is replaced by a white arrow pointer with a short, tapering white canvas trail. The trail draws only during mouse movement and fades out within 190ms; it clears on blur, pointer exit, tab-key use, or hidden documents. Touch devices keep native behavior, and reduced-motion disables section animation and the cursor trail.

November 3, 2026 story/footer update: Why we started and the About navigation now open about.html. The user supplied the 2023 frustration about low student engagement in Oakland County’s health and community; the page presents that motivation, OSI’s mission, and three distinct service-photo cards. The cursor effect is now a soft white glow following the native pointer, with no ring/dot or canvas trail. The large homepage Get Involved area and old footer are archived in archive/2026-11-03-before-compact-footer/. A compact shared footer retains brand, navigation, email, location, Instagram, and the #involved destination on all pages.
