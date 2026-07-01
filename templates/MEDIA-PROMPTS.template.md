# Media Prompt List — TEMPLATE (Qwen Image + Wan)

Fill in `{{PRODUCT}}`, `{{BRAND_MARK}}`, `{{ORIGIN}}`, the palette/edge color, and the story beats.
Numbered by order of appearance. Stills generated via **Qwen Image**, video clips via **Wan**.
All assets land in `assets/` with the exact filenames the HTML expects.

## 0 · Setup
- Save the client reference(s) under ASCII names, e.g. `assets/ref-product.jpg` (and `assets/ref-detail.jpg`).
- These paths will be passed as reference images to Qwen Image on every product-related generation.

### Shared spec (paste into every product keyframe prompt)
- **Edge/background (theme-dependent, keep IDENTICAL across keyframes):**
  - Light: `Clean seamless warm off-white #FBF8F2 fading to the same paper tone at every edge and corner, soft natural daylight, gentle soft shadow.`
  - Dark: `Deep espresso near-black #0B0805 fading to pure black at every edge and corner, dramatic single warm raking light.`
- **Identity:** `Keep the exact {{PRODUCT}} identity and the {{BRAND_MARK}} unchanged.` (And: keep the mark where it really lives — on packaging vs on the product.)
- **Always:** `editorial luxury, hyper-detailed, no extra text, no watermark.`

---

## A · The transformation film (keyframes P1→P5 + clips V1→V4) — boundary-matched
> Beat list (edit to your product): raw/plain {{PRODUCT}} → it forms/assembles → the {{BRAND_MARK}} appears → final product → gallery reveal.

- **P1 / K1** — `assets/seq-src/k1.jpg` — **Qwen Image** with ref image, 16:9 — *plain {{PRODUCT}}, hero pose.* + shared spec.
- **P2 / K2** — `assets/seq-src/k2.jpg` — **Qwen Image** with ref image, 16:9 — *{{PRODUCT}} front-facing, centred.*
- **P3 / K3** — `assets/seq-src/k3.jpg` — **Qwen Image** with ref image, 16:9 — *the transition state (forming / blank packaging).*
- **P4 / K4** — `assets/seq-src/k4.jpg` — **Qwen Image** with ref image, 16:9 — *the FINISHED product with the {{BRAND_MARK}} in place.* (Often just the real reference, copied.)
- **P5 / K5** — `assets/seq-src/k5.jpg` — **Qwen Image** with ref image, 16:9 — *final product on a pedestal in a soft gallery (reveal).*
- **V1** `assets/v1.mp4` — **Wan** image-to-video — start-image k1, end-image k2 — *slow orbit. Locked, slow motion, no cuts, no flicker.*
- **V2** `assets/v2.mp4` — **Wan** image-to-video — start-image k2, end-image k3 — *the form/assembly beat.*
- **V3** `assets/v3.mp4` — **Wan** image-to-video — start-image k3, end-image k4 — *the {{BRAND_MARK}} materializes (where it really lives).*
- **V4** `assets/v4.mp4` — **Wan** image-to-video — start-image k4, end-image k5 — *pull back to the gallery.*
- All clips: aspect ratio 16:9, 1080p, ~5 seconds, high bitrate, no audio.
- Then extract → `assets/seq/f000.jpg…` (OpenCV, drop duplicate boundary frames) and set `FRAME_COUNT` in the HTML.

## B · Section stills
- **P6** — `assets/origin.jpg` — **Qwen Image** (no ref needed), 16:9 — *{{ORIGIN}} environment, no product.*
- **P7** — `assets/product-hero.jpg` — **Qwen Image** with ref image, 4:3/4:5 — *the product hero on the theme ground.* (Or use the real reference.)
- **P8 (opt)** — `assets/macro.jpg` — **Qwen Image** with ref image — *extreme macro detail.*
- **P9** — `assets/ritual.jpg` — **Qwen Image** with ref image, 16:9 — *lifestyle moment.* **If a woman appears: full hijab, conservative long sleeves, only face & hands (mandatory).** Realistic product scale.
- **P11/P12** — `assets/edition-1.jpg`, `assets/edition-2.jpg` — **Qwen Image** with ref image, re-skins/variants, keep the {{BRAND_MARK}}.

## C · Hero cutout + nav logo
- **CUT** — `assets/product-cut.png` — Run `rembg` + `Pillow` on the cleanest product/hero shot → transparent PNG for the hero (no blend trick).
  ```python
  from rembg import remove; from PIL import Image
  out = remove(Image.open("assets/product-hero.jpg")); out.save("assets/product-cut.png")
  ```
- **P13 (opt)** — `assets/logo.png` — **Qwen Image**: *"ONLY the {{BRAND_MARK}}, flat, on pure black/white"* → then `rembg` to remove background → transparent nav logo.

## D · CTA + lifestyle video
- **V5** — `assets/cta.mp4` — **Wan** image-to-video — start-image k4, end-image k4 (seamless loop) — *the product rotating slowly.* Poster = `assets/product-hero.jpg`.
- **V6** — `assets/life1.mp4` — **Wan** image-to-video — start-image ritual.jpg — *subtle modest lifestyle motion.*

---

### Run notes
- Call Qwen Image with `prompt="..."`, reference images as your API specifies, and save to `assets/` with the filename the HTML expects.
- Call Wan image-to-video with keyframe images as start/end frames, and save to `assets/` with the filename the HTML expects.
- Generate Qwen Image stills in parallel (multiple calls). Wan video calls depend on keyframes — run them after all Qwen Image keyframes are done and verified.
- **Verify every asset by viewing it** (identity, modesty, mark placement, scale) before making video from it.
