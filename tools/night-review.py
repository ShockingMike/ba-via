"""Build small review sheets + prototypes/render-review.html from the overnight renders.
Usage (repo root):  python tools/night-review.py
Output: prototypes/review/*.jpg (small, public-safe) and prototypes/render-review.html
"""
import json, os, re, glob, html
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'blender', 'out', 'via')
REV = os.path.join(ROOT, 'prototypes', 'review')
os.makedirs(REV, exist_ok=True)
CREAM = (253, 247, 236)
INK = (40, 34, 54)
try:
    FONT = ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 22)
    SMALL = ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 18)
except OSError:
    FONT = SMALL = ImageFont.load_default()


def fit(path, box):
    im = Image.open(path).convert('RGBA')
    bb = im.getbbox()
    if bb:
        im = im.crop(bb)
    im.thumbnail((box, box), Image.LANCZOS)
    return im


def grid(rows, cols, cell, title, fname, header=None):
    """rows: list of (label, [path|None per col])"""
    top = 60 + (34 if header else 0)
    W, H = 200 + cols * cell, top + len(rows) * (cell + 10) + 20
    sheet = Image.new('RGB', (W, H), CREAM)
    d = ImageDraw.Draw(sheet)
    d.text((20, 16), title, font=FONT, fill=INK)
    if header:
        for c, h in enumerate(header):
            d.text((200 + c * cell + 10, 60), h, font=SMALL, fill=INK)
    for r, (label, paths) in enumerate(rows):
        y = top + r * (cell + 10)
        d.text((20, y + cell // 2 - 12), label[:22], font=SMALL, fill=INK)
        for c, p in enumerate(paths):
            if p and os.path.exists(p):
                im = fit(p, cell - 12)
                sheet.paste(im, (200 + c * cell + (cell - im.width) // 2, y + (cell - im.height) // 2), im)
            else:
                d.text((200 + c * cell + 20, y + cell // 2 - 10), 'chưa có', font=SMALL, fill=(170, 160, 150))
    sheet.thumbnail((1100, 100000), Image.LANCZOS)
    sheet.save(os.path.join(REV, fname), quality=80, optimize=True)
    return fname


def rgba(p):
    q = p.replace('.png', '_rgba.png')
    return q if os.path.exists(q) else p


sections = []

# 1. wardrobe: item x species
wd = os.path.join(OUT, 'wear_d3')
items = sorted({re.sub(r'_(khan|binh|gang).*$', '', os.path.basename(f)) for f in glob.glob(os.path.join(wd, '*_khan*.png'))})
items = [i for i in items if not i.startswith('outfit')]
if items:
    VN = {'bangtay': 'Băng tay Hội mình', 'chia': 'Chìa khoá tủ 17', 'coc': 'Cốc trà đá', 'dep': 'Dép tổ ong', 'huy': 'Huy chương 2009',
          'kinh': 'Kính bơi lạc bể', 'mu': 'Mũ lưỡi trai', 'quat': 'Quạt nhựa', 'ta': 'Tạ lon sữa', 'tui': 'Túi bao tử', 'vuong': 'Vương miện giấy'}
    rows = [(VN.get(i, i), [rgba(os.path.join(wd, f'{i}_{sp}.png')) for sp in ('khan', 'binh', 'gang')]) for i in items]
    for k in range(0, len(rows), 6):
        sections.append(('Tủ đồ D3 (nháp)', grid(rows[k:k + 6], 3, 220, f'Tủ đồ D3 · phần {k // 6 + 1}', f'wardrobe_{k // 6 + 1}.jpg', ['Khăn', 'Bình', 'Găng'])))
    outfits = sorted(glob.glob(os.path.join(wd, 'outfit*.png')))
    outfits = [o for o in outfits if not o.endswith('_rgba.png')]
    if outfits:
        sections.append(('Tủ đồ D3 (nháp)', grid([(os.path.basename(o)[:-4], [rgba(o)]) for o in outfits], 1, 260, 'Phối đồ', 'wardrobe_outfits.jpg')))

# 2. cast: pose x (khan default, binh, gang)
man = os.path.join(ROOT, 'blender', 'queue', 'manifest_poses.json')
cast = os.path.join(OUT, 'cast')
screens = os.path.join(OUT, 'screens')
poses = sorted({os.path.basename(f).rsplit('_', 1)[0] for f in glob.glob(os.path.join(cast, 'binh', '*.png')) if not f.endswith('_rgba.png')})
if poses:
    def find(sp, pose):
        for pat in (f'{pose}_*.png',):
            c = [f for f in glob.glob(os.path.join(cast, sp, pat)) if not f.endswith('_rgba.png')]
            dflt = {'binh': 'orange', 'gang': 'violet'}.get(sp)
            for f in c:
                if dflt and f.endswith(f'_{dflt}.png'):
                    return rgba(f)
            if c:
                return rgba(sorted(c)[0])
        return None
    rows = []
    for p in poses:
        k = os.path.join(screens, p + '_rgba.png')
        k = k if os.path.exists(k) else os.path.join(screens, p + '.png')
        rows.append((p, [k, find('binh', p), find('gang', p)]))
    for k in range(0, len(rows), 8):
        sections.append(('Bình và Găng ở mọi tư thế (nháp)', grid(rows[k:k + 8], 3, 200, f'Tư thế bạn đồng hành · phần {k // 8 + 1}', f'cast_{k // 8 + 1}.jpg', ['Khăn (đã duyệt)', 'Bình', 'Găng'])))

# 3. Khan colours: a few poses x 6 colours
kc = os.path.join(cast, 'khan')
sample = ['kh_stand', 'kh_cheer', 'k10_door_glad', 'kh_box']
cols = sorted({os.path.basename(f)[:-4].rsplit('_', 1)[-1] for f in glob.glob(os.path.join(kc, '*.png')) if not f.endswith('_rgba.png')})
if cols:
    rows = [(p, [rgba(os.path.join(kc, f'{p}_{c}.png')) for c in cols]) for p in sample]
    sections.append(('Khăn đủ 6 màu', grid(rows, len(cols), 170, 'Khăn các màu (mẫu 4 tư thế)', 'khan_colours.jpg', cols)))

# 4. Mirror: first and middle frame per exercise
mr = os.path.join(OUT, 'mirror')
ex = sorted(d for d in os.listdir(mr) if os.path.isdir(os.path.join(mr, d)) and not d.startswith('_')) if os.path.isdir(mr) else []
done = [e for e in ex if os.path.exists(os.path.join(mr, e, 'f4.png'))]
if done:
    rows = [(e, [os.path.join(mr, e, f'f{i}.png') for i in range(5)]) for e in done]
    for k in range(0, len(rows), 8):
        sections.append(('Bóng trong gương (nháp)', grid(rows[k:k + 8], 5, 150, f'Bóng gương · phần {k // 8 + 1}', f'mirror_{k // 8 + 1}.jpg')))

# page
body = ['<main style="max-width:1100px;margin:0 auto;padding:20px 16px;font:15px/1.5 system-ui;background:#FDF7EC;color:#28223A">',
        '<h1 style="margin:0 0 6px">Render đêm 26/11 · bản nháp để duyệt</h1>',
        f'<p style="color:#6b6478">Tự sinh bằng <code>tools/night-review.py</code>. Mọi hình là nháp, chưa chốt.</p>']
cur = None
for sec, f in sections:
    if sec != cur:
        body.append(f'<h2 style="margin:28px 0 8px">{html.escape(sec)}</h2>')
        cur = sec
    body.append(f'<a href="review/{f}" target="_blank"><img src="review/{f}" style="width:100%;border-radius:12px;margin:6px 0;display:block" loading="lazy"></a>')
body.append('</main>')
open(os.path.join(ROOT, 'prototypes', 'render-review.html'), 'w', encoding='utf-8').write('<title>Duyệt render đêm</title>\n' + '\n'.join(body))
print('sections', len(sections), 'mirror done', len(done), 'of', len(ex))
