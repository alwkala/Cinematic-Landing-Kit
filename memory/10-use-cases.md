# 10 · Use-Case Routing Guide

Quick decision: identify the product type + user intent → pick the layout + media strategy.

## Fit test (run this first)

1. **One clear subject?** (one product / one brand / one space / one person) → ✅ proceed. Multiple products / catalog → ❌ wrong tool.
2. **Transformation arc?** (before→after, raw→finished, outside→inside, problem→solution) → ✅ proceed. Static spec sheet → ❌ wrong tool.
3. **User in inspire mode?** (browse/dream/aspirate) → ✅ proceed. Evaluate/compare/decide mode → ❌ wrong tool.

If all three pass → cinematic kit is the right choice.

---

## Layout decision table

| Layout | File | Best for | Hero type | Film type |
|--------|------|----------|-----------|-----------|
| **fullbleed** | `fullbleed.html` | Physical goods, brand stories, rebrands, fashion, causes, artisan | Product cutout + aura + motes | Long transformation film (600vh, 4 clips) |
| **editorial** | `editorial.html` | Specs-heavy products, founders, events, conferences | Split-screen: image + copy | Shorter transformation film (420vh, 3-4 clips) |
| **minimal** | `minimal.html` | Personal brands, creators, digital products, books | Centered cutout, no aura | No film — section-based scroll |
| **spatial** | `spatial.html` | Real estate, architecture, travel, hospitality, venues | Wide establishing shot, no cutout | Spatial walkthrough film (500vh, 4-5 clips) |
| **interface** | `interface.html` | SaaS, apps, digital platforms | Device mockup (phone/laptop frame) | UI flow film (420vh, 3-4 clips) |

---

## Per-use-case specifications

### 1 · Product launches (physical goods)
**Layout:** fullbleed  
**Sections:** Hero → Film (raw→formed→branded→gallery) → Product reveal (specs grid) → Ritual/lifestyle → CTA (video + order)  
**Hero:** Product cutout with aura + motes + 3D tilt + sheen  
**Film beats:** Raw material → forming/assembly → brand mark appears → final product → gallery reveal  
**Media:** Qwen Image keyframes with ref product photo; Wan clips boundary-matched; rembg on cleanest hero shot  
**Ambient palette:** Match product. Warm neutrals for food/beauty; cool grays for tech; deep tones for luxury  
**Gotcha:** The transformation must be visually dramatic. If the raw→finished difference is subtle, skip the film → use editorial layout instead.

### 2 · Flagship brand story / positioning pages
**Layout:** fullbleed or editorial  
**Sections:** Hero → Film (heritage→problem→solution→outcome) → Origin story (text + environment image) → Values/pillars (3-column grid) → CTA  
**Hero:** Brand symbol cutout or flagship product, aura optional  
**Film beats:** Heritage/origin scene → the problem/the gap → the innovation → the result/legacy  
**Media:** Origin environment (no product needed) + product-in-context keyframes. Mix product and lifestyle imagery.  
**Ambient palette:** Shift per story beat: muted heritage → tense problem → bright resolution  
**Gotcha:** Brand stories risk feeling generic. Ground every section in a specific, concrete detail from the brand's real history.

### 3 · High-ticket single-offer sales pages
**Layout:** fullbleed  
**Sections:** Hero → Film (desire→proof→exclusivity) → Feature highlights (icon grid) → Testimonial/press → CTA (strong close)  
**Hero:** Product cutout, maximum drama — large aura, gold sheen  
**Film beats:** Aspirational lifestyle → close-up craftsmanship detail → product in premium setting → exclusive reveal  
**Media:** High production value. Every frame must scream premium. Use macro detail shots.  
**Ambient palette:** Dark theme preferred for luxury; deep blacks with gold accents  
**Gotcha:** The CTA section must be the emotional climax. Build scroll tension through the film before releasing into the ask.

### 4 · Real estate / architecture / interior showcase
**Layout:** spatial *(new)*  
**Sections:** Hero (establishing exterior) → Film (approach→entry→rooms→view) → Space details (dimensions, materials) → Neighborhood/location → CTA (tour booking)  
**Hero:** Wide architectural shot, NO product cutout. Full-bleed image with overlay text.  
**Film beats:** Approach/exterior → threshold/entry → key interior space → signature view/detail  
**Media:** Qwen Image for architectural keyframes (no ref needed — describe the space). Wan for walkthrough clips. No rembg needed.  
**Ambient palette:** Match architecture style — warm stone for Mediterranean, cool concrete for modernist, lush greens for tropical  
**Gotcha:** Spatial films need consistent camera movement (walk/dolly). No orbits or product-style rotations. The viewer is walking through, not looking at.

