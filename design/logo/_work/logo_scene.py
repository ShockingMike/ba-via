"""Tạ Nhỏ logo marks as needle-felt renders (same vlib felt + fibres as the cast). New file: nothing in blender/via is edited.

  blender.exe -b -P design\\logo\\_work\\logo_scene.py -- <A|B|C|D> [--size 1024] [--samples 128] [--nofuzz] [--tag _x]
Output: design/logo/_work/r/<mark><tag>_rgba.png (transparent, with contact shadow) + <mark><tag>.png on a flat ground.
"""
import bpy, sys, os, math, time
from math import radians, sin, cos, pi
HERE = os.path.dirname(os.path.abspath(__file__))
VIA = os.path.normpath(os.path.join(HERE, "..", "..", "..", "blender", "via"))
sys.path.insert(0, VIA)
import vlib as L
from vlib import V, S, lib
import v_khan
argv = sys.argv[sys.argv.index("--") + 1:]
SIZE = L.argopt(argv, "--size", 1024, int); SAMPLES = L.argopt(argv, "--samples", 128, int); TAG = L.argopt(argv, "--tag", "")
NOFUZZ = "--nofuzz" in argv
WHICH = [a for a in argv if not a.startswith("--")][0]
OUT = os.path.join(HERE, "r"); os.makedirs(OUT, exist_ok=True)
FONT = os.path.join(HERE, "font", "Baloo2-ExtraBold.ttf")
INK = "#2A2340"; ORANGE = "#FF5B1E"; MINT = "#2EC4B6"; CREAM = "#FFF1D0"; INDIGO = "#6360E0"; YELLOW = "#FFC93C"
L.init_scene(); L.FUZZ["on"] = not NOFUZZ
t0 = time.time()


def prop_rig():
    L.new_char(v_khan.J, v_khan.SOLE, face_bone="chest")


def mats(d):
    for k, (h, flat) in d.items(): L.felt(k, h, flat=bool(flat))


FACE_MATS = dict(ink=(INK, 1), white=("#FFFFFF", 1), mouth=("#7A1830", 1), tongue=("#FF7C8E", 1), water=("#8FD8FF", 1), blush=("#FF8FA3", 1))


def dumbbell_pieces(c, half, head_r, head_w, bar_r, e=0.55):
    """axis along X, centre c. Returns (heads, collars, bar) piece lists on bone 'chest'."""
    c = V(c)
    heads = [("chest", L.sell(c + V((sg * half, 0, 0)), (head_w, head_r * 0.92, head_r), e=e)) for sg in (1, -1)]
    cx = half - head_w - head_w * 0.16
    collars = [("chest", L.sell(c + V((sg * cx, 0, 0)), (head_w * 0.26, head_r * 0.62, head_r * 0.62), e=0.6)) for sg in (1, -1)]
    bar = [("chest", L.rcone(c + V((-half, 0, 0)), bar_r, c + V((half, 0, 0)), bar_r))]
    return heads, collars, bar


def static_from(ob, tag, fuzz=1.0):
    """bake any object (text, modifiers) to a static mesh under a root so fuzz_all() and shoot() treat it like a frozen char."""
    bpy.context.view_layer.update(); dg = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(ob.evaluated_get(dg), depsgraph=dg); me.transform(ob.matrix_world)
    for p in me.polygons: p.use_smooth = True
    n = bpy.data.objects.new(tag, me); S["col"].objects.link(n); n["fuzz"] = fuzz
    bpy.data.objects.remove(ob, do_unlink=True)
    return n


def group(tag, obs, loc=(0, 0, 0), rot=(0, 0, 0)):
    root = bpy.data.objects.new(tag, None); S["col"].objects.link(root)
    for o in obs: o.parent = root
    root["parts"] = [o.name for o in obs]; root.location = loc; root.rotation_euler = rot
    S.setdefault("chars", []).append(root)
    return root


def felt_text(body, size, mat, depth=0.03, puff=0.012, voxel=0.004, fuzz=1.0, name="txt"):
    """extruded Baloo letter(s) in the XZ plane facing -Y, centred on the origin, softened like a felt cut-out"""
    cu = bpy.data.curves.new(name, "FONT"); cu.body = body; cu.font = bpy.data.fonts.load(FONT); cu.size = size
    cu.align_x = "CENTER"; cu.align_y = "BOTTOM_BASELINE"; cu.extrude = depth; cu.bevel_depth = puff; cu.bevel_resolution = 4
    o = bpy.data.objects.new(name, cu); S["col"].objects.link(o); o.rotation_euler = (radians(90), 0, 0)
    cu.materials.append(S["mats"][mat])
    o = static_from(o, name + "_m0", fuzz)
    if voxel:
        r = o.modifiers.new("Remesh", "REMESH"); r.mode = "VOXEL"; r.voxel_size = voxel; r.use_smooth_shade = True
        s = o.modifiers.new("Smooth", "SMOOTH"); s.factor = 0.5; s.iterations = 4
        tx = bpy.data.textures.new(name + "_lump", "CLOUDS"); tx.noise_scale = 0.09
        d = o.modifiers.new("lump", "DISPLACE"); d.texture = tx; d.strength = 0.005; d.mid_level = 0.5
        o = static_from(o, name + "_m", fuzz)
    return o


