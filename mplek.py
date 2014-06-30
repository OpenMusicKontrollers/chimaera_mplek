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

D = float(sys.argv[4]) # diameter of 2nd phalanx
T = 1 # wall thickness
B = 1 # bevel thickness
N = 12 # number of edges of polygonal prism
P = pi/N # edge angle of polygonal prism

prec = 1.01

W = 4 # width of bar magnet
H = 3 # height of bar magnet
L = 20 # length of bar magnet

R0 = D/2 # radius of 2nd phalanx
R1 = R0+1.5*T+H/2 # minimal radius of polygonal prism
R2 = R1/cos(P) # maximal radius of polygonal prism

C = 6 # diameter of circular magnet

cen = (0, 0, 0) # origin

# clear scene
for item in bpy.data.objects:
	item.select = True
bpy.ops.object.delete()

# create inner cyclinder, aka virtual finger
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=R0, depth=L, location=(-(H+T)/2,0,0))
inner = bpy.context.active_object
inner.name = "inner"

# create bar magnet
bpy.ops.mesh.primitive_cube_add(location=(R1-T-H/2, 0, 0))
bar = bpy.context.active_object
bar.name = "bar"
bpy.ops.transform.resize(value=(H/2*prec, W/2*prec, L/2*prec))

# create cylinder magnet
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=C/2*prec, depth=T*2, location=(R1-T*2-H, 0, 0), rotation=(0,pi/2,0))
cyl = bpy.context.active_object
cyl.name = "cyl"
cyl.select = False

# create partially cut polygonal prism
P2 = P*2
coords=[]
for i in range(0, N):
	phi = P2*i + P
	coords.append( (sin(phi)*R2, cos(phi)*R2, -L/2) )
for i in range(0, N):
	phi = P2*i + P
	coords.append( (sin(phi)*R2, cos(phi)*R2, L/4*(1+sin(phi))) )
faces = []
tmp1 = []
tmp2 = []
for i in range(0, N):
	if i+1 < N:
		faces.append( (i+1, i, N+i, N+i+1) )
	else:
		faces.append( (0, i, N+i, N) )
	tmp1.append(i)
	tmp2.append(N*2-1-i)
faces.append(tmp1)
faces.append(tmp2)
 
# create a new mesh  
mesh = bpy.data.meshes.new("polygonal_prism_mesh")
mesh.from_pydata(coords,[],faces)
mesh.update(calc_edges=True)
 
# create an object with that mesh
outer = bpy.data.objects.new("outer", mesh)
scn = bpy.context.scene
scn.objects.link(outer)
scn.objects.active = outer
outer.select = True

# add bevel modifier
bpy.ops.object.modifier_add(type="BEVEL")
bevel = outer.modifiers["Bevel"]
bevel.name = "bevel"
bevel.width = B
bevel.segments = 1

## add simple deform modifier
#bpy.ops.object.modifier_add(type="SIMPLE_DEFORM")
#simple = outer.modifiers["SimpleDeform"]
#simple.name = "simple"
#simple.angle = P

# subtract inner from outer cylinder
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_inner = outer.modifiers["Boolean"]
sub_inner.name = "sub_inner"
sub_inner.operation = "DIFFERENCE"
sub_inner.object = inner

# subtract bar from outer cylinder
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_bar = outer.modifiers["Boolean"]
sub_bar.name = "sub_bar"
sub_bar.operation = "DIFFERENCE"
sub_bar.object = bar

# subtract cyl from outer cylinder
bpy.ops.object.modifier_add(type="BOOLEAN")
sub_cyl = outer.modifiers["Boolean"]
sub_cyl.name = "sub_cyl"
sub_cyl.operation = "DIFFERENCE"
sub_cyl.object = cyl

# export to STL
bpy.ops.export_mesh.stl(filepath=sys.argv[5], check_existing=False, ascii=True, use_mesh_modifiers=True)
bpy.ops.wm.quit_blender()
