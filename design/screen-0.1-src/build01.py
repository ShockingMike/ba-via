"""Build design/screen-0.1.html from template.html + the w02_* layers (welcome2.py).
  python build01.py <pt.txt>      pt.txt = the "PT name x y" lines welcome2.py prints
The shared design-system CSS is taken verbatim from screens-v2-src/app.css (everything above the per-screen rules).
Also writes wrap.html here for headless screenshots: ?only=A|B|C  &state=open  &freeze=<ms>"""
import base64, io, os, sys
from PIL import Image
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
R = "C:/Work/GymApp/blender/out/via/screens/"
OUT = "C:/Work/GymApp/design/screen-0.1.html"
PT = {l.split()[1]: (float(l.split()[2]), float(l.split()[3])) for l in open(sys.argv[1], encoding="utf-8", errors="ignore") if l.startswith("PT ")}


def uri(im, q=90):
    b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()


NAMES = ("base", "lid", "peek", "khan", "binh", "gang")
L = {k: Image.open(R + "w02_%s_rgba.png" % k).convert("RGBA") for k in NAMES}
S = L["base"].width
a = np.zeros((S, S), np.uint8)
for k in ("base", "lid", "khan", "binh", "gang"): a = np.maximum(a, np.array(L[k])[..., 3])
ys, xs = np.where(a > 6); pad = int(S * 0.008)
# crop: full height of the action, but the dumbbells may run off the sides (they are set dressing)
c = np.zeros((S, S), np.uint8)
for k in ("lid", "khan", "binh", "gang"): c = np.maximum(c, np.array(L[k])[..., 3])
cx = np.where(c > 6)[1]
x0, x1 = max(0, cx.min() - int(S * 0.035)), min(S, cx.max() + int(S * 0.035)); y0, y1 = max(0, ys.min() - pad), min(S, ys.max() + pad * 4)
cw, ch = x1 - x0, y1 - y0
W = 780; H = round(ch * W / cw)
crop = lambda im: im.crop((x0, y0, x1, y1)).resize((W, H), Image.LANCZOS)
fx = lambda p: ((p[0] * S - x0) / cw * 100, (p[1] * S - y0) / ch * 100)


def edge(pl, pr):
    (lx, ly), (rx, ry) = fx(pl), fx(pr); k = (ry - ly) / (rx - lx)
    return ly - k * lx, ry + k * (100 - rx)


rim_l, rim_r = edge(PT["rimL"], PT["rimR"]); lid_l, lid_r = edge(PT["lidL"], PT["lidR"])
V = {k: uri(crop(L[k]), 92 if k in ("khan", "binh", "gang") else 90) for k in NAMES}
V.update(ar="%d/%d" % (cw, ch), rim_l="%.2f" % (rim_l + 0.3), rim_r="%.2f" % (rim_r + 0.3), lid_l="%.2f" % (lid_l - 0.5), lid_r="%.2f" % (lid_r - 0.5),
         floor_x="%.1f" % fx(PT["floor"])[0], floor_y="%.1f" % (fx(PT["floor"])[1] + 6), hinge="%.1f" % (fx(PT["mouth"])[1] - 6))

STATUS = ('<div class="status"><span>%s</span><svg width="68" height="14" viewBox="0 0 68 14" fill="#2A2340" aria-hidden="true">'
          '<rect x="0" y="9" width="4" height="5" rx="1.5"/><rect x="6" y="6" width="4" height="8" rx="1.5"/><rect x="12" y="3" width="4" height="11" rx="1.5"/><rect x="18" y="0" width="4" height="14" rx="1.5"/>'
          '<path d="M36 3.2c3 0 5.6 1.2 7.5 3.1l-1.900 1.900A7.900 7.900 0 0 0 36 6c-2.200 0-4.200.900-5.600 2.200l-1.900-1.900A10.600 10.600 0 0 1 36 3.200zm0 5.300c1.500 0 2.900.600 3.900 1.600L36 14l-3.900-3.900c1-1 2.400-1.600 3.900-1.600z"/><rect x="48" y="1" width="20" height="12" rx="4"/></svg></div>')
ART = ('<button class="art" aria-label="Cái hộp đồ bỏ quên. Chạm để mở hoặc đóng."><span class="floor"></span><img src="{{base}}" alt="Hộp các-tông ghi ĐỒ BỎ QUÊN, cạnh mấy quả tạ tay">'
       '<span class="clip"><img src="{{peek}}" alt="Mấy đôi mắt ló ra từ khe nắp hộp"></span><img class="lid" src="{{lid}}" alt="">'
       '<img class="who binh" src="{{binh}}" alt="Bình"><img class="who gang" src="{{gang}}" alt="Găng"><img class="who khan" src="{{khan}}" alt="Khăn"></button>')


