import os
from PIL import Image

def resize_image_max_dim(path, max_dim=1000):
    if not os.path.exists(path):
        print(f"{path} not found!")
        return
    try:
        img = Image.open(path)
        w, h = img.size
        if w > max_dim or h > max_dim:
            if w > h:
                new_w = max_dim
                new_h = int(h * (max_dim / w))
            else:
                new_h = max_dim
                new_w = int(w * (max_dim / h))
            print(f"Resizing {path} from {img.size} to {(new_w, new_h)}...")
            img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
            img.save(path)
    except Exception as e:
        print(f"Error resizing {path}: {e}")

# Optimize the hero cutout
resize_image_max_dim("assets/product-cut.png", 1200)

# Optimize the logo
resize_image_max_dim("assets/logo.png", 240)
