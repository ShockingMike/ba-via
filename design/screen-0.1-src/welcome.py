"""Screen 0.1 art: the DO BO QUEN box on the front desk; the three via stacked inside push the lid up.
Model-sheet lock (same as kh3.py): lens 90, azimuth -10, elevation 5, vlib light rig, transparent film.
Writes three registered layers (same camera, same frame) so the page can animate them:
  out/via/screens/w01_box_rgba.png   box + desk bell          (stack and lid invisible to camera, still shading)
  out/via/screens/w01_trio_rgba.png  Gang / Binh / Khan stack
  out/via/screens/w01_lid_rgba.png   the lid, held up on Khan's hands
  out/via/screens/w01_all_rgba.png   everything together (true occlusion; reduced-motion still and reference)
Also prints RIM: the image-space y (0..1) of the box's front top edge at the left and right, for the CSS clip.

  blender -b -P welcome.py -- [--size 1200] [--nofuzz]
"""
import bpy, sys, os
from math import radians
HERE = "C:/Work/GymApp/blender/via"; sys.path.insert(0, HERE)
import vlib as L
from vlib import V, S, lib
import v_khan, v_binh, v_gang
from bpy_extras.object_utils import world_to_camera_view
argv = sys.argv[sys.argv.index("--") + 1:]
SIZE = L.argopt(argv, "--size", 1200, int); SAMPLES = L.argopt(argv, "--samples", 160, int)
L.init_scene(); L.FUZZ["on"] = "--nofuzz" not in argv

P_GANG = dict(
    pelvis=dict(pos=(0, 0, 0.128), rot=(4, 0, 0)), chest=(0, 0, 0), head=(0, 4, 0),
    legs=dict(L=dict(ankle=(0.135, -0.01), yaw=30), R=dict(ankle=(-0.135, 0.01), yaw=30)),
    arms=dict(L=dict(upper=(1, -0.15, 0.25), fore=(0.15, -0.25, 1)), R=dict(upper=(-1, -0.15, 0.25), fore=(-0.15, -0.25, 1))),
    face=dict(eyeL=dict(open=0.66, tilt=14, px=0.1, pz=0.75), eyeR=dict(open=0.52, tilt=16, px=0.1, pz=0.75),
              brows=dict(y=-0.14, tilt=20, arch=0.0), mouth=dict(type="grin", w=1.0, h=0.30, teeth=True, tongue=False, skew=0.05)),
    dyn=dict(crest="fist"))
P_BINH = dict(
    pelvis=dict(pos=(0, 0, 0.172), rot=(4, -8, 0)), belly=(0, 0, 0), chest=(0, 0, 0),
    legs=dict(L=dict(ankle=(0.085, 0.0), yaw=26), R=dict(ankle=(-0.080, 0.0), yaw=22)),
    arms=dict(L=dict(upper=(1, -0.1, 0.05), fore=(0.9, -0.2, 0.45)), R=dict(upper=(-0.8, -0.3, 0.5), fore=(0.15, -0.2, 1))),
    face=dict(eyeL=dict(open=1.0, tilt=-4, px=0.1, pz=0.2, ps=0.85), eyeR=dict(open=1.0, tilt=-8, px=0.1, pz=0.2, ps=0.85),
              browL=dict(y=0.30, tilt=-12, arch=0.3), browR=dict(y=0.18, tilt=-18, arch=0.2),
              mouth=dict(type="open", w=0.95, h=0.70, dz=0.10, teeth=True, tongue=True)),
    dyn=dict(lid=(0, 0, -0.004), ball=(0.014, 0.016)))
P_KHAN = dict(      # both hands up under the lid, looking out at the newcomer: hopeful, a bit shy
    pelvis=dict(pos=(0, 0, 0.180), rot=(-3, 0, -5)), belly=(0, 0, -2), chest=(-2, 0, -2),
    legs=dict(L=dict(ankle=(0.075, 0.0), yaw=10), R=dict(ankle=(-0.085, 0.0), yaw=14)),
    arms=dict(L=dict(upper=(0.55, -0.05, 1.0), fore=(0.25, -0.05, 1.0)), R=dict(upper=(-0.55, -0.05, 1.0), fore=(-0.25, -0.05, 1.0))),
    face=dict(eyeL=dict(open=0.95, tilt=-4, px=0.0, pz=0.1), eyeR=dict(open=0.88, tilt=-6, px=0.0, pz=0.1),
              brows=dict(y=0.14, tilt=-10, arch=0.3), mouth=dict(type="open", w=0.85, h=0.52, dz=0.06)),
    dyn=dict(mode="hood", zf=0.590, slant=0.03, fwd=0.03, tag=-80))

# ---- the stack (bottom -> top), as in scene_trio.py
cfg = v_gang.build(L); L.pose(cfg, P_GANG)
g = L.freeze("gang", loc=(0.0, 0, 0.014), rot=(0, radians(-3), radians(6)), keep_rig=False)
zt = L.top_z(g, 0.0, 0.0, 0.16)
cfg = v_binh.build(L); L.pose(cfg, P_BINH)
b = L.freeze("binh", loc=(0.035, -0.005, zt - 0.012), rot=(0, radians(5), radians(-5)), keep_rig=False)
zt2 = L.top_z(b, part="Cap"); cp = L.part_pts(b, "binh_Cap"); cx = float(cp[cp[:, 2] > zt2 - 0.03][:, 0].mean())
cfg = v_khan.build(L); L.pose(cfg, P_KHAN)
k = L.freeze("khan", loc=(cx - 0.01, 0.0, zt2 - 0.035), rot=(0, radians(-5), radians(-3)), keep_rig=False)
hp = L.part_pts(k, "khan_Hands"); hz = float(hp[:, 2].max()); hx = float(hp[:, 0].mean())
kz = L.top_z(k)
print("STACK gang top %.2f, binh top %.2f, khan hands %.2f, khan top %.2f" % (zt, zt2, hz, kz))

