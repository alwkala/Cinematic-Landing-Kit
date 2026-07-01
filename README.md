# Cinematic Landing Kit

A context-and-memory package that instructs **any AI coding agent** to produce
scroll-driven, cinematic product landing pages — the kind that feel like a
luxury TV ad, not a website.  One HTML file, CDN libraries, zero build step.

```
AI agent reads AGENTS.md  →  follows memory/  →  produces index.html  →  done.
```

Works with Claude Code, Codex, Cursor, Kilo, Windsurf, Roo Code, and any agent
that auto-reads project-level instruction files.

---

## Quick start

```bash
# 1 — Copy into your project root (next to your code):
cp -r AGENTS.md memory/ templates/ scripts/   /path/to/your-project/

# 2 — Tell your AI agent:
"Build a cinematic luxury landing page for [product].
  Reference photos are in assets/. Follow AGENTS.md."

# 3 — Preview:
npx -y serve -l 8123 .
```

That's it. The agent reads `AGENTS.md`, follows the build order, and produces a
working `index.html` on the first attempt.

---

## What's inside

```
├── AGENTS.md                         ← entry point any agent reads automatically
├── memory/                           ← 10 reference files (the "DNA" of the look)
│   ├── 01-build-playbook.md             page structure, Lenis + GSAP motion stack
│   ├── 02-scroll-film-canvas.md         ★ canvas frame-sequence technique
│   ├── 03-seamless-transitions.md       boundary-matched video clips
│   ├── 04-cinematic-hero.md             hero entrance, tilt, sheen, cutout
│   ├── 05-theming.md                    light/dark themes, the blend-mode trap
│   ├── 06-media-pipeline.md             Qwen Image + Wan API, frame extraction
│   ├── 07-modesty-and-identity.md       non-negotiable constraints on people/products
│   ├── 08-preview-and-env-gotchas.md    hidden-tab quirks, eval-based verification
│   ├── 09-quality-bar.md                what gets auto-rejected
│   └── 10-use-cases.md                  ★ use-case routing: 15 use cases → layout + beats + media
├── templates/
│   ├── layouts/                       ← choose one layout variant per project
│   │   ├── fullbleed.html                long scroll film + aura hero (1,2,3,7,9,11,12,14,15)
│   │   ├── editorial.html                split-screen hero + shorter film (2,8,13)
│   │   ├── spatial.html                  establishing-shot hero + walkthrough film (4,10)
│   │   ├── interface.html                device mockup hero + UI-flow film (6)
│   │   ├── minimal.html                  centered hero, no canvas film (5)
│   │   └── README.md                     decision tree: which template for which product
│   ├── MEDIA-PROMPTS.template.md      ← numbered prompt list + per-use-case beat variants
│   └── launch.json                    ← preview-server config
└── scripts/                          ← Python helpers (no ffmpeg/jq required)
    ├── remove_backgrounds.py            rembg → transparent cutouts
    ├── prepare_images.py                PNG → JPEG conversion
    ├── optimize_assets.py               resize hero cutout + logo for web
    ├── generate_transitions.py          transition keyframes
    ├── check_alpha.py                   verify PNG transparency
    ├── create_mock_videos.py            generate placeholder clips
    └── inspect_images.py                inspect image properties
```

---

## Requirements

| Tool | Why | Install |
|------|-----|---------|
| Node.js | `npx serve` for preview | Any modern version |
| Python 3.8+ | asset pipeline scripts | Any 3.8+ |
| `rembg` | transparent cutouts | `pip install rembg` |
| `Pillow` | image resize/convert | `pip install Pillow` |
| `opencv-python` | frame extraction (replaces ffmpeg) | `pip install opencv-python` |
| `dashscope` *(optional)* | Qwen Image + Wan API calls | `pip install dashscope` |

One-shot install:

```bash
pip install rembg Pillow opencv-python dashscope
```

---

## Stack

The output is a **single `index.html`** — no build, no bundler, no framework.

