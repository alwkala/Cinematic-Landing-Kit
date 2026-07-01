"""Shared utilities for the Cinematic Landing Kit asset pipeline."""

import re
from PIL import Image


def crop_cover_16_9(img: Image.Image, target_w: int = 1280, target_h: int = 720) -> Image.Image:
    """Crop-resize an image to a target 16:9 frame (object-cover style)."""
    img = img.convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if img_ratio > target_ratio:
        new_width = int(target_ratio * img.height)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))
    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)


_NATURAL_SORT_RE = re.compile(r"(\d+)")


def natural_sort_key(s: str):
    """Sort key for filenames with embedded numbers.

    'k2.jpg' sorts before 'k10.jpg', matching human expectations.
    """
    parts = _NATURAL_SORT_RE.split(s)
    return [int(p) if p.isdigit() else p.lower() for p in parts]
