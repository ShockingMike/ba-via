"""Final three nav icons: one markup source -> page, six static SVGs, nav-anim.js.   python final.py"""
import math, os, re, json
D = "C:/Work/GymApp/design/"
SW_OFF, SW_ON = 1.9, 2.3

def scl(d, k): return re.sub(r"-?\d*\.?\d+", lambda m: ("%.2f" % (float(m.group()) * k)).rstrip("0").rstrip("."), d)
def rays(cx, cy, r0, r1, n, a0=0):
    d = ""
    for i in range(n):
        a = math.radians(a0 + i * 360 / n); c, s = math.cos(a), -math.sin(a)
        d += "M%.2f %.2fL%.2f %.2f" % (cx + r0 * c, cy + r0 * s, cx + r1 * c, cy + r1 * s)
    return d
def tint(inner, state):
    """state: 'off' -> nothing, 'on' -> baked soft fill, 'dyn' -> present but hidden until the tab is current (CSS in nav-anim.js)."""
    if state == "off": return ""
    return '<g class="ni-tint" fill="currentColor" stroke="none" opacity="%s">%s</g>' % (".2" if state == "on" else "0", inner)

# ---- Hôm nay: the logo's dumbbell (pill plates, thick bar, -12 deg) under a six-ray sun
SUN = dict(cx=7.9, cy=6.7, r=2.6, r0=4.4, r1=5.8)
def homnay(state, uid):
    plates = '<rect x="3" y="10.9" width="5.3" height="8.6" rx="2.4"/><rect x="16.9" y="10.9" width="5.3" height="8.6" rx="2.4"/>'
    bar = '<path d="M8.3 13.5h8.6M8.3 16.9h8.6"/>'
    barfill = '<path d="M8.3 13.5h8.6v3.4H8.3z"/>'
    sun = '<circle cx="%(cx)s" cy="%(cy)s" r="%(r)s"/>' % SUN
    R = 'transform="rotate(-12 12.6 15.2)"'
    od = 'style="transform-origin:12.6px 20.7px"'
    return ('<mask id="%s" maskUnits="userSpaceOnUse" x="0" y="0" width="24" height="24"><rect width="24" height="24" fill="#fff" stroke="none"/>'
            '<g class="ni-db" %s><g %s fill="#000" stroke="#000" stroke-width="4.4">%s%s</g></g></mask>' % (uid, od, R, plates, barfill)
            + '<g mask="url(#%s)"><g class="ni-sun" style="transform-origin:%spx %spx">%s%s<path d="%s"/></g></g>' % (uid, SUN["cx"], SUN["cy"], tint(sun, state), sun, rays(SUN["cx"], SUN["cy"], SUN["r0"], SUN["r1"], 5, 0)[:0] + "".join(rays(SUN["cx"], SUN["cy"], SUN["r0"], SUN["r1"], 1, a) for a in (0, 45, 90, 135, 180)))
            + '<g class="ni-db" %s><g %s>%s%s%s</g></g>' % (od, R, tint(plates + barfill, state), plates, bar))

# ---- Hội: two mitten palms, the right one in front, a three-line burst over the contact
PAD = scl("M-2.7 .4-3-2.4C-4.4-3-5.7-4.2-5.9-5.5-6.1-6.8-4.7-7.4-3.9-6.5L-3-5.5V-8.3C-3-9.6-2-10.5-.8-10.5H.8C2-10.5 3-9.6 3-8.3V-2.4L2.7 .4Z", 1.27)
TL = "translate(6.5 20.1) rotate(18)"
TR = "translate(16.9 19.6) scale(-1 1) rotate(21)"
CUFF = ''
def hoi(state, uid):
    hand = '<path d="%s"/>' % PAD
    def g(t): return '<g transform="%s">%s%s%s</g>' % (t, tint(hand, state), hand, CUFF)
    ol, orr = 'style="transform-origin:6.6px 21px"', 'style="transform-origin:17.4px 20.4px"'
    return ('<mask id="%s" maskUnits="userSpaceOnUse" x="0" y="0" width="24" height="24"><rect width="24" height="24" fill="#fff" stroke="none"/>'
            '<g class="ni-hand-r" %s><path transform="%s" d="%s" fill="#000" stroke="#000" stroke-width="4"/></g></mask>' % (uid, orr, TR, PAD)
            + '<g mask="url(#%s)"><g class="ni-hand-l" %s>%s</g></g>' % (uid, ol, g(TL))
            + '<g class="ni-hand-r" %s>%s</g>' % (orr, g(TR))
            + '<path class="ni-burst" style="transform-origin:12px 6.5px" d="M11.8 1.5v2.2M7.6 4 6.3 2.3M15.9 3.2l1.3-1.7"/>')

