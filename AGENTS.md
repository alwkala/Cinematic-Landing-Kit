# AGENTS.md — Cinematic Luxury Landing-Page Engine

Build a **single-file, scroll-driven luxury landing page** (Apple × Cartier aesthetic) for any product using Qwen Image (stills) + Wan (video clips). This is a single-file web app (`index.html`) with CDN libraries (GSAP, Lenis, Tailwind) — no build step, no framework, no bundler.

## Critical architecture (the #1 thing)

The product "film" is a **JPG frame-sequence drawn on `<canvas>`**, scrubbed by scroll progress.
**NEVER scrub `video.currentTime`** — H.264 keyframe-seeking causes stutter. Convert videos to ~90–120 numbered JPGs (`assets/seq/f000.jpg … fNNN.jpg`) at 1280px wide, JPEG q≈80.

## Build order

1. **Decide direction** from the product + reference photos: theme (light/dark), story beats, palette. Don't ask the user to specify unless genuinely blocked.
2. **Choose a layout** from `templates/layouts/` — see the decision table there. Pick based on product type:
   - `fullbleed.html` — long scroll film, aura+motes hero (transformation stories: perfume, food, watches)
   - `editorial.html` — split-screen hero, shorter film, two-column sections (specs-heavy: furniture, auto, skincare)
   - `minimal.html` — centered hero, no canvas film, section-based (fast/lightweight: digital products, books)
3. **Scaffold**: copy the chosen template to root as `index.html`, fill `{{PLACEHOLDERS}}`, wire sections/assets. The engine is correct — wire it, don't rewrite it.
4. **Write the prompt list** from `templates/MEDIA-PROMPTS.template.md` (numbered, boundary-matched, identity + modesty clauses). Skip the film-section prompts if building from `minimal.html`.
5. **Generate assets** (see `memory/06-media-pipeline.md`): Qwen Image keyframes in parallel → Wan boundary-matched video clips (after keyframes verified) → extract frames → transparent hero cutout via `rembg`.
6. **Sync `FRAME_COUNT`** in `index.html` to the actual extracted frame count (4 clips × 24 frames − 3 duplicates = 93 is typical). Only applies to `fullbleed` and `editorial` templates.
7. **Preview locally & verify** (see "Preview & verification" below). Web-optimize heavy assets via `scripts/optimize_assets.py`.

## Non-negotiables

- **Cinematic hero**, not a static image + fade. Transparent PNG cutout (no `mix-blend-mode` — it breaks under GSAP `transform`).
- **Boundary-matched clips**: clip N end-frame == clip N+1 start-frame. Never cross-dissolve two stills.
- **Ambient `#ambient` layer** shifts color per section via GSAP tween.
- **Header** hides on scroll-down (`.hidden`), returns on scroll-up. Never removed.
- **Typography**: Arabic = El Messiri (headings) + Tajawal (body). **Never Amiri**. Captions off-center (right in RTL).
- **Modesty mandatory** for any person (full hijab, conservative). **Exact product identity** preserved across all assets.
- **Graceful fallbacks**: `prefers-reduced-motion` + missing-asset gradient on a container (not `::after` on `<img>` — `::after` doesn't render on replaced elements).

## Preview & verification

Serve: `npx -y serve -l 8123 .`

**Hidden browser tabs pause `requestAnimationFrame`** — GSAP tweens freeze, screenshots time out, bulk image preloads stall. This is the OS, not a bug. Verify via:
- `eval` in the preview: check DOM structure, `getComputedStyle`, console errors.
- Force end-states: `gsap.set('.elem', { ... })` to confirm layout.
- Drive scroll programmatically: `window.lenis.scrollTo(y, {immediate:true, force:true}); ScrollTrigger.update();` — plain `window.scrollTo` doesn't update ScrollTrigger when Lenis owns scroll.
- Position by trigger's pixel range: `st.start + progress * (st.end - st.start)`, not `offsetTop`.

## Asset pipeline (Python)

**Dependencies:** `pip install rembg pillow opencv-python dashscope`

| Script | Purpose |
|--------|---------|
| `scripts/remove_backgrounds.py` | `rembg` → transparent PNG cutouts (logo, product hero) |
| `scripts/prepare_images.py` | PNG → JPEG q=87 conversion for web |
| `scripts/optimize_assets.py` | Resize hero cutout (max 1200px), logo (max 240px) |
| `scripts/generate_transitions.py` | Generate transition keyframes |

The frame extraction recipe (no ffmpeg needed) is in `memory/06-media-pipeline.md` — uses OpenCV `VideoCapture`. Guard against empty mp4s (failed download = 0-frame file).

## Tooling constraints

- **No `jq`** — parse JSON with `grep -oE` if needed.
- **No `ffmpeg`/`ffprobe`** — use Python + OpenCV.
- `<picture>` 404 pitfall: if a matched `<source>` 404s, the `<img>` fallback does NOT render. Use a single `<img>` until responsive assets are actually generated.
- Muted autoplay: call `video.play().catch(()=>{})` on first user gesture; don't set the `loop` attribute if you rely on the `ended` event (looping elements never fire `ended`).

## Deep reference — read these before building

- `memory/02-scroll-film-canvas.md` — the canvas frame-sequence technique in detail
- `memory/04-cinematic-hero.md` — the blend-mode trap; entrance + aura + particles + 3D tilt + sheen
- `memory/05-theming.md` — light vs dark multiply/screen
- `memory/06-media-pipeline.md` — Qwen Image + Wan API patterns, frame extraction code, parallel generation
- `memory/08-preview-and-env-gotchas.md` — all the env quirks above, with full explanations
- `memory/09-quality-bar.md` — the auto-reject checklist (what gets thrown out)
