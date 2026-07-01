import os
import cv2
import numpy as np
from PIL import Image

os.makedirs("assets", exist_ok=True)

def create_dolly_zoom_video(img_path, dest_path, duration=3, fps=24, zoom_range=(1.0, 1.08)):
    if not os.path.exists(img_path):
        print(f"Source {img_path} not found!")
        return False
    
    img = Image.open(img_path).convert("RGB")
    W, H = 1280, 720
    
    # Crop to 16:9 first
    img_ratio = img.width / img.height
    target_ratio = W / H
    if img_ratio > target_ratio:
        new_width = int(target_ratio * img.height)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))
    
    img = img.resize((W, H), Image.Resampling.LANCZOS)
    img_np = np.array(img)
    
    # Initialize VideoWriter (using 'avc1' or 'mp4v' codec)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(dest_path, fourcc, fps, (W, H))
    
    total_frames = duration * fps
    for i in range(total_frames):
        # Calculate scale factor (slow zoom-in)
        t = i / float(total_frames - 1)
        # Ease in-out
        ease_t = t * t * (3.0 - 2.0 * t)
        scale = zoom_range[0] + (zoom_range[1] - zoom_range[0]) * ease_t
        
        # Apply zoom using PIL
        new_w, new_h = int(W * scale), int(H * scale)
        zoomed = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        
        # Crop back to WxH from center
        left = (new_w - W) // 2
        top = (new_h - H) // 2
        cropped = zoomed.crop((left, top, left + W, top + H))
        
        frame = np.array(cropped)
        # Convert RGB to BGR for OpenCV
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame_bgr)
        
    out.release()
    print(f"Saved mock video to {dest_path}")
    return True

# Create the two MP4 files required by the playlist
create_dolly_zoom_video("assets/product-hero.jpg", "assets/cta.mp4", duration=3, zoom_range=(1.0, 1.06))
create_dolly_zoom_video("assets/ritual.jpg", "assets/life1.mp4", duration=4, zoom_range=(1.0, 1.05))
