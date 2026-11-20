# -*- coding: utf8 -*-
import flat as F, base64
refs = ["duolingo-learn-languages", "finch-self-care-pet", "strava-run-bike-walk", "headspace-sleep-meditation", "gentler-streak-workout-track"]


def ref(n, s):
    b = base64.b64encode(open(f"ref/{n}.jpg", "rb").read()).decode()
    return f'<img src="data:image/jpeg;base64,{b}" width="{s}" height="{s}" style="border-radius:{s*0.2237:.1f}px">'


cands = [
    ("A1 navy", F.mark_A(), F.INK), ("A1 sun", F.mark_A(), F.YELLOW), ("A1 mint", F.mark_A(), F.TEAL), ("A1 cream", F.mark_A(bar=F.INK), F.SUN),
    ("A2 navy", F.mark_A(variant=2), F.INK), ("A2 sun", F.mark_A(variant=2, bar=F.PAPER), F.YELLOW),
    ("B orange", F.mark_B(bell=F.INK, bar=F.INK), F.ORANGE), ("B mint", F.mark_B(), F.TEAL), ("B navy", F.mark_B(), F.INK), ("B sun", F.mark_B(letter=F.INK), F.YELLOW),
    ("C mint", F.mark_C(text=False), F.TEAL), ("C navy", F.mark_C(text=False), F.INK), ("C orange", F.mark_C(text=False, stitch=F.INK), F.ORANGE), ("C text", F.mark_C(text=True), F.TEAL),
    ("D sun", F.mark_D(), F.SUN), ("D yellow", F.mark_D(), F.YELLOW), ("D navy", F.mark_D(bar=F.CREAM), F.INK), ("D orange", F.mark_D(bell=F.INK), "#FF7A3D"),
]
h = '<meta charset="utf8"><body style="margin:0;background:#E9E4DC;font:12px sans-serif;width:1500px">'
h += '<div style="display:flex;flex-wrap:wrap;gap:14px;padding:14px">'
for i, (n, m, g) in enumerate(cands):
    h += f'<div style="width:230px">{F.icon(m, g, 200, uid="a%d"%i)}<br>{F.icon(m, g, 60, uid="b%d"%i)} {F.icon(m, g, 40, uid="c%d"%i)} {n}</div>'
h += '</div>'
order = [refs[0], 0, 5, refs[1], 7, 9, refs[2], 10, 12, refs[3], 14, 15, refs[4], 16, 4, 8, 11]
for bgc in ("#3b6a8c", "#d9c7b4"):
    for sz in (60, 40):
        h += f'<div style="background:{bgc};padding:16px;display:flex;gap:22px;flex-wrap:wrap;align-items:center">'
        for o in order:
            h += ref(o, sz) if isinstance(o, str) else F.icon(cands[o][1], cands[o][2], sz, uid="h%d%s%d" % (o, bgc[1:3], sz))
        h += '</div>'
open("t/sheet1.html", "w", encoding="utf8").write(h)
