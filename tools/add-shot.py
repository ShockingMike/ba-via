"""Add a screen screenshot to the tracker.

Usage (from the repo root):
    python tools/add-shot.py <screen-id> <image> [<image> ...]

Saves compressed copies as shots/<id>.jpg, shots/<id>-2.jpg, ... (about 420 px wide),
which the tracker page shows as thumbnails for that screen. Old shots for the id are replaced.
"""
import sys
from pathlib import Path

from PIL import Image

root = Path(__file__).resolve().parent.parent
shots = root / "shots"


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    sid, images = sys.argv[1], sys.argv[2:]
    shots.mkdir(exist_ok=True)
    for old in list(shots.glob(f"{sid}.jpg")) + list(shots.glob(f"{sid}-*.jpg")):
        old.unlink()
    for i, src in enumerate(images):
        im = Image.open(src).convert("RGB")
        w = 420
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        name = f"{sid}.jpg" if i == 0 else f"{sid}-{i + 1}.jpg"
        im.save(shots / name, "JPEG", quality=82, optimize=True, progressive=True)
        print(f"shots/{name}")


if __name__ == "__main__":
    main()