cam = None; shadow = True; bg = "#FFE9B8"

if WHICH == "A":
    # ---- the dumbbell is the creature: one eye per head, the grip is the mouth
    prop_rig(); mats(dict(body=(ORANGE, 0), shade=(L.tint(ORANGE, -0.22), 0), cream=(CREAM, 0), lid=(L.tint(ORANGE, -0.2), 1), **FACE_MATS))
    Z = 0.30
    heads, collars, bar = dumbbell_pieces((0, 0, Z), 0.235, 0.172, 0.098, 0.060)
    L.mk("Heads", heads, "body"); L.mk("Collars", collars, "shade", lump=0.002); L.mk("Bar", bar, "cream", lump=0.003)
    FACE = dict(eye_x=0.232, eye_z=Z + 0.004, eye_w=0.100, eye_h=0.136, pupil=0.031, pupil_tall=1.2,
                brow_z=Z + 0.118, brow_len=0.086, brow_th=0.020, mouth_x=0.0, mouth_z=Z + 0.010, mouth_w=0.074, line=0.0056)
    cfg = dict(face=FACE, bvh=["Heads", "Bar"], ground=["Heads"])
    P = dict(pelvis=dict(pos=v_khan.J["pelvis"]), ground=False,
             face=dict(eyeL=dict(open=1.0, px=-0.35, pz=0.15), eyeR=dict(open=1.0, px=-0.2, pz=0.15),
                       browL=dict(y=0.0, tilt=-6, arch=0.35), browR=dict(y=0.10, tilt=8, arch=0.35),
                       mouth=dict(type="smile", curve=0.30, w=1.0)))
    L.pose(cfg, P)
    root = L.freeze("nhoc", loc=(0, 0, 0), rot=(0, radians(9), radians(-10)), keep_rig=False)
    bpy.context.view_layer.update()
    root.location.z = -float(min(L.part_pts(root, "nhoc_" + n)[:, 2].min() for n in ("Heads",))) + 0.004
    cam = dict(az=-9, el=7, dist=2.45, target=(0, 0, 0.30))

elif WHICH == "B":
    # ---- "a" + dau nang = a small dumbbell
    mats(dict(letter=(INK, 0), bell=(ORANGE, 0), shade=(L.tint(ORANGE, -0.22), 0)))
    a = felt_text("a", 1.60, "letter", depth=0.08, puff=0.008, voxel=0)
    a.location = (0, 0, 0.44)
    ga = group("letter", [a])
    prop_rig(); S["mats"].update({m.name: m for m in bpy.data.materials if m.name in ("letter", "bell", "shade")})
    heads, collars, bar = dumbbell_pieces((0, 0, 0), 0.200, 0.134, 0.081, 0.050)
    L.mk("Heads", heads, "bell", lump=0.003); L.mk("Collars", collars, "shade", lump=0); L.mk("Bar", bar, "shade", lump=0.002)
    L.pose(dict(ground=["Heads"]), dict(pelvis=dict(pos=v_khan.J["pelvis"]), ground=False))
    root = L.freeze("bell", loc=(-0.015, -0.04, 0.160), rot=(0, radians(8), radians(-8)), keep_rig=False)
    cam = dict(az=-6, el=5, dist=4.3, target=(0, 0, 0.66))