### 5 · Personal brand / creator persona pages
**Layout:** minimal  
**Sections:** Hero (portrait cutout, centered) → Statement (large quote) → About (two-column: story + portrait) → Work/Portfolio (grid) → CTA (connect/hire)  
**Hero:** Person cutout (modesty rules apply), centered, no aura. Clean and minimal.  
**Film:** None — section-based scroll reveals.  
**Media:** Qwen Image for lifestyle/editorial portraits. rembg for hero cutout. Photography-style prompts, not product-style.  
**Ambient palette:** Warm, approachable. Cream/paper tones. Gold accent for personal touch.  
**Gotcha:** People pages must feel human, not corporate. Avoid dramatic cinematic effects — the minimal layout's restraint IS the premium signal.

### 6 · SaaS / app launches
**Layout:** interface *(new)*  
**Sections:** Hero (device mockup) → Film (problem→UI flow→result) → Feature highlights (icon + text grid) → Integration/social proof → CTA (signup)  
**Hero:** Device frame (laptop or phone) with UI screenshot inside. Subtle float + tilt.  
**Film beats:** Problem state (empty/frustrating) → the app interface appears → key workflow in action → delighted result  
**Media:** Qwen Image for UI mockups on device screens. Wan for UI interaction clips. Clean, modern prompts — not cinematic/luxury.  
**Ambient palette:** Tech-forward — cool blues/purples, or match the app's brand colors. Dark theme common.  
**Gotcha:** UI films must show ACTUAL interaction, not abstract transformations. Each frame should be a recognizable screen state. Use device frames consistently.

### 7 · Rebrand reveals
**Layout:** fullbleed  
**Sections:** Hero → Film (old identity→transition→new identity) → Brand values → New visual system showcase → CTA  
**Hero:** New brand symbol cutout, maximum aura  
**Film beats:** Old identity dissolving → transition/abstract moment → new identity forming → new identity in context  
**Media:** Generate old identity keyframes from client brief. New identity from new brand guide. Wan clips show the metamorphosis.  
**Ambient palette:** Start in old brand colors, transition to new brand colors through the film  
**Gotcha:** The old→new transition must feel intentional and respectful of heritage, not dismissive. The film is a bridge, not a demolition.

### 8 · Premium event / conference pages
**Layout:** editorial  
**Sections:** Hero (event identity + date) → Film (anticipation build) → Speakers (card grid) → Agenda (timeline) → Venue (wide shot) → CTA (register)  
**Hero:** Split-screen: event visual + key info (date, location, tagline)  
**Film beats:** Empty venue → setup/preparation → first attendees → event in full swing  
**Media:** Venue/environment shots for keyframes. Wan clips show the space coming alive. Use event brand colors in ambient.  
**Ambient palette:** Shift per section — calm anticipation → energized speakers → warm venue glow  
**Gotcha:** Event pages have many information sections (speakers, agenda, venue). The cinematic film builds mood; the editorial grid delivers the data. Don't try to make data cinematic.

### 9 · Automotive / luxury goods
**Layout:** fullbleed  
**Sections:** Hero → Film (design→engineering→driving/experience→reveal) → Specs (performance grid) → Craftsmanship (macro details) → CTA (configure/book)  
**Hero:** Vehicle/product cutout with dramatic aura and sheen  
**Film beats:** Design sketch/concept → engineering detail (engine/material) → product in motion → product at rest in premium setting  
**Media:** Hyper-detailed automotive/product keyframes. Wan for dynamic motion clips (driving, rotating).  
**Ambient palette:** Dark/dramatic — deep blacks, chrome/silver accents, or rich racing colors  
**Gotcha:** Automotive demands photorealism that AI generation often struggles with. Use reference images heavily and verify every generated frame for accuracy.

### 10 · Luxury travel / hospitality
**Layout:** spatial *(new)*  
**Sections:** Hero (destination establishing shot) → Film (arrival→lobby→room→view) → Experience highlights (icon grid) → Dining/amenities → CTA (book)  
**Hero:** Wide destination/property shot, full-bleed, text overlay  
**Film beats:** Arrival approach (driveway/shore) → threshold/lobby → signature room/suite → the view from the room  
**Media:** Architectural/hospitality keyframes. Wan for dolly/walkthrough clips. Lush, aspirational descriptions.  
**Ambient palette:** Match destination — tropical greens/blues, desert golds, alpine cool grays  
**Gotcha:** Same as use case 4 — spatial walkthrough, not product orbit. Camera moves through spaces. Verify each frame has consistent lighting and style.

### 11 · Fashion / jewelry drops
**Layout:** fullbleed  
**Sections:** Hero → Film (material→crafting→adorned→editorial) → Collection grid → Lookbook (full-bleed images) → CTA (shop)  
**Hero:** Piece cutout with sheen + aura (especially effective for jewelry)  
**Film beats:** Raw material (fabric/metal/gem) → artisan crafting → piece being worn/adorned → editorial lifestyle moment  
**Media:** Extreme macro detail for materials. Product cutout rembg. Lifestyle with modest subjects (full hijab if applicable).  
**Ambient palette:** Match the collection mood — rose gold warmth, platinum cool, gemstone-specific  
**Gotcha:** Fashion demands the most careful modesty compliance. Any person must be conservatively dressed. Focus on the piece, not the wearer.

