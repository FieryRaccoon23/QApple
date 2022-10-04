import bpy
from random import random

# get the object
ob = bpy.context.active_object

# get the mesh
mesh = ob.data

# create a list with all faces
face_list = [face for face in mesh.polygons]

# remove material slots
for x in bpy.context.object.material_slots: 
    bpy.context.object.active_material_index = 0 
    bpy.ops.object.material_slot_remove() 

# delete materials  
for material in bpy.data.materials:
    if(material.name != "Leaf_Mat") and (material.name != "Stalk_Mat"):
        material.user_clear()
        bpy.data.materials.remove(material)

# toggle to edit mode
bpy.ops.object.mode_set(mode='EDIT')

# create materials
faceCount = len(face_list)

for i in range(faceCount):
    matName = str("FaceMat_") + str(i)
    newMat = bpy.data.materials.new(name=matName)
    bpy.data.materials[matName].diffuse_color = random(), random(), random(), random()
    ob.data.materials.append(newMat)

# need to set material in object mode
bpy.ops.object.mode_set(mode='OBJECT')

# assign material to faces
for i, face in enumerate(face_list):
    face.material_index = i
