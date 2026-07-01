import argparse
import os
import sys
from PIL import Image

TARGET_W, TARGET_H = 1280, 720

def crop_cover_16_9(img):
    """Crop-resize an image to 16:9 cover-fit (object-cover style)."""
    img = img.convert("RGB")
    img_ratio = img.width / img.height
    target_ratio = TARGET_W / TARGET_H
    if img_ratio > target_ratio:
        new_width = int(target_ratio * img.height)
        offset = (img.width - new_width) // 2
        img = img.crop((offset, 0, offset + new_width, img.height))
    else:
        new_height = int(img.width / target_ratio)
        offset = (img.height - new_height) // 2
        img = img.crop((0, offset, img.width, offset + new_height))
    return img.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate a JPEG frame-sequence from N keyframe images using eased cross-blends. "
            "Output frames are named f000.jpg, f001.jpg, … and are suitable for scrubbing on a <canvas>."
        ),
    )
    parser.add_argument(
        "--keyframes-dir",
        "-k",
        required=True,
        help="Directory containing numbered keyframe images (k1.png k2.png … or any sorted order).",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        default="assets/seq",
        help="Directory to write the output frame sequence (default: assets/seq).",
    )
    parser.add_argument(
        "--src-dir",
        help="Optional directory to save the normalised 1280x720 keyframes (default: <output-dir>/../seq-src).",
    )
    parser.add_argument(
        "--total-frames",
        "-f",
        type=int,
        default=93,
        help="Total number of output frames (default: 93).",
    )
    parser.add_argument(
        "--quality",
        "-q",
        type=int,
        default=80,
        help="JPEG quality for output frames (default: 80).",
    )
    args = parser.parse_args()

    kf_dir = args.keyframes_dir
    if not os.path.isdir(kf_dir):
        print(f"Error: keyframes directory '{kf_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    kf_files = sorted(
        f for f in os.listdir(kf_dir)
        if os.path.splitext(f)[1].lower() in {".png", ".jpg", ".jpeg", ".webp"}
    )
    if len(kf_files) < 2:
        print(f"Error: at least 2 keyframe images are required; found {len(kf_files)} in '{kf_dir}'.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.output_dir, exist_ok=True)
    src_dir = args.src_dir or os.path.join(os.path.dirname(args.output_dir), "seq-src")
    os.makedirs(src_dir, exist_ok=True)

    keyframes = []
    for i, fname in enumerate(kf_files):
        path = os.path.join(kf_dir, fname)
        img = crop_cover_16_9(Image.open(path))
        keyframes.append(img)
        dest = os.path.join(src_dir, f"k{i + 1}.jpg")
        img.save(dest, "JPEG", quality=90)
        print(f"[keyframe] {path} -> {dest}")

    n_segments = len(keyframes) - 1
    total_frames = args.total_frames
    seg_frames = total_frames // n_segments
    remainder = total_frames - seg_frames * n_segments

    frame_idx = 0
    for seg in range(n_segments):
        start_img = keyframes[seg]
        end_img = keyframes[seg + 1]
        count = seg_frames + (1 if seg < remainder else 0)
        for j in range(count):
            t = j / max(count - 1, 1)
            ease_t = t * t * (3.0 - 2.0 * t)
            blended = Image.blend(start_img, end_img, ease_t)
            dest = os.path.join(args.output_dir, f"f{frame_idx:03d}.jpg")
            blended.save(dest, "JPEG", quality=args.quality)
            frame_idx += 1

    print(f"[done] Generated {frame_idx} frames in {args.output_dir}/")

if __name__ == "__main__":
    main()
