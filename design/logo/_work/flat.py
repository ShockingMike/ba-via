# -*- coding: utf8 -*-
"""Flat vector marks, wordmarks, lockups for Ta Nho. Everything is generated so iterations stay consistent."""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(HERE, "glyphs.json"), encoding="utf8"))
INK = "#2A2340"; ORANGE = "#FF5B1E"; ORANGE_D = "#D8430A"; MINT = "#2EC4B6"; MINT_D = "#178F84"; CREAM = "#FFF1D0"
PAPER = "#FFFCF7"; YELLOW = "#FFC93C"; INDIGO = "#6360E0"; SUN = "#FFE9B8"; BLUSH = "#FF8FA3"; WHITE = "#FFFFFF"
TEAL = "#22B8A9"


def rr(x, y, w, h, r, fill, extra=""):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{r:.1f}" fill="{fill}" {extra}/>'


def eye(cx, cy, w, h, px=0.0, py=0.0, mono=None):
    """cast eye: white capsule, tall ink pupil, glint. mono=(fg, bg): eye = knockout (bg), pupil = fg."""
    r = w / 2; pr = w * 0.30; pcx = cx + px * (r - pr * 0.55); pcy = cy + py * (h / 2 - pr)
    wcol, icol = (mono[1], mono[0]) if mono else (WHITE, INK)
    s = rr(cx - r, cy - h / 2, w, h, r, wcol)
    s += f'<ellipse cx="{pcx:.1f}" cy="{pcy:.1f}" rx="{pr:.1f}" ry="{pr*1.22:.1f}" fill="{icol}"/>'
    s += f'<circle cx="{pcx-pr*0.36:.1f}" cy="{pcy-pr*0.55:.1f}" r="{pr*0.32:.1f}" fill="{wcol}"/>'
    return s


def stroke(d, col, w, extra=""):
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


# ---------------------------------------------------------------- mark A: the dumbbell is the creature
def mark_A(head=ORANGE, shade=ORANGE_D, bar=CREAM, mono=None, rot=-9, variant=1):
    fg = mono[0] if mono else None
    hc = fg or head; bc = fg or bar; sc = fg or shade
    line = mono[1] if mono else INK
    s = f'<g transform="rotate({rot} 512 512)">'
    if variant == 1:      # wide-set eyes: one per head, mouth on the grip
        s += rr(352, 438, 320, 148, 40, bc)
        for x0 in (330, 632): s += rr(x0, 372, 62, 280, 28, sc)
        for x in (104, 664): s += rr(x, 272, 256, 480, 104, hc)
        for cx, px in ((232, 0.35), (792, 0.2)): s += eye(cx, 500, 132, 176, px=px, py=-0.12, mono=mono)
        s += stroke("M176 352 Q232 322 290 344", line, 26) + stroke("M734 344 Q792 318 848 348", line, 26)
        s += stroke("M468 498 Q512 540 556 498", line, 22)
    else:                 # face on a fat grip
        s += rr(300, 372, 424, 280, 70, bc)
        for x in (112, 712): s += rr(x, 262, 200, 500, 88, hc)
        for x0 in (288, 676): s += rr(x0, 342, 60, 340, 28, sc)
        for cx in (436, 588): s += eye(cx, 500, 104, 140, px=0.2, py=-0.1, mono=mono)
        s += stroke("M478 606 Q512 632 546 606", line, 18)
    return s + "</g>"


# ---------------------------------------------------------------- mark B: the "a" whose heavy-tone dot is a small dumbbell
def dumbbell_h(cx, cy, w, h, head, bar):
    """side-on mini dumbbell, total width w, head height h"""
    hw = w * 0.30; bh = h * 0.36; r = min(hw, h) * 0.34
    s = rr(cx - w / 2 + hw * 0.6, cy - bh / 2, w - hw * 1.2, bh, bh * 0.3, bar)
    for x in (cx - w / 2, cx + w / 2 - hw): s += rr(x, cy - h / 2, hw, h, r, head)
    return s


def glyph(font, ch, x, y, size, fill, extra=""):
    g = G[font]; k = size / g["upm"]
    return f'<path transform="translate({x:.1f} {y:.1f}) scale({k:.4f})" d="{g["g"][ch]["d"]}" fill="{fill}" {extra}/>'


def mark_B(letter=PAPER, bell=ORANGE, bar=ORANGE_D, mono=None):
    lc = mono[0] if mono else letter; bc = mono[0] if mono else bell; brc = mono[0] if mono else bar
    size = 1060; k = size / 1000
    x = 512 - (28 + (492 - 28) / 2) * k; y = 660
    s = glyph("baloo800", "a", x, y, size, lc)
    s += '<g transform="rotate(-8 512 820)">' + dumbbell_h(512, 818, 330, 150, bc, brc) + "</g>"
    return s


# ---------------------------------------------------------------- mark C: stitched felt patch
def arc_text(txt, cx, cy, r, size, fill, font="baloo800", track=0.0):
    """text centred on 12 o'clock, baseline on radius r"""
    g = G[font]; k = size / g["upm"]
    advs = [(g["g"][c]["adv"] * k if c != " " else size * 0.32) + track for c in txt]
    tot = sum(advs); s = ""; pos = -tot / 2
    for c, a in zip(txt, advs):
        th = (pos + a / 2) / r
        if c != " ":
            s += f'<g transform="translate({cx + r*math.sin(th):.1f} {cy - r*math.cos(th):.1f}) rotate({math.degrees(th):.2f})">' + glyph(font, c, -(a - track) / 2, 0, size, fill) + "</g>"
        pos += a
    return s


