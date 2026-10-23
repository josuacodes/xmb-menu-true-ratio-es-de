"""Generate the True Ratio slot and video sizes for the XMB Menu True Ratio theme.

Writes _inc/screen-ratio/ and _inc/box-ratio/ and sets <systemScreenRatio> in the
system metadata files from the CONSOLES table below. Edit the table, then run:

    python3 resources/generate-true-ratio.py
"""
import re
import shutil
import sys
from pathlib import Path

theme = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent

# Screen aspect files: (ratio, max slot width as fraction of screen width)
SCREENS = {
    "16-9": (16 / 9, 0.140),
    "16-10": (16 / 10, 0.140),
    "3-2": (3 / 2, 0.140),
    "4-3": (4 / 3, 0.140),
    "8-7": (8 / 7, 0.140),
    "1-1": (1.0, 0.140),
    "20-9": (20 / 9, 0.1116667),
}
MAX_H = 0.170  # original boxart slot height, keeps tall slots inside the layout
ITEM_SCALE = 1.9  # selected item zoom from the aspect-ratio files
# ES-DE rounds the image to whole pixels but not the video, so their edges can be
# half a pixel apart. Overscan the video by this share of the screen width
# (same pixel amount vertically) so it always covers the image edges.
VIDEO_OVERSCAN = 0.005

# Console display ratios; "screen" = same shape as the screen (mixed collections)
RATIOS = {"16-9": 16 / 9, "5-3": 5 / 3, "4-3": 4 / 3, "3-2": 3 / 2, "10-9": 10 / 9, "1-1": 1.0, "2-3": 2 / 3, "screen": None}

CONSOLES = {
    "16-9": "psp psvita switch wiiu ps3 ps4 xbox360 xboxone virtualboy steam windows epic lutris moonlight android androidapps androidgames",
    "5-3": "n3ds playdate",  # 400x240, scraped 3DS videos show the top screen only
    "3-2": "gba gbah atarilynx wonderswan wonderswancolor pokemini",
    "10-9": "gb gbh gbc gbch gamegear megaduck",
    "1-1": "ngp ngpc supervision gamate",
    "2-3": "nds",
    "screen": "auto-allgames auto-favorites auto-lastplayed custom-collections now-playing completed",
}
DEFAULT = "4-3"


def fmt(v):
    return f"{v:.7f}".rstrip("0").rstrip(".")


def slot(screen_ratio, max_w, ratio):
    r = screen_ratio if ratio is None else ratio
    w = min(max_w, MAX_H * r / screen_ratio)
    return w, w * screen_ratio / r


# 1) size variables: _inc/screen-ratio/<screen>/<console ratio>.xml
out = theme / "_inc" / "screen-ratio"
shutil.rmtree(out, ignore_errors=True)
for sname, (s, max_w) in SCREENS.items():
    d = out / sname
    d.mkdir(parents=True)
    for rname, r in RATIOS.items():
        w, h = slot(s, max_w, r)
        (d / f"{rname}.xml").write_text(
            f"""<!-- {rname} console screen on a {sname} display (generated) -->
<theme>
   <variables>
      <screenRatioItemSize>{fmt(w)} {fmt(h)}</screenRatioItemSize>
      <screenRatioVideoSize>{fmt(w * ITEM_SCALE + VIDEO_OVERSCAN)} {fmt(h * ITEM_SCALE + VIDEO_OVERSCAN * s)}</screenRatioVideoSize>
   </variables>
</theme>
"""
        )

meta = theme / "_inc" / "systems" / "_metadata-global"

# 1b) cover / cartridge slots: _inc/box-ratio/<screen>/<w-h>.xml, one per size used in the metadata
box_sizes = set()
for f in meta.glob("*.xml"):
    box_sizes |= set(re.findall(r"<system(?:Cover|Cart)Size>(\d+-\d+)</", f.read_text()))
box_out = theme / "_inc" / "box-ratio"
shutil.rmtree(box_out, ignore_errors=True)
for sname, (s, max_w) in SCREENS.items():
    d = box_out / sname
    d.mkdir(parents=True)
    for size in sorted(box_sizes):
        bw, bh = map(int, size.split("-"))
        w, h = slot(s, max_w, bw / bh)
        assert abs((w * s) / h - bw / bh) < 1e-9 and w <= max_w + 1e-9 and h <= MAX_H + 1e-9, (sname, size)
        (d / f"{size}.xml").write_text(
            f"""<!-- {size} cover or cartridge on a {sname} display (generated) -->
<theme>
   <variables>
      <boxRatioItemSize>{fmt(w)} {fmt(h)}</boxRatioItemSize>
   </variables>
</theme>
"""
        )
print("box sizes:", " ".join(sorted(box_sizes)))

# 2) per-console ratio variable in the system metadata files
assign = {"_default": DEFAULT}
for rname, names in CONSOLES.items():
    for n in names.split():
        assign[n] = rname
for name, rname in assign.items():
    f = meta / f"{name}.xml"
    if not f.exists():
        print("missing metadata file:", name)
        continue
    text = f.read_text()
    text = re.sub(r"\n\s*<systemScreenRatio>[^<]*</systemScreenRatio>", "", text)
    # first (global) <variables> block only, not the per-language ones
    text = re.sub(
        r"\n(\s*)</variables>",
        lambda m: f"\n{m.group(1)}    <systemScreenRatio>{rname}</systemScreenRatio>\n{m.group(1)}</variables>",
        text,
        count=1,
    )
    f.write_text(text)

# 3) self-check: every slot has the intended on-screen shape and fits the box
for sname, (s, max_w) in SCREENS.items():
    for rname, r in RATIOS.items():
        w, h = slot(s, max_w, r)
        assert abs((w * s) / h - (s if r is None else r)) < 1e-9, (sname, rname)
        assert w <= max_w + 1e-9 and h <= MAX_H + 1e-9, (sname, rname)
print("ok:", len(SCREENS) * len(RATIOS), "size files,", len(assign), "consoles")
