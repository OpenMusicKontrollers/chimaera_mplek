# Copyright (c) 2014 Hanspeter Portner (dev@open-music-kontrollers.ch)
# 
# This documentation describes Open Hardware and is licensed under the
# CERN OHL v.1.2. You may redistribute and modify this documentation
# under the terms of the CERN OHL v.1.2. (http://ohwr.org/cernohl). This
# documentation is distributed WITHOUT ANY EXPRESS OR IMPLIED WARRANTY,
# INCLUDING OF MERCHANTABILITY, SATISFACTORY QUALITY AND FITNESS FOR A
# PARTICULAR PURPOSE. Please see the CERN OHL v.1.2 for applicable
# conditions.

import sys
import bpy
from math import pi, sin, cos

prec = 1.01

T = 1 # wall thickness
W = 4 # width of bar magnet
H = 3 # height of bar magnet
L = 20 # length of bar magnet

R0 = 3
S0 = 0.4
SG = 64

R1 = 15
L1 = R1
S1 = S0/2
O1 = R1*S1 + 0.35

# clear scene
for item in bpy.data.objects:
	item.select = True
bpy.ops.object.delete()

# create knob
bpy.ops.mesh.primitive_uv_sphere_add(segments=SG, size=R1, location=(0, 0, L1))
knob = bpy.context.active_object
knob.name = "knob"
bpy.ops.transform.resize(value=(S0, 1, 1))

# create knob1a
bpy.ops.mesh.primitive_uv_sphere_add(segments=SG, size=R1, location=(O1, 0, L1))
knob1a = bpy.context.active_object
knob1a.name = "knob1a"
bpy.ops.transform.resize(value=(S1, 1, 1))

# create knob1b
bpy.ops.mesh.primitive_uv_sphere_add(segments=SG, size=R1, location=(-O1, 0, L1))
knob1b = bpy.context.active_object
knob1b.name = "knob1b"
bpy.ops.transform.resize(value=(S1, 1, 1))

# create stamp
bpy.ops.mesh.primitive_cylinder_add(vertices=6, radius=1, location=(0, 0, -H/2), rotation=(pi/2, 0, 0))
stamp = bpy.context.active_object
stamp.name = "stamp"
bpy.ops.transform.resize(value=(W*1.2, L/2, H*2))

# create bar magnet
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bar = bpy.context.active_object
bar.name = "bar"
bpy.ops.transform.resize(value=(W/2*prec, L/2*prec, H/2*prec))

# create base 
bpy.ops.mesh.primitive_cube_add(location=(0, 0, -H*2 + (H/2-T)))
base = bpy.context.active_object
base.name = "base"
bpy.ops.transform.resize(value=(W*2, L*2, H))

scn = bpy.context.scene
scn.objects.active = knob
knob.select = True

# subtract knob1a from knob 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob1a = knob.modifiers["Boolean"]
sub_knob1a.name = "sub_knob1a"
sub_knob1a.operation = "DIFFERENCE"
sub_knob1a.object = knob1a

# subtract knob3 from knob 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob1b = knob.modifiers["Boolean"]
sub_knob1b.name = "sub_knob1b"
sub_knob1b.operation = "DIFFERENCE"
sub_knob1b.object = knob1b

# merge knob with stamp
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob2 = knob.modifiers["Boolean"]
sub_knob2.name = "sub_knob2"
sub_knob2.operation = "UNION"
sub_knob2.object = stamp

# subtract bar from stamp 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob3 = knob.modifiers["Boolean"]
sub_knob3.name = "sub_knob3"
sub_knob3.operation = "DIFFERENCE"
sub_knob3.object = bar

# subtract bar from stamp 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob4 = knob.modifiers["Boolean"]
sub_knob4.name = "sub_knob4"
sub_knob4.operation = "DIFFERENCE"
sub_knob4.object = base

# apply modifiers
bpy.ops.object.modifier_apply(modifier="sub_knob1a")
bpy.ops.object.modifier_apply(modifier="sub_knob1b")
bpy.ops.object.modifier_apply(modifier="sub_knob2")
bpy.ops.object.modifier_apply(modifier="sub_knob3")
bpy.ops.object.modifier_apply(modifier="sub_knob4")

# unlink unneeded objects
scn.objects.unlink(knob1a)
scn.objects.unlink(knob1b)
scn.objects.unlink(stamp)
scn.objects.unlink(bar)
scn.objects.unlink(base)

if(sys.argv[4].endswith(".dae")):
    # export to Collada
    bpy.ops.wm.collada_export(filepath=sys.argv[4], selected=True, apply_modifiers=True)
elif(sys.argv[4].endswith(".stl")):
    # export to STL
    bpy.ops.export_mesh.stl(filepath=sys.argv[4], check_existing=False, ascii=True, use_mesh_modifiers=True)

bpy.ops.wm.quit_blender()
