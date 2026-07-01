import argparse
import os
import sys
from PIL import Image

def resize_image_max_dim(path, max_dim, output=None):
    if not os.path.exists(path):
        print(f"[skip] {path} not found")
        return
    try:
        img = Image.open(path)
        w, h = img.size
        if w <= max_dim and h <= max_dim:
            print(f"[ok]   {path} already within {max_dim}px ({w}x{h})")
            return
        if w > h:
            new_w = max_dim
            new_h = int(h * (max_dim / w))
        else:
            new_h = max_dim
            new_w = int(w * (max_dim / h))
        print(f"[resize] {path}  {w}x{h} -> {new_w}x{new_h}")
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        dest = output or path
        img.save(dest)
        print(f"[saved] {dest}")
    except Exception as e:
        print(f"[error] {path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Resize images so their largest dimension does not exceed a given pixel limit. "
                    "Overwrites in place unless --output is specified.",
    )
    parser.add_argument(
        "inputs",
        nargs="*",
        help="Image file paths. Each can be followed by a colon and a max-dim value "
             "(e.g. assets/logo.png:240). If no colon value is given, --max-dim is used.",
    )
    parser.add_argument(
        "--max-dim",
        type=int,
        default=1200,
        help="Default max dimension in pixels (default: 1200)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional output path (only valid when a single input is given)",
    )
    args = parser.parse_args()

    if not args.inputs:
        parser.print_help()
        sys.exit(0)

    if args.output and len(args.inputs) > 1:
        parser.error("--output can only be used with a single input file")

    for spec in args.inputs:
        if ":" in spec and not os.path.exists(spec):
            parts = spec.rsplit(":", 1)
            path, dim_str = parts[0], parts[1]
            try:
                dim = int(dim_str)
            except ValueError:
                dim = args.max_dim
        else:
            path = spec
            dim = args.max_dim
        resize_image_max_dim(path, dim, output=args.output if len(args.inputs) == 1 else None)

if __name__ == "__main__":
    main()
