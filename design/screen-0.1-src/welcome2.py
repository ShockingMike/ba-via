"""Screen 0.1 art, v2. REST: the DO BO QUEN box, lid cracked open, eyes and Gang's fingertips in the gap.
REVEAL: Khan, Binh and Gang standing in front of the open box, one hopeful look. A pair of dumbbells says "gym".
Model-sheet lock: lens 90, azimuth -10, elevation 5, vlib light rig, transparent film. The box alone is turned
toward the camera so its label reads; the characters keep the sheet angle.
Registered layers (same camera, same frame), written to out/via/screens/:
  w02_base  box (open, no lid) + dumbbells      w02_lid   the lid, propped a hand's width open
  w02_peek  whoever is inside, looking out      w02_khan / w02_binh / w02_gang   the three, out of the box
Prints "PT name x y" (image fractions) for the CSS: the gap the peek layer is clipped to, and the box mouth.

  blender -b -P welcome2.py -- [--size 1400] [--nofuzz]
"""
import bpy, sys, os
from math import radians, tan
HERE = "C:/Work/GymApp/blender/via"; sys.path.insert(0, HERE)
import vlib as L
from vlib import V, S, lib
import v_khan, v_binh, v_gang
from mathutils import Matrix
from bpy_extras.object_utils import world_to_camera_view
argv = sys.argv[sys.argv.index("--") + 1:]
SIZE = L.argopt(argv, "--size", 1400, int); SAMPLES = L.argopt(argv, "--samples", 160, int); ONLY = L.argopt(argv, "--only", "")
L.init_scene(); L.FUZZ["on"] = "--nofuzz" not in argv
out = os.path.join(L.OUT, "screens")
FONT = "C:/Windows/Fonts/VNF-Comic Sans.ttf"

HOOD = dict(mode="hood", zf=0.590, slant=0.03, fwd=0.03, tag=-80)
F_HOPE_K = dict(eyeL=dict(open=0.95, tilt=-3, px=0.0, pz=0.12), eyeR=dict(open=0.90, tilt=-5, px=0.0, pz=0.12),
                brows=dict(y=0.14, tilt=-8, arch=0.3), mouth=dict(type="grin", w=0.74, h=0.42, teeth=False, tongue=True, dx=0.03))
F_HOPE_B = dict(eyes=dict(open=0.95, tilt=0, px=0.0, pz=0.12), browL=dict(y=0.20, tilt=-6, arch=0.3), browR=dict(y=0.24, tilt=-8, arch=0.3),
                mouth=dict(type="smile", curve=0.30, w=0.85))
F_HOPE_G = dict(eyeL=dict(open=0.84, tilt=2, px=0.0, pz=0.12), eyeR=dict(open=0.80, tilt=3, px=0.0, pz=0.12),
                brows=dict(y=0.10, tilt=-4, arch=0.2), mouth=dict(type="smile", curve=0.30, w=0.9, skew=-0.08))
# ---- inside the box (rest state)
PK = dict(pelvis=dict(pos=(0, 0, 0.17)), legs=v_khan._STAND, arms=v_khan._DOWN, face=dict(F_HOPE_K, mouth=dict(type="smile", curve=0.1, w=0.4)), dyn=dict(HOOD, zf=0.580), ground=False)
PB = dict(pelvis=dict(pos=(0, 0, 0.19)), legs=v_binh._STAND, arms=v_binh._DOWN, face=F_HOPE_B, dyn=dict(lid=(0, 0, 0)), ground=False)
PG = dict(pelvis=dict(pos=(0, 0, 0.15)), legs=v_gang._STAND, arms=v_gang._DOWN, face=F_HOPE_G, dyn=dict(crest="open"), ground=False)
peek = []
for mod, P, tag, loc in ((v_khan, PK, "pkK", (-0.03, -0.17, 0.02)), (v_binh, PB, "pkB", (-0.30, -0.14, -0.02)), (v_gang, PG, "pkG", (0.25, -0.15, -0.115))):
    cfg = mod.build(L); L.pose(cfg, P); peek.append(L.freeze(tag, loc=loc, keep_rig=False))
