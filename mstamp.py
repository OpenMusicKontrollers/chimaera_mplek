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
L0 = 50

R1 = 6

# clear scene
for item in bpy.data.objects:
	item.select = True
bpy.ops.object.delete()

# create knob
bpy.ops.mesh.primitive_uv_sphere_add(size=R1, location=(0, 0, L0))
knob = bpy.context.active_object
knob.name = "knob"
bpy.ops.transform.resize(value=(0.5, 1, 1))

# create pistill
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=R0, depth=L0, location=(0, 0, L0/2))
pistill = bpy.context.active_object
pistill.name = "pistill"

# create stamp
bpy.ops.mesh.primitive_uv_sphere_add(size=1, location=(0, 0, -H/2))
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

# merge knob with pistill 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob1 = knob.modifiers["Boolean"]
sub_knob1.name = "sub_knob1"
sub_knob1.operation = "UNION"
sub_knob1.object = pistill

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
bpy.ops.object.modifier_apply(modifier="sub_knob1")

# rotate
base.select = False
bpy.ops.transform.rotate(value=-75/180*pi, axis=(1, 0, 0))
bpy.ops.transform.translate(value=(0, 45, 14-50))

bpy.ops.object.modifier_apply(modifier="sub_knob2")
bpy.ops.object.modifier_apply(modifier="sub_knob3")
bpy.ops.object.modifier_apply(modifier="sub_knob4")

# unlink unneeded objects
scn.objects.unlink(pistill)
scn.objects.unlink(stamp)
scn.objects.unlink(bar)
scn.objects.unlink(base)

# export to Collada
bpy.ops.wm.collada_export(filepath=sys.argv[4], selected=True, apply_modifiers=True)

# export to STL
#bpy.ops.export_mesh.stl(filepath=sys.argv[4], check_existing=False, ascii=True, use_mesh_modifiers=True)

bpy.ops.wm.quit_blender()