# ---- box, lid, desk bell
L.plain("card", "#C9995F", rough=0.9); L.plain("card_in", "#A87C48", rough=0.95); L.plain("marker", "#3A2A1E", rough=0.8); L.plain("tape", "#E9D9B8", rough=0.6)
L.plain("brass", "#E7B24A", rough=0.35); L.plain("brass2", "#B9852A", rough=0.4)
W, D, H, t = 0.90, 0.70, 0.37, 0.014
FONT = "C:/Windows/Fonts/VNF-Comic Sans.ttf"
if not os.path.exists(FONT): FONT = "C:/Windows/Fonts/arialbd.ttf"
box = [L.box("BxF", (W, t, H), (0, -D / 2, H / 2), "card", bevel=0.004), L.box("BxB", (W, t, H), (0, D / 2, H / 2), "card_in", bevel=0.004),
       L.box("BxL", (t, D, H), (-W / 2, 0, H / 2), "card", bevel=0.004), L.box("BxR", (t, D, H), (W / 2, 0, H / 2), "card", bevel=0.004),
       L.box("BxBot", (W, D, t), (0, 0, t / 2), "card_in", bevel=0),
       L.box("Tape", (0.085, 0.004, H * 0.62), (0.34, -D / 2 - 0.008, H * 0.32), "tape", bevel=0.001)]
tx = L.text("Lbl", "ĐỒ BỎ QUÊN", FONT, 0.100, (-0.07, -D / 2 - 0.0085, H * 0.47), "marker", rot=(90, 0, 0), extrude=0.0015)
tx.rotation_euler = (radians(90), radians(-3), 0); box.append(tx)
# desk bell
bx, by = 0.66, -0.20
bpy.ops.mesh.primitive_uv_sphere_add(segments=48, ring_count=24, radius=0.085, location=(bx, by, 0.022)); dome = bpy.context.object
dome.scale = (1, 1, 0.72); dome.data.materials.append(S["mats"]["brass"])
for p in dome.data.polygons: p.use_smooth = True
box += [dome, L.box("BellBase", (0.20, 0.20, 0.022), (bx, by, 0.011), "brass2", bevel=0.012),
        L.box("BellBtn", (0.030, 0.030, 0.045), (bx, by, 0.098), "brass2", bevel=0.012)]
# the lid: a shallow tray, resting on Khan's hands and the top of its hood, tipped back
lid = bpy.data.objects.new("LidRoot", None); S["col"].objects.link(lid)
LW, LD, LS = W + 0.05, D + 0.05, 0.085
lidp = [L.box("LdTop", (LW, LD, t), (0, 0, LS), "card", bevel=0.004), L.box("LdF", (LW, t, LS), (0, -LD / 2, LS / 2), "card", bevel=0.004),
        L.box("LdB", (LW, t, LS), (0, LD / 2, LS / 2), "card_in", bevel=0.004), L.box("LdL", (t, LD, LS), (-LW / 2, 0, LS / 2), "card", bevel=0.004),
        L.box("LdR", (t, LD, LS), (LW / 2, 0, LS / 2), "card", bevel=0.004)]
for o in lidp: o.parent = lid
lid.location = (hx + 0.02, 0.06, max(hz, kz) - 0.045); lid.rotation_euler = (radians(-20), radians(9), 0)
L.fuzz_all()

chars = [bpy.data.objects[n] for r in (g, b, k) for n in r["parts"] if bpy.data.objects.get(n)]
cam = dict(az=-10, el=5, lens=90, dist=6.6, target=(0.06, 0, 1.06))
out = os.path.join(L.OUT, "screens")


def show(groups):
    for grp, objs in (("box", box), ("trio", chars), ("lid", lidp)):
        for o in objs: o.visible_camera = grp in groups


if "--lidclosed" in argv:      # the lid sitting on the box (start of the animation); nothing else changes
    lid.location = (0.0, 0.0, H - LS + 0.012); lid.rotation_euler = (0, 0, radians(1.5))
    show(("lid",))
    for o in chars: o.hide_render = True          # the stack would poke through the closed lid and shade it black
    L.shoot(os.path.join(out, "w01_lidc"), cam=cam, size=SIZE, samples=80, shadow=False, keep_rgba=True)
    LAYERS = ()
else:
    LAYERS = (("all", ("box", "trio", "lid")), ("box", ("box",)), ("trio", ("trio",)), ("lid", ("lid",)))
for name, groups in LAYERS:
    show(groups)
    L.shoot(os.path.join(out, "w01_" + name), cam=cam, size=SIZE, samples=SAMPLES if name in ("all", "trio") else max(48, SAMPLES // 2), shadow=False, keep_rgba=True)
scene = S["scene"]; camo = bpy.data.objects["Cam"]; bpy.context.view_layer.update()
for nm, p in (("rimL", (-W / 2, -D / 2, H)), ("rimR", (W / 2, -D / 2, H)), ("lidC", tuple(lid.location)), ("floor", (0, -D / 2, 0))):
    c = world_to_camera_view(scene, camo, V(p)); print("RIM %s x=%.4f y=%.4f" % (nm, c.x, 1 - c.y))