# ---- out of the box (reveal): Khan in front looking straight at the newcomer, the other two at its shoulders
EK = dict(pelvis=dict(pos=(0, 0, 0.172), rot=(-3, 0, 3)), chest=(-2, 0, 2), legs=dict(L=dict(ankle=(0.105, -0.03), yaw=20), R=dict(ankle=(-0.095, 0.01), yaw=6)),
          arms=dict(L=dict(upper=(0.75, -0.15, 0.85), fore=(0.45, -0.15, 1)), R=dict(upper=(-0.45, 0, -1), fore=(-0.25, -0.15, -1))), face=F_HOPE_K, dyn=dict(HOOD))
EB = dict(pelvis=dict(pos=(0, 0, 0.19), rot=(2, 10, -4)), chest=(0, 0, -2), legs=v_binh._STAND,
          arms=dict(L=dict(upper=(0.4, 0, -1), fore=(0.2, -0.15, -1)), R=dict(upper=(-0.8, -0.2, 0.7), fore=(-0.3, -0.2, 1))), face=F_HOPE_B, dyn=dict(lid=(14, -6, 0.004)))
EG = dict(pelvis=dict(pos=(0, 0, 0.15), rot=(0, -10, 4)), head=(0, 0, 4), legs=v_gang._STAND,
          arms=dict(L=dict(upper=(0.9, -0.1, 0.5), fore=(0.3, -0.2, 1)), R=dict(upper=(-0.6, 0, -1), fore=(-0.25, -0.2, -1))), face=F_HOPE_G, dyn=dict(crest="open"))
ends = {}
for mod, P, tag, loc in ((v_khan, EK, "khan", (0.02, -0.74, 0)), (v_binh, EB, "binh", (-0.47, -0.50, 0)), (v_gang, EG, "gang", (0.50, -0.48, 0))):
    cfg = mod.build(L); L.pose(cfg, P); ends[tag] = L.freeze(tag, loc=loc, keep_rig=False)

# ---- the box, turned to face the camera; its lid propped open from the back edge
L.plain("card", "#C9995F", rough=0.9); L.plain("card_in", "#8F6638", rough=0.95); L.plain("marker", "#3A2A1E", rough=0.8); L.plain("tape", "#E9D9B8", rough=0.6)
L.plain("rubber", "#33384C", rough=0.75); L.plain("steel", "#C9CDD8", rough=0.3)
W, D, H, t = 0.92, 0.70, 0.46, 0.014
boxr = bpy.data.objects.new("BoxRoot", None); S["col"].objects.link(boxr)
box = [L.box("BxF", (W, t, H), (0, -D / 2, H / 2), "card", bevel=0.004), L.box("BxB", (W, t, H), (0, D / 2, H / 2), "card_in", bevel=0.004),
       L.box("BxL", (t, D, H), (-W / 2, 0, H / 2), "card", bevel=0.004), L.box("BxR", (t, D, H), (W / 2, 0, H / 2), "card", bevel=0.004),
       L.box("BxBot", (W, D, t), (0, 0, t / 2), "card_in", bevel=0),
       L.box("Tape", (0.085, 0.004, H * 0.50), (0.36, -D / 2 - 0.008, H * 0.26), "tape", bevel=0.001)]