elif WHICH == "C":
    # ---- stitched club patch: cream felt disc, running stitch, tri-colour applique dumbbell (one colour per nhoc)
    prop_rig(); mats(dict(patch=("#FFE7BE", 0), inkf=(INK, 1), stitch=(ORANGE, 0), mint=(MINT, 0), indigo=(INDIGO, 0), orange=(ORANGE, 0), ink=(INK, 0), rim=(L.tint(CREAM, -0.10), 0)))
    Z = 0.42; R = 0.38
    L.mk("Disc", [("chest", L.rcone((0, -0.014, Z), R, (0, 0.014, Z), R, flat=True))], "patch", lump=0.004, voxel=0.004)
    st = []; n = 34; rs = R - 0.042
    for i in range(n):
        a0 = 2 * pi * i / n; a1 = a0 + 2 * pi / n * 0.56
        st.append(("chest", L.rcone((rs * cos(a0), -0.017, Z + rs * sin(a0)), 0.0085, (rs * cos(a1), -0.017, Z + rs * sin(a1)), 0.0085)))
    L.mk("Stitch", st, "stitch", lump=0, voxel=0.002, smooth=3, fuzz=0.5)
    rot = lib.rot(0, 0, 14).to_4x4() if False else None
    cz = Z - 0.105; th = radians(14); ux = V((cos(th), 0, sin(th)))
    c = V((-0.012, -0.030, cz))
    R3 = __import__("mathutils").Matrix.Rotation(-th, 3, "Y")
    for sg, mat, nm in ((-1, "mint", "HeadL"), (1, "indigo", "HeadR")):
        L.mk(nm, [("chest", L.sell(c + ux * (sg * 0.135), (0.058, 0.030, 0.098), e=0.55, rot=R3))], mat, lump=0.003)
    L.mk("BarC", [("chest", L.sell(c, (0.100, 0.024, 0.036), e=0.6, rot=R3))], "orange", lump=0.002)
    L.pose(dict(ground=["Disc"]), dict(pelvis=dict(pos=v_khan.J["pelvis"]), ground=False))
    root = L.freeze("patch", keep_rig=False)
    # letters: base glyphs + own dot and hook, laid on an arc
    letters = []; txt = "TẠ NHỎ"; base = "TA NHO"; ra = 0.212; size = 0.140
    widths = dict(T=0.556, A=0.627, N=0.679, H=0.672, O=0.703)
    advs = [(widths[ch] * size + 0.004) if ch != " " else size * 0.34 for ch in base]; tot = sum(advs); pos = -tot / 2
    extra = []
    for ch, full, adv in zip(base, txt, advs):
        t = (pos + adv / 2) / ra; pos += adv
        if ch == " ": continue
        o = felt_text(full, size, "ink", depth=0.008, puff=0.0012, voxel=0, fuzz=0.3, name="L" + ch)
        o.rotation_euler = (0, t, 0); o.location = (ra * sin(t), -0.022, Z + ra * cos(t))
        letters.append(o)
    group("letters", letters)
    shadow = False
    cam = dict(az=0, el=0.5, dist=2.55, target=(0, 0, Z))

elif WHICH == "D":
    # ---- Khan (approved rig, untouched) peeking over a small dumbbell it can barely lift
    cfg = v_khan.build(L, "mint")
    P = dict(pelvis=dict(pos=(0, 0, 0.170), rot=(3, 5, -3)), chest=(0, 0, -2),
             legs=dict(L=dict(ankle=(0.095, 0.0), yaw=14), R=dict(ankle=(-0.090, 0.0), yaw=12)),
             arms=dict(L=dict(wrist=(0.150, -0.185, 0.385), pole=(1, 0.3, -0.2)), R=dict(wrist=(-0.150, -0.185, 0.385), pole=(-1, 0.3, -0.2))),
             face=dict(eyeL=dict(open=0.96, tilt=-4, px=0.15, pz=0.30), eyeR=dict(open=0.90, tilt=-6, px=0.15, pz=0.30),
                       browL=dict(y=0.10, tilt=-10, arch=0.25), browR=dict(y=0.02, tilt=-14, arch=0.15),
                       mouth=dict(type="smile", curve=0.12, w=0.5)),
             dyn=dict(mode="hood", zf=0.588, slant=0.012, fwd=0.03, tag=30))
    L.pose(cfg, P)
    k = L.freeze("khan", keep_rig=False)
    prop_rig(); mats(dict(bell=(ORANGE, 0), shade=(L.tint(ORANGE, -0.22), 0), barm=("#33407F", 0)))
    heads, collars, bar = dumbbell_pieces((0, 0, 0), 0.300, 0.118, 0.070, 0.036)
    L.mk("Heads", heads, "bell"); L.mk("Collars", collars, "shade", lump=0.002); L.mk("Bar", bar, "barm", lump=0.002)
    L.pose(dict(ground=["Heads"]), dict(pelvis=dict(pos=v_khan.J["pelvis"]), ground=False))
    hp = L.part_pts(k, "khan_Hands"); hz = float(hp[:, 2].mean()); hy = float(hp[:, 1].mean())
    L.freeze("bell", loc=(0.0, hy - 0.012, hz - 0.030), rot=(0, radians(-4), radians(3)), keep_rig=False)
    cam = dict(az=3, el=4, dist=2.9, target=(0, 0, 0.40))

L.fuzz_all()
print("BUILT %s in %.1fs" % (WHICH, time.time() - t0))
L.shoot(os.path.join(OUT, WHICH + TAG), cam=cam, size=SIZE, samples=SAMPLES, shadow=shadow, bg=bg, keep_rgba=True)
print("TOTAL %.1fs" % (time.time() - t0))
