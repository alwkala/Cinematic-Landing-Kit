import os
from PIL import Image

os.makedirs("assets", exist_ok=True)

conversions = [
    ("assets/papagendo (7).png", "assets/product-hero.jpg"),
    ("assets/papagendo (8).png", "assets/edition-1.jpg"),
    ("assets/papagendo (9).png", "assets/edition-2.jpg"),
    ("assets/papagendo (10).png", "assets/origin.jpg"), # fallback background
    ("assets/papagendo (6).png", "assets/ritual.jpg") # fallback lifestyle/ritual
]

print("Starting PNG to JPG conversions...")
for src, dest in conversions:
    if not os.path.exists(src):
        print(f"Source file {src} not found!")
        continue
    try:
        print(f"Converting {src} -> {dest}...")
        img = Image.open(src)
        # Convert to RGB mode before saving as JPEG
        rgb_img = img.convert('RGB')
        # Save as optimized JPEG
        rgb_img.save(dest, 'JPEG', quality=87)
        print(f"Saved {dest}")
    except Exception as e:
        print(f"Error converting {src}: {e}")
