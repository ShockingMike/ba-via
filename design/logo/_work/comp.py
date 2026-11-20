# -*- coding: utf8 -*-
"""felt icon composites: render RGBA on an iOS-style ground, all sizes."""
from PIL import Image, ImageDraw, ImageFilter
import sys
def hexrgb(h): h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
def mask(n, ss=4):
    m = Image.new("L", (n*ss, n*ss), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, n*ss-1, n*ss-1), radius=n*ss*0.2237, fill=255)
    return m.resize((n, n), Image.LANCZOS)
def felt_icon(src, ground, scale, dx=0, dy=0, n=1024, glow=None):
    """scale: object bbox width as fraction of icon; dx,dy offset of bbox centre from icon centre (fraction)"""
    im = Image.open(src).convert("RGBA"); bb = im.getbbox(); im = im.crop(bb)
    k = scale * n / im.width; im = im.resize((round(im.width*k), round(im.height*k)), Image.LANCZOS)
    g = Image.new("RGBA", (n, n), hexrgb(ground) + (255,))
    if glow:
        gl = Image.new("RGBA", (n, n), (0, 0, 0, 0)); d = ImageDraw.Draw(gl); r = n*0.46
        d.ellipse((n/2-r, n*0.47-r, n/2+r, n*0.47+r), fill=hexrgb(glow) + (255,)); gl = gl.filter(ImageFilter.GaussianBlur(n*0.13))
        g = Image.alpha_composite(g, gl)
    g.alpha_composite(im, (round(n/2 + dx*n - im.width/2), round(n/2 + dy*n - im.height/2)))
    return g
def rounded(im, n):
    a = im.resize((n, n), Image.LANCZOS).convert("RGBA"); a.putalpha(mask(n)); return a
CFG = dict(
    A=dict(src="r/A_f_rgba.png", ground="#2A2340", scale=0.90, dy=0.03, glow="#3B3360"),
    B=dict(src="r/B_f_rgba.png", ground="#FFC93C", scale=0.50, dy=0.02, glow="#FFD968"),
    C=dict(src="r/C_f_rgba.png", ground="#22B8A9", scale=0.86, glow="#3CCDBE"),
    D=dict(src="r/D_f_rgba.png", ground="#FFE2A6", scale=1.06, dy=0.16, glow="#FFF1CF"),
)
if __name__ == "__main__":
    for k, c in CFG.items():
        im = felt_icon(**c); im.convert("RGB").save(f"t/icon_{k}_felt.png")
    sheet = Image.new("RGB", (4*420, 520), "#E9E4DC")
    for i, k in enumerate(CFG):
        im = Image.open(f"t/icon_{k}_felt.png")
        sheet.paste(rounded(im, 400), (i*420+10, 10), rounded(im, 400))
        x = i*420+10
        for n in (180, 60, 40):
            if n == 180: continue
            sheet.paste(rounded(im, n), (x, 430), rounded(im, n)); x += n+14
    sheet.save("t/felt_icons.png")