tx = L.text("Lbl", "ĐỒ BỎ QUÊN", FONT, 0.132, (-0.045, -D / 2 - 0.0085, H * 0.50), "marker", rot=(90, 0, 0), extrude=0.002)
tx.rotation_euler = (radians(90), radians(-3), 0); box.append(tx)
for o in box: o.parent = boxr
lidr = bpy.data.objects.new("LidRoot", None); S["col"].objects.link(lidr)
LW, LD, LS, TILT = W + 0.05, D + 0.05, 0.060, -13
lidp = [L.box("LdTop", (LW, LD, t), (0, -LD / 2, LS), "card", bevel=0.004), L.box("LdF", (LW, t, LS), (0, -LD, LS / 2), "card", bevel=0.004),
        L.box("LdL", (t, LD, LS), (-LW / 2, -LD / 2, LS / 2), "card", bevel=0.004), L.box("LdR", (t, LD, LS), (LW / 2, -LD / 2, LS / 2), "card", bevel=0.004)]
for o in lidp: o.parent = lidr
lidr.parent = boxr; lidr.location = (0, LD / 2, H - 0.03); lidr.rotation_euler = (radians(TILT), 0, radians(1.5))
AZ = -10
boxr.location = (0, 0.20, 0); boxr.rotation_euler = (0, 0, radians(AZ))
for r in peek: r.parent = boxr          # they sit in the box, wherever the box is

def dumbbell(nm, loc, rz, tilt=0.0):
    root = bpy.data.objects.new(nm, None); S["col"].objects.link(root); parts = []
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.017, depth=0.20); h = bpy.context.object; h.data.materials.append(S["mats"]["steel"]); parts.append(h)
    for sg in (1, -1):
        bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=0.082, depth=0.075, location=(0, 0, sg * 0.105)); o = bpy.context.object
        o.data.materials.append(S["mats"]["rubber"]); md = o.modifiers.new("bev", "BEVEL"); md.width = 0.012; md.segments = 5; parts.append(o)
    for o in parts:
        o.parent = root
        for p in o.data.polygons: p.use_smooth = True
    root.rotation_euler = (0, radians(90 + tilt), radians(rz)); root.location = loc
    return parts
props = dumbbell("Db1", (0.80, 0.34, 0.072), 28) + dumbbell("Db2", (0.90, 0.06, 0.072), -18)
props += dumbbell("Db3", (-0.74, 0.30, 0.072), -30)
L.fuzz_all()
bpy.context.view_layer.update()
peekp = [bpy.data.objects[n] for r in peek for n in r["parts"] if bpy.data.objects.get(n)]
endp = {k: [bpy.data.objects[n] for n in r["parts"] if bpy.data.objects.get(n)] for k, r in ends.items()}
cam = dict(az=-10, el=5, lens=90, dist=4.3, target=(0.03, -0.15, 0.42))
groups = dict(base=box + props, lid=lidp, peek=peekp, **endp)

def show(names):
    for g, objs in groups.items():
        for o in objs: o.visible_camera = g in names
# rest state: the reveal cast must not shade the box
for objs in endp.values():
    for o in objs: o.hide_render = True
for name in ("lid", "peek"):
    show((name,)); L.shoot(os.path.join(out, "w02_" + name), cam=cam, size=SIZE, samples=SAMPLES, shadow=False, keep_rgba=True)
for objs in endp.values():
    for o in objs: o.hide_render = False
for o in lidp + peekp: o.hide_render = True
for name in ("base", "khan", "binh", "gang"):
    show((name,)); L.shoot(os.path.join(out, "w02_" + name), cam=cam, size=SIZE, samples=SAMPLES, shadow=False, keep_rgba=True)
scene = S["scene"]; camo = bpy.data.objects["Cam"]; bpy.context.view_layer.update()
Mb = boxr.matrix_world; Ml = lidr.matrix_world
pts = dict(rimL=Mb @ V((-W / 2, -D / 2, H)), rimR=Mb @ V((W / 2, -D / 2, H)), lidL=Ml @ V((-LW / 2, -LD, 0)), lidR=Ml @ V((LW / 2, -LD, 0)),
           mouth=Mb @ V((0, 0, H)), floor=V((0, -0.35, 0)))
for nm, p in pts.items():
    c = world_to_camera_view(scene, camo, p); print("PT %s %.4f %.4f" % (nm, c.x, 1 - c.y))
