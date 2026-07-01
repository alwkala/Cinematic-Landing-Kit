import os
from PIL import Image

brand_dir = 'brand-images'
files = [f for f in os.listdir(brand_dir) if f.endswith('.png') or f.endswith('.jpg')]

print("Image Inspection:")
for file in files:
    path = os.path.join(brand_dir, file)
    try:
        with Image.open(path) as img:
            print(f"- {file}: {img.size} (Format: {img.format}, Mode: {img.mode})")
    except Exception as e:
        print(f"- {file}: Error {e}")
