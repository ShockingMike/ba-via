# -*- coding: utf8 -*-
import flat as F
h = '<meta charset="utf8"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&display=swap"><body style="margin:0;background:#FFFCF7;font:12px sans-serif;width:1400px;padding:20px">'
h += '<div style="font:800 150px/1.3 \'Baloo 2\';color:#2A2340">Tạ Nhỏ <span style="font-size:14px">(Baloo 2 mặc định)</span></div>'
for kw in (dict(), dict(case="lower"), dict(case="upper", track=30, gap=230), dict(dot="ball"), dict(dot="pill", dotcol=F.MINT)):
    s, x0, y0, w, hh = F.wordmark(**kw)
    h += f'<div style="margin:10px 0"><svg viewBox="{x0} {y0} {w} {hh}" height="210" style="background:#FFF1CF">{s}</svg> <svg viewBox="{x0} {y0} {w} {hh}" height="26">{s}</svg> <svg viewBox="{x0} {y0} {w} {hh}" height="40" style="background:#2A2340">{s.replace(F.INK, "#fff")}</svg></div>'
open("t/sheet2.html", "w", encoding="utf8").write(h)
