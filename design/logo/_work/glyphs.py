import json, sys
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
out = {}
for key, path, axes in (("baloo800", "font/Baloo2.ttf", dict(wght=800)), ("baloo700", "font/Baloo2.ttf", dict(wght=700)), ("bvp700", "font/BeVietnamPro-Bold.ttf", None)):
    f = TTFont(path)
    if axes: f = instantiateVariableFont(f, axes)
    gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
    d = dict(upm=upm, asc=f["hhea"].ascent, desc=f["hhea"].descent, xh=getattr(f["OS/2"], "sxHeight", 0), cap=getattr(f["OS/2"], "sCapHeight", 0), g={})
    for ch in "TaNhoạỏẠỎtnAOH":
        gn = cmap.get(ord(ch))
        if not gn: print("missing", key, ch); continue
        pen = SVGPathPen(gs); tp = TransformPen(pen, (1, 0, 0, -1, 0, 0)); gs[gn].draw(tp)
        bp = BoundsPen(gs); gs[gn].draw(bp)
        d["g"][ch] = dict(d=pen.getCommands(), adv=gs[gn].width, b=bp.bounds)
    out[key] = d
    print(key, upm, d["xh"], d["cap"], {k: (v["adv"], [round(x) for x in v["b"]]) for k, v in d["g"].items()})
json.dump(out, open("glyphs.json", "w", encoding="utf8"), ensure_ascii=False)