# ---- Tủ đồ: a gym locker, door ajar; vents, handle, two little feet. The sock tip only peeks during the tap animation.
def tudo(state, uid):
    body = '<rect x="3.6" y="2.6" width="9.8" height="17.4" rx="1.8"/>'
    door = '<path d="M13.4 4l5.5 1.7a1.2 1.2 0 0 1 .9 1.2v8.6a1.2 1.2 0 0 1-.9 1.2l-5.5 1.9"/>'
    sock = ('<path class="ni-sock" opacity="0" style="transform-origin:13.4px 19.6px" d="M14.3 18.2h2.3a1.5 1.5 0 0 1 0 3h-2.3"/>' if state == "dyn" else "")
    return ('<g class="ni-body">%s%s<path d="M6.6 6.4h3.8M6.6 9.2h3.8M5.6 20v1.6M11.4 20v1.6"/></g>' % (tint(body, state), body)
            + sock + '<g class="ni-door" style="transform-origin:13.4px 11px">%s%s<path d="M16.7 10.4v1.8"/></g>' % (tint(door, state), door))

ICON = {"homnay": homnay, "hoi": hoi, "tudo": tudo}
TABS = (("homnay", "Hôm nay"), ("hoi", "Hội"), ("tudo", "Tủ đồ"))
_n = [0]
def svg(k, state, size=28, uid=None, attrs=""):
    _n[0] += 1
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%s" height="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round"%s>%s</svg>' % (size, size, SW_ON if state == "on" else SW_OFF, attrs, ICON[k](state, uid or "ni-s%d" % _n[0])))