| Layer | Technology | Source |
|-------|-----------|--------|
| Scroll engine | Lenis 1.0 | CDN |
| Animation | GSAP 3.12 + ScrollTrigger | CDN |
| Styling | Tailwind CSS | CDN |
| Typography | Google Fonts (El Messiri, Tajawal) | CDN |
| Film | `<canvas>` + JPG frame sequence | local assets |
| Hero cutout | transparent PNG (rembg) | local assets |

Visual assets are generated via **Qwen Image** (stills) and **Wan** (video
clips) — typically through DashScope or Alibaba Cloud Bailian. Any model that
supports image-to-image and image-to-video can substitute.

---

## Layouts & supported use cases

Five layout variants cover 15 distinct use cases. The agent reads the use-case
routing guide (`memory/10-use-cases.md`) to pick the right layout automatically.

| Layout | Hero treatment | Film | Use cases |
|--------|---------------|------|-----------|
| `fullbleed` | Product cutout + aura + motes | Long transformation (640vh) | Product launches, high-ticket sales, rebrands, automotive, fashion, causes, artisan, limited drops |
| `editorial` | Split-screen (image + copy) | Shorter film (420vh) | Brand stories, events/conferences, founder pages |
| `spatial` | Full-bleed establishing shot | Spatial walkthrough (500vh) | Real estate, architecture, luxury travel, hospitality |
| `interface` | Device mockup (CSS frame) | UI flow film (420vh) | SaaS launches, app launches, digital platforms |
| `minimal` | Centered cutout, no aura | No film | Personal brands, creators, digital products |

**Fit test:** one clear subject + transformation arc + user in inspire mode → cinematic kit.
Multi-product catalogs, spec comparison pages, and A/B-tested funnels → standard landing page.

---

## What the agent knows before it starts

These are the hard-won lessons encoded in `memory/` — the things agents
typically get wrong on the first attempt without guidance:

- **Never scrub `video.currentTime`** — the scroll "film" is a canvas frame
  sequence, not a video element. H.264 seeking stutters.
- **Never use `mix-blend-mode`** on animated elements — it breaks under GSAP
  transforms. Use transparent PNG cutouts instead.
- **Never cross-dissolve two stills** — seamless transitions require
  boundary-matched video clips.
- **Sync `FRAME_COUNT`** in the HTML to the actual extracted frame count.
- **Hidden browser tabs pause `requestAnimationFrame`** — verify via `eval`,
  not screenshots.
- **Arabic typography:** El Messiri (headings) + Tajawal (body). Never Amiri.
- Modesty is mandatory for any human subject. Product identity is preserved
  exactly across all generated assets.
- Layout-specific heroes: `fullbleed`/`editorial`/`minimal` use a transparent
  PNG cutout. `spatial` uses a full-bleed establishing shot. `interface` uses
  a CSS device mockup frame — no cutout needed for either.

---

## How it works

```
  reference photo + product brief
           │
           ▼
  ┌─────────────────────┐
  │  AI agent reads      │
  │  AGENTS.md           │
  │  + memory/ files     │
  │  (inc. 10-use-cases) │
  └─────────┬───────────┘
            │
            ▼
  pick layout: fullbleed | editorial
               spatial   | interface
               minimal
            │
            ▼
  templates/layouts/*.html  ←  scaffold, fill placeholders
            │
            ▼
  Qwen Image keyframes  →  Wan video clips
            │                    │
            └──────┬─────────────┘
                   ▼
        opencv frame extraction
        → assets/seq/f000.jpg … fNNN.jpg
                   │
                   ▼
        rembg → hero cutout (not needed for spatial/interface)
                   │
                   ▼
             index.html  (served via npx serve)
```

---

## Preview

```bash
npx -y serve -l 8123 .
```

Open `http://localhost:8123` in a **visible** browser tab. Hidden or
backgrounded tabs pause `requestAnimationFrame`, which freezes GSAP tweens and
breaks visual testing. See `memory/08-preview-and-env-gotchas.md` for the
full verification workflow.

---

## Contributing

If you find a gotcha that isn't in `memory/` yet, add it. The value of this
kit grows with every hard-won lesson captured here instead of forgotten.

## Credits

Built from real production experience. Created by
[alwkala](https://github.com/alwkala). Use freely.
