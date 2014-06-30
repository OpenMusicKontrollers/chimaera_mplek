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

# create pistill
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=R0, depth=L0, location=(0, 0, L0/2))
pistill = bpy.context.active_object
pistill.name = "pistill"

# create stamp
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=1, depth=1, location=(0, 0, 0))
stamp = bpy.context.active_object
stamp.name = "stamp"
bpy.ops.transform.resize(value=(W * 1.2, L/2, H*2))

# create bar magnet
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
bar = bpy.context.active_object
bar.name = "bar"
bpy.ops.transform.resize(value=(W/2*prec, L/2*prec, H/2*prec))

scn = bpy.context.scene
scn.objects.active = knob
knob.select = True

# merge knob with pistill 
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob = knob.modifiers["Boolean"]
sub_knob.name = "sub_knob"
sub_knob.operation = "UNION"
sub_knob.object = pistill

# add simple smooth modifier
#bpy.ops.object.modifier_add(type="SMOOTH")
#simple = knob.modifiers["Smooth"]
#simple.name = "smooth"
#simple.factor = 1
#simple.iterations = 10
#simple.use_x = False
#simple.use_y = False
#simple.use_z = True

# merge knob with stamp
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob2 = knob.modifiers["Boolean"]
sub_knob2.name = "sub_knob2"
sub_knob2.operation = "UNION"
sub_knob2.object = stamp

# subtract bar from stamp 
#scn.objects.active = stamp
#stamp.select = True
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_knob3 = knob.modifiers["Boolean"]
sub_knob3.name = "sub_knob3"
sub_knob3.operation = "DIFFERENCE"
sub_knob3.object = bar

# export to STL
bpy.ops.export_mesh.stl(filepath=sys.argv[4], check_existing=False, ascii=True, use_mesh_modifiers=True)
bpy.ops.wm.quit_blender()