def frame(fid, cap, install, head, line, cta, cta_mode, cta_toast, second, sec_mode, sec_toast, nxt):
    return '''
  <section class="unit" id="u%s">
    <p class="cap">%s</p>
    <div class="phone"><div class="fit"><div class="screen w" id="s%s" data-next="%s">
      %s
      <div class="top"><span class="mark" role="img" aria-label="Tên app"></span>%s</div>
      <div class="scene">%s</div>
      <div class="pad say"><h2>%s</h2><p>%s</p></div>
      <div class="pad panel">
        <button class="btn-main" data-mode="%s" data-rest="%s" data-toast="%s">%s</button>
        <button class="restore" data-mode="%s" data-toast="%s">%s</button>
      </div>
      <div class="toast" role="status"></div>
      <div class="home"></div>
    </div></div></div>
  </section>''' % (fid, cap, fid, nxt, STATUS % '17:42', '<button class="install">Cài app</button>' if install else '', ART, head, line,
                   cta_mode, cta_mode, cta_toast, cta, sec_mode, sec_toast, second)


HEAD = 'Nhận một người bạn tập. Tập đều để giữ bạn ấy.'
LINE = 'Ba người bạn nhỏ đang chờ chủ trong hộp đồ bỏ quên của phòng gym.'
frames = (
    frame('A', 'a · Mở lần đầu trong trình duyệt', True, HEAD, LINE, 'Mở hộp', 'open', '', 'Đã dùng app rồi? <b>Khôi phục dữ liệu</b>', 'toast',
          'Bản mẫu: sang 5.6a, khôi phục dữ liệu.', 'Bản mẫu: sang 0.2, cài lên màn hình chính.')
    + frame('B', 'b · Mở từ màn hình chính (đã cài)', False, HEAD, LINE, 'Mở hộp', 'open', '', 'Đã dùng app rồi? <b>Khôi phục dữ liệu</b>', 'toast',
            'Bản mẫu: sang 5.6a, khôi phục dữ liệu.', 'Bản mẫu: sang 0.3.')
    + frame('C', 'c · Máy trống nhưng từng có dữ liệu', False, 'Ơ, chủ đấy à?', 'Máy mới, nhưng ba người bạn tập trong hộp vẫn nhớ chủ.',
            'Khôi phục dữ liệu', 'toast', 'Bản mẫu: sang 5.6a, khôi phục dữ liệu.', 'Chưa dùng bao giờ? <b>Mở hộp</b>', 'open', '', 'Bản mẫu: sang 0.3.'))
css = open("C:/Work/GymApp/design/screens-v2-src/app.css", encoding="utf-8").read()
css = css[:css.index("/* ---------- Hôm nay")]
s = open(os.path.join(HERE, "template.html"), encoding="utf-8").read().replace("{{system_css}}", css).replace("{{frames}}", frames)
for k, v in V.items(): s = s.replace("{{%s}}" % k, v)
assert "{{" not in s, s[s.index("{{"):][:40]
open(OUT, "w", encoding="utf-8").write(s)
WRAP_HEAD = ('<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
             '<style>body{margin:0;font:14px system-ui}img{max-width:100%}[hidden]{display:none!important}</style>'
             '<script>var o=(location.search.match(/only=([A-C])/)||[])[1];if(o)document.documentElement.className="only only"+o</script>'
             '<style>.only .intro,.only .cap{display:none}.only .desk{padding:0!important;margin:0;max-width:none}.only .frames{justify-content:flex-start}'
             '.only .unit{display:none}.onlyA #uA,.onlyB #uB,.onlyC #uC{display:flex}.only .phone{box-shadow:none}</style></head><body>')
WRAP_TAIL = ('<script>var fz=(location.search.match(/freeze=([0-9]+)/)||[])[1];if(fz)setTimeout(function(){document.getAnimations().forEach(function(a){a.pause();a.currentTime=+fz})},60);</script></body></html>')
open(os.path.join(HERE, "wrap.html"), "w", encoding="utf-8").write(WRAP_HEAD + s + WRAP_TAIL)
print("size %.2f MB" % (len(s.encode()) / 1e6), {k: v for k, v in V.items() if not v.startswith("data:")})
