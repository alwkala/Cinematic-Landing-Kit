import os
from PIL import Image

brand_dir = 'brand-images'
files = [
    'papagendo (1).png',
    'papagendo (10).png',
    'papagendo (6).png',
    'PapaGendo-logo.png'
]

print("Alpha Channel Check:")
for file in files:
    path = os.path.join(brand_dir, file)
    if not os.path.exists(path):
        print(f"- {file} does not exist")
        continue
    try:
        with Image.open(path) as img:
            if img.mode == 'RGBA':
                # Check if there is any transparency (alpha < 255)
                alpha = img.split()[3]
                extrema = alpha.getextrema()
                print(f"- {file}: RGBA. Alpha range: {extrema}. Has transparency: {extrema[0] < 255}")
            else:
                print(f"- {file}: {img.mode}. No alpha channel.")
    except Exception as e:
        print(f"- {file}: Error {e}")