### 12 · Documentary / cause campaigns
**Layout:** fullbleed  
**Sections:** Hero → Film (issue→impact→solution→hope) → Impact stats (counter grid) → Stories/testimonials → CTA (donate/act)  
**Hero:** Powerful image cutout or full-bleed, depending on subject  
**Film beats:** The problem visualized → human impact close-up → the intervention → hopeful resolution  
**Media:** Documentary-style keyframes. Emotional, grounded, real. Wan for narrative clips.  
**Ambient palette:** Shift from heavy/dark (problem) to bright/hopeful (solution) through the scroll  
**Gotcha:** Cause content must earn emotional weight through specificity, not manipulation. Every section needs a concrete fact or real story, not abstract sentiment.

### 13 · Founder story pages (any brand)
**Layout:** editorial  
**Sections:** Hero (founder portrait + name) → Film (journey: origin→struggle→breakthrough→today) → Origin story (text + environment) → Vision/mission → CTA (engage)  
**Hero:** Split-screen: founder portrait + name/title/one-line  
**Film beats:** Origin place/moment → the challenge/obstacle → the breakthrough idea → today's reality  
**Media:** Editorial portraits, environment shots relevant to the origin story. Warm, human prompts.  
**Ambient palette:** Warm, grounded — matching the founder's environment/culture  
**Gotcha:** Like use case 5, founder pages must feel authentic. The cinematic treatment elevates without glamorizing. Keep the editorial grid for facts/timeline.

### 14 · Artisan / handmade product brands
**Layout:** fullbleed  
**Sections:** Hero → Film (raw material→hand-crafting→finished piece→in-context) → Process details (step-by-step grid) → Materials/origin → CTA (order custom)  
**Hero:** Handcrafted product cutout with warm aura  
**Film beats:** Raw material close-up → hands at work → piece taking shape → finished piece in its natural setting  
**Media:** Extreme macro for materials and tool marks. Process keyframes showing stages. Wan for craft clips.  
**Ambient palette:** Workshop warmth — honey ambers, natural wood tones, raw material colors  
**Gotcha:** The "making-of" narrative is the product. Every section should reinforce craft and human touch. Avoid anything that feels mass-produced or generic.

### 15 · Limited drops / countdown reveals
**Layout:** fullbleed  
**Sections:** Hero (mystery/partial reveal) → Film (building anticipation) → Countdown timer section → Feature previews (progressive reveal grid) → CTA (drop notification signup)  
**Hero:** Partial or silhouetted product cutout — build intrigue. Reduced aura.  
**Film beats:** Obscured/abstract hints → partial reveals → progressive detail → full product reveal  
**Media:** Keyframes that progressively reveal less to more. Wan clips that tease without showing everything.  
**Ambient palette:** Dark and mysterious — deep blacks with a single accent color matching the product  
**Gotcha:** The scroll itself is the countdown. Frame count and section heights must create real pacing tension. The final reveal must feel earned. Add a live countdown timer in HTML if there's a real drop date.

---

## Anti-patterns (when NOT to use this kit)

| Use case | Why it fails |
|----------|-------------|
| Multi-course catalogs / LMS pages | Needs filtering/comparison — conflicts with single-hero format |
| B2B SaaS feature/spec pages | Buyers need scannable data, not cinematic pacing |
| A/B-tested funnels | Single-file cinematic builds are heavy to iterate on |
| Low-bandwidth mobile funnels | Frame-sequence assets are too heavy for fast-conversion contexts |
| Pricing/tier decision pages | User is comparing, not being inspired |
| Multi-product storefronts | One hero = one product. Catalogs need different architecture. |

---

## Quick-pick flowchart

```
Is it ONE subject (not a catalog)?
├── NO → standard landing page, not this kit
└── YES
    │
    Is there a TRANSFORMATION or JOURNEY arc?
    ├── NO → minimal layout (personal brand, creator, digital product)
    └── YES
        │
        Is the subject a SPACE (building, venue, destination)?
        ├── YES → spatial layout
        ├── NO
        │   │
        │   Is the subject a DIGITAL INTERFACE (app, SaaS)?
        │   ├── YES → interface layout
        │   ├── NO
        │   │   │
        │   │   Does the story need LONG transformation film (600vh)?
        │   │   ├── YES → fullbleed layout
        │   │   ├── NO (shorter, or data-heavy) → editorial layout
```

---

## Per-use-case ambient palette reference

