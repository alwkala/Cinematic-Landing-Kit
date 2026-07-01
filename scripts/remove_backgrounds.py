import os
import sys

try:
    from rembg import remove
    from PIL import Image
except ImportError:
    print("Dependencies not met yet. Install rembg and pillow first.")
    sys.exit(1)

os.makedirs("assets", exist_ok=True)

# File lists
tasks = [
    ("assets/PapaGendo-logo.png", "assets/logo.png"),
    ("assets/papagendo (1).png", "assets/papagendo_1_cut.png"),
    ("assets/papagendo (6).png", "assets/papagendo_6_cut.png"),
    ("assets/papagendo (10).png", "assets/papagendo_10_cut.png"),
]

print("Starting background removal...")
for src, dest in tasks:
    if not os.path.exists(src):
        print(f"Skipping {src} (not found)")
        continue
    try:
        print(f"Removing background from {src} -> {dest}...")
        img = Image.open(src)
        out = remove(img)
        out.save(dest)
        print(f"Saved {dest}")
    except Exception as e:
        print(f"Error processing {src}: {e}")

# Copy default hero cut
if os.path.exists("assets/papagendo_1_cut.png"):
    try:
        import shutil
        shutil.copy("assets/papagendo_1_cut.png", "assets/product-cut.png")
        print("Copied papagendo_1_cut.png as default product-cut.png")
    except Exception as e:
        print(f"Error copying hero cutout: {e}")

# Also copy an original to product-hero.jpg
if os.path.exists("assets/papagendo (7).png"):
    try:
        import shutil
        shutil.copy("assets/papagendo (7).png", "assets/product-hero.jpg")
        print("Copied papagendo (7).png as default product-hero.jpg")
    except Exception as e:
        print(f"Error copying product-hero: {e}")
