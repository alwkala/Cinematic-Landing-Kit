import os
from PIL import Image, ImageChops

# Paths to the generated images
brain_dir = r"C:\Users\waels\.gemini\antigravity-ide\brain\fecac563-cfae-412f-a406-f21326b0b459"
k_files = [
    os.path.join(brain_dir, "k1_1782877929407.png"),
    os.path.join(brain_dir, "k2_1782877945610.png"),
    os.path.join(brain_dir, "k3_1782877979057.png"),
    os.path.join(brain_dir, "k4_1782878016164.png"),
    os.path.join(brain_dir, "k5_1782878093890.png")
]

# Ensure seq-src exists and save the clean keyframes there
os.makedirs("assets/seq-src", exist_ok=True)
os.makedirs("assets/seq", exist_ok=True)

# Target size for 16:9 canvas frames
W, H = 1280, 720

keyframes = []
for i, path in enumerate(k_files):
    if not os.path.exists(path):
        print(f"Warning: {path} not found!")
        continue
    img = Image.open(path).convert("RGB")
    # Crop/resize to exactly 1280x720 (16:9) object-cover style
    img_ratio = img.width / img.height
    target_ratio = W / H
    if img_ratio > target_ratio:
        # Image is wider than 16:9 -> crop sides
        new_width = int(target_ratio * img.height)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        # Image is taller than 16:9 -> crop top/bottom
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))
    
    img = img.resize((W, H), Image.Resampling.LANCZOS)
    keyframes.append(img)
    
    # Save the source keyframe in assets/seq-src
    dest_path = f"assets/seq-src/k{i+1}.jpg"
    img.save(dest_path, "JPEG", quality=90)
    print(f"Saved keyframe: {dest_path}")

# Now generate the transitions
# We want 93 frames total.
# 4 clips, transitions between:
# K1 -> K2 (24 frames: f000 to f023)
# K2 -> K3 (23 frames: f023 to f045, f023 is K2, f045 is K3) -> wait, let's write it carefully:
# Let's map each frame index to a progress ratio between keyframes
total_frames = 93
indices_per_transition = 23 # 93 frames total = 24 + 23 + 23 + 23

# We will generate frames f000 to f092
# Frame i from 0 to 92:
# which segment does it belong to?
# 0 to 23 -> segment 0 (K1 to K2)
# 23 to 46 -> segment 1 (K2 to K3)
# 46 to 69 -> segment 2 (K3 to K4)
# 69 to 92 -> segment 3 (K4 to K5)

for idx in range(total_frames):
    if idx <= 23:
        # Segment 0 (K1 to K2)
        start_img = keyframes[0]
        end_img = keyframes[1]
        t = idx / 23.0
    elif idx <= 46:
        # Segment 1 (K2 to K3)
        start_img = keyframes[1]
        end_img = keyframes[2]
        t = (idx - 23) / 23.0
    elif idx <= 69:
        # Segment 2 (K3 to K4)
        start_img = keyframes[2]
        end_img = keyframes[3]
        t = (idx - 46) / 23.0
    else:
        # Segment 3 (K4 to K5)
        start_img = keyframes[3]
        end_img = keyframes[4]
        t = (idx - 69) / 23.0
    
    # Linear interpolation/blend with a gentle ease-in-out curve
    # ease_t = 3 * t^2 - 2 * t^3
    ease_t = t * t * (3.0 - 2.0 * t)
    
    # We can also do a gentle zoom/pan
    # For segment 0: zoom in end_img slightly
    # For segment 3: zoom out start_img slightly
    # Let's keep it clean: simple blend
    blended = Image.blend(start_img, end_img, ease_t)
    
    # Save frame
    frame_path = f"assets/seq/f{idx:03d}.jpg"
    blended.save(frame_path, "JPEG", quality=80)

print(f"Generated {total_frames} transition frames successfully in assets/seq/")