| Use case | Hero ambient | Mid-page ambient | CTA ambient |
|----------|-------------|-----------------|-------------|
| 1 · Product launch | `#FBF8F2` warm paper | `#F3EEE2` cream | `#ECE2CF` sand |
| 2 · Brand story | `#FBF8F2` heritage warm | `#E8E2D6` muted sage | `#F7F4EC` bright paper |
| 3 · High-ticket sales | `#0B0805` deep black | `#1A1410` warm dark | `#0B0805` return to dark |
| 4 · Real estate | Match exterior material stone/wood | Interior wall tone | View palette (sky/green) |
| 5 · Personal brand | `#FBF8F2` warm paper | `#F7F4EC` mist | `#FBF8F2` return |
| 6 · SaaS/app | `#0F172A` dark navy | `#1E293B` slate | `#0F172A` return to dark |
| 7 · Rebrand | Old brand primary color | Transition gradient | New brand primary color |
| 8 · Event/conference | `#0B0805` dramatic dark | `#1A1812` warm dark | `#FBF8F2` bright for CTA |
| 9 · Automotive | `#0A0A0A` pure dark | `#1A1A1A` graphite | `#0A0A0A` return |
| 10 · Travel | Destination sky/water tone | Interior warmth | View/landscape palette |
| 11 · Fashion/jewelry | Collection accent color | `#F7F4EC` neutral | Collection accent return |
| 12 · Cause/documentary | `#2C2824` heavy muted | `#4A4238` warm gray | `#FBF8F2` bright hope |
| 13 · Founder story | `#FBF8F2` warm paper | `#F3EEE2` cream | `#FBF8F2` return |
| 14 · Artisan | `#3C2E1C` workshop dark | `#6E5C4B` raw material | `#FBF8F2` finished bright |
| 15 · Limited drop | `#050505` near-black | `#0B0805` mystery dark | Accent color burst |

---

## Per-use-case typography adjustments

Most use cases use the default Arabic stack: **El Messiri** (headings) + **Tajawal** (body) + **Cormorant Garamond** (latin accents).

Adjustments by use case:
- **6 · SaaS/app**: Switch to **Inter** (body) + **Space Grotesk** (headings) + **JetBrains Mono** (code/technical). More tech-forward.
- **9 · Automotive**: Optionally add **Oswald** for spec numbers / performance data. Keep El Messiri for branding.
- **4/10 · Spatial**: Optionally add **Playfair Display** for editorial architectural descriptions alongside the Arabic stack.
- **12 · Cause**: Consider **Source Serif 4** for body text if the site is long-form editorial heavy.

When switching fonts, update the Google Fonts link in the `<head>` and the `font-family` declarations in CSS. The Latin accent font variable stays independent.

---

## Per-use-case section count guide

| Use case | Typical sections | Scroll depth | Notes |
|----------|-----------------|--------------|-------|
| 1, 3, 9, 11, 14, 15 | 5–7 sections | Deep (800vh+) | Full cinematic treatment |
| 2, 7, 12 | 5–6 sections | Medium (600vh) | Film + editorial balance |
| 8, 13 | 6–8 sections | Medium (500vh) | More info sections, shorter film |
| 4, 10 | 5–6 sections | Medium (600vh) | Spatial film + info grid |
| 5 | 4–5 sections | Shallow (300vh) | Minimal, no film |
| 6 | 5–6 sections | Medium (500vh) | UI film + feature grid |

---

## Asset count estimates

| Use case | Qwen Image stills | Wan clips | rembg cutouts | Total assets |
|----------|-------------------|-----------|---------------|-------------|
| 1 · Product launch | 8–12 | 4–5 | 1–2 | 13–19 |
| 2 · Brand story | 6–10 | 4 | 1 | 11–15 |
| 3 · High-ticket sales | 8–10 | 4–5 | 1–2 | 13–17 |
| 4 · Real estate | 8–12 | 4–5 | 0 | 12–17 |
| 5 · Personal brand | 4–6 | 0 | 1 | 5–7 |
| 6 · SaaS/app | 6–8 | 3–4 | 0 | 9–12 |
| 7 · Rebrand | 8–10 | 4 | 1 | 13–15 |
| 8 · Event | 6–8 | 3–4 | 0 | 9–12 |
| 9 · Automotive | 8–12 | 4–5 | 1 | 13–18 |
| 10 · Travel | 8–12 | 4–5 | 0 | 12–17 |
| 11 · Fashion | 10–14 | 4–6 | 1–2 | 15–22 |
| 12 · Cause | 6–8 | 4 | 0–1 | 10–13 |
| 13 · Founder | 5–7 | 3–4 | 0–1 | 8–12 |
| 14 · Artisan | 8–12 | 4–5 | 1 | 13–18 |
| 15 · Limited drop | 6–10 | 4–5 | 1 | 11–16 |