def mark_C(patch=CREAM, stitch=ORANGE, bell=INK, mono=None, text=True, R=400):
    fg, bg = mono if mono else (None, None)
    pc = fg or patch; st = bg or stitch; bl = bg or bell
    s = f'<circle cx="512" cy="512" r="{R}" fill="{pc}"/>'
    n = 30; rs = R - 44
    for i in range(n):
        a = 2 * math.pi * i / n; b = a + 2 * math.pi / n * 0.52
        s += stroke(f"M{512+rs*math.cos(a):.1f} {512+rs*math.sin(a):.1f} A{rs} {rs} 0 0 1 {512+rs*math.cos(b):.1f} {512+rs*math.sin(b):.1f}", st, 17)
    cy = 560 if text else 512
    s += f'<g transform="rotate(-14 512 {cy})">' + dumbbell_h(512, cy, 400 if text else 500, 196 if text else 250, bl, bl) + "</g>"
    if text:
        s += arc_text("TẠ NHỎ", 512, 512, 222, 92, bl, track=6)
    return s


# ---------------------------------------------------------------- mark D: Khan peeking over a small dumbbell
def mark_D(body=MINT, brim=CREAM, bell=ORANGE, bar=INK, mono=None, hands=True):
    fg, bg = mono if mono else (None, None)
    bc = fg or body
    s = rr(182, 250, 660, 900, 150, bc)
    if not mono:
        s += stroke("M212 372 Q512 318 812 372", brim, 30)
    for cx, px in ((402, 0.25), (622, 0.25)): s += eye(cx, 545, 132, 172, px=px, py=0.25, mono=mono)
    bw = bg or INK
    s += stroke("M344 430 Q400 404 456 428", bw, 28) + stroke("M568 424 Q624 398 680 432", bw, 28)
    if not mono:
        for cx in (300, 724): s += f'<ellipse cx="{cx}" cy="664" rx="44" ry="28" fill="{BLUSH}"/>'
    if mono: s += rr(40, 716, 944, 40, 0, bg)
    s += rr(150, 770, 724, 74, 30, fg or bar)
    for x in (72, 792): s += rr(x, 660, 160, 294, 62, fg or bell)
    if hands:
        for cx in (372, 652): s += rr(cx - 62, 742, 124, 130, 56, bc, f'stroke="{bg or MINT_D}" stroke-width="{14 if mono else 10}"')
    return s


# ---------------------------------------------------------------- wrappers
def icon(inner, ground, size=1024, uid="k"):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="{size}" height="{size}">'
    s += f'<clipPath id="{uid}"><rect width="1024" height="1024" rx="229"/></clipPath><g clip-path="url(#{uid})">'
    s += f'<rect width="1024" height="1024" fill="{ground}"/>' + inner + "</g></svg>"
    return s


def svg(inner, vb="0 0 1024 1024", size=None):
    w = f' width="{size}"' if size else ""
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}"{w}>{inner}</svg>'


# ---------------------------------------------------------------- wordmark (Baloo 2 800 outlines, own diacritics, hand kerning)
KERN = {("T", "a"): -58, ("N", "h"): -14, ("h", "o"): -12, ("t", "a"): -10, ("n", "h"): -10, ("T", "A"): -40, ("N", "H"): 0, ("H", "O"): -6}


def hook(cx, top, col, w=62, k=1.0):
    """own dau hoi: one fat round-capped stroke, sits `top` above the baseline (y up -> svg y down)"""
    y = -top
    d = f"M{cx-74*k:.0f} {y-58*k:.0f} C{cx-70*k:.0f} {y-150*k:.0f} {cx+84*k:.0f} {y-156*k:.0f} {cx+82*k:.0f} {y-78*k:.0f} C{cx+80*k:.0f} {y-30*k:.0f} {cx+14*k:.0f} {y-34*k:.0f} {cx+8*k:.0f} {y+8*k:.0f}"
    return stroke(d, col, w)


def wordmark(case="title", ink=INK, dot="bell", dotcol=ORANGE, dotbar=None, hookcol=None, font="baloo800", gap=190, track=0):
    """returns (inner_svg, x0, y0, w, h) in font units, baseline at y=0"""
    g = G[font]["g"]; s = ""; x = 0
    txt = dict(title="Ta Nho", lower="ta nho", upper="TA NHO")[case]
    centers = {}; prev = None
    for i, c in enumerate(txt):
        if c == " ": x += gap; prev = None; continue
        if prev: x += KERN.get((prev, c), 0)
        s += f'<path transform="translate({x} 0)" d="{g[c]["d"]}" fill="{ink}"/>'
        b = g[c]["b"]; centers[i] = (x + (b[0] + b[2]) / 2, b[3], x + b[0], x + b[2])
        x += g[c]["adv"] + track; prev = c
    W = x - track
    ax, atop, a0, a1 = centers[1]; ox, otop, o0, o1 = centers[5]
    up = case == "upper"
    # dau nang under a
    if dot == "bell":
        cy = 150 if not up else 142
        s += f'<g transform="rotate(-8 {ax:.0f} {cy})">' + dumbbell_h(ax + (0 if up else -6), cy, 250, 112, dotcol, dotbar or dotcol) + "</g>"
        bottom = cy + 80
    elif dot == "ball":
        s += f'<circle cx="{ax-4:.0f}" cy="128" r="64" fill="{dotcol}"/>'; bottom = 192
    else:
        s += rr(ax - 82, 84, 164, 96, 44, dotcol); bottom = 180
    s += hook(ox + 2, otop + 36, hookcol or ink, w=64 if not up else 60)
    top = otop + 36 + 156 + 34
    return s, -10, -top, W + 20, top + bottom + 10


def wm_svg(scale=1.0, **kw):
    s, x0, y0, w, h = wordmark(**kw)
    return svg(s, vb=f"{x0} {y0} {w} {h}"), w, h