if __name__ == "__main__":
    os.makedirs(D + "nav-icons", exist_ok=True)
    w = lambda p, s: open(D + p, "w", encoding="utf-8", newline="\n").write(s)
    for k, _ in TABS:
        w("nav-icons/%s.svg" % k, svg(k, "off", 24, uid=k + "-m") + "\n")
        w("nav-icons/%s-on.svg" % k, svg(k, "on", 24, uid=k + "-on-m") + "\n")
    js = open("nav-anim.tpl.js", encoding="utf-8").read()
    js = js.replace("/*ICONS*/{}", json.dumps({k: ICON[k]("dyn", "{{id}}") for k, _ in TABS}, ensure_ascii=False, indent=1))
    w("nav-icons/nav-anim.js", js)

    # ---------- the review page
    P = lambda d: '<path d="%s"/>' % d
    MITT = "M7.4 20.6v-5L5.6 13.4a1.1 1.1 0 0 1 1.8-1.3l.8 1V7.6a2 2 0 0 1 4 0v7.8c0 2.1-.9 3.8-2.4 5.2z"
    OLD = {  # set 2, copied from screen-1.1-1.3-src/navc.py
     "homnay": [(P("M2.6 12.6h3.2v7.6H2.6zM18.2 12.6h3.2v7.6h-3.2z"), 1), (P("M5.8 16.4h12.4"), 0), ('<circle cx="17.6" cy="5.6" r="2.4"/>', 1), (P("M17.6 1.6v.6M21.6 5.6H21M14.2 5.6h-.6M20.4 2.8l-.4.4M14.8 2.8l.4.4"), 0)],
     "hoi": [('<g transform="translate(-2.4 0) rotate(-12 9.4 14)"><path d="' + MITT + '"/></g>', 1), ('<g transform="translate(26.4 0) scale(-1 1) rotate(-12 9.4 14)"><path d="' + MITT + '"/></g>', 1), (P("M12 2.6v2M8.9 3.6l1 1.5M15.1 3.6l-1 1.5"), 0)],
     "tudo": [(P("M4.8 3.2h8.6v17.6H4.8z"), 1), (P("M13.4 3.2l5.8 1.9v13.8l-5.8 1.9"), 1), (P("M7.2 6.6h3.8M7.2 9h3.8"), 0), (P("M15.6 11v2"), 0)],
    }
    def old(k, on, size=28):
        out = "".join(e.replace('"/>', '" fill="currentColor" fill-opacity=".22"/>') if (on and f) else e for e, f in OLD[k])
        return '<svg class="li" width="%s" height="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (size, size, "2.2" if on else "1.9", out)
    src = open(D + "nav-c-icons.html", encoding="utf-8").read()
    face = re.search(r"\.o-face\{[^}]*\}", src).group()
    RING = ('<svg class="ring" viewBox="0 0 70 70" aria-hidden="true"><circle cx="35" cy="35" r="32" fill="none" stroke="#EDE5D8" stroke-width="5"/>'
            '<circle cx="35" cy="35" r="32" fill="none" stroke="#22B8A9" stroke-width="5" stroke-linecap="round" stroke-dasharray="67 201" transform="rotate(-90 35 35)"/></svg>')
    ORB = '<button class="orb" aria-label="Tôi">%s<i class="o-face"></i></button>' % RING
    def nav(active):   # live bar: nav-anim.js draws the icons from data-icon and wires the taps
        t = "".join('<button class="t tab%s" data-icon="%s" aria-current="%s"><span>%s</span><em></em></button>' % (" on" if i == active else "", k, "page" if i == active else "false", n) for i, (k, n) in enumerate(TABS))
        return '<nav class="navg vc navbar"><div class="pill">%s</div>%s</nav>' % (t, ORB)
    def oldnav(active):
        t = "".join('<button class="t%s" aria-current="%s">%s<span>%s</span><em></em></button>' % (" on" if i == active else "", "page" if i == active else "false", old(k, i == active), n) for i, (k, n) in enumerate(TABS))
        return '<nav class="navg vc"><div class="pill">%s</div>%s</nav>' % (t, ORB)
    NOTE = {"homnay": "Quả tạ nhỏ của logo (nghiêng 12°, hai bánh tạ bầu) trước mặt trời đang lên",
            "hoi": "Hai bàn tay đập vào nhau, tay phải đè lên tay trái, ba tia bật ra",
            "tudo": "Tủ đồ phòng tập hé cửa: hai khe thoáng, tay nắm, hai chân nhỏ"}
    MOVE = {"homnay": "Chạm: tạ nhấc lên rồi lún nhẹ, mặt trời phồng lên lắc một cái", "hoi": "Chạm: hai tay tách ra rồi đập, ba tia bật ra",
            "tudo": "Chạm: cửa khép mở một nhịp, mũi tất ló ra rồi rụt vào"}
    big = "".join('<figure><div class="pair"><span class="off">%s</span><span class="onn">%s</span></div><figcaption><b>%s</b>%s<i>%s</i></figcaption></figure>'
                  % (svg(k, "off", 96), svg(k, "on", 96), n, NOTE[k], MOVE[k]) for k, n in TABS)
    bars = "".join('<div class="bar"><small>%s đang chọn</small>%s</div>' % (n, nav(i)) for i, (k, n) in enumerate(TABS))
    cmp_ = "".join('<div class="c"><small>%s</small><div class="row"><span class="off">%s</span><span class="onn">%s</span><u>cũ</u></div><div class="row"><span class="off">%s</span><span class="onn">%s</span><u>mới</u></div></div>'
                   % (n, old(k, 0), old(k, 1), svg(k, "off"), svg(k, "on")) for k, n in TABS)
    html = open("page.tpl.html", encoding="utf-8").read()
    for a, b in (("{{face}}", face), ("{{big}}", big), ("{{bars}}", bars), ("{{cmp}}", cmp_), ("{{oldbar}}", '<div class="bar"><small>Bộ 2 cũ</small>%s</div>' % oldnav(1))):
        html = html.replace(a, b)
    assert "{{" not in html
    w("nav-icons-final.html", html)
    print("ok", len(html), len(js))
