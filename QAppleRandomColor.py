import bpy
import sys
import os
import time

startTime = time.time()

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )
    #print(sys.path)

import QAppleApp

# this next part forces a reload in case you edit the source after you first start the blender session
import importlib
importlib.reload(QAppleApp)

numberOfModels = 10

for l in range(numberOfModels):
    print("----------------START " + str(l) + "----------------")
    colorsArrayAndHash = QAppleApp.QAppleRandomColors()

    colorsArray = colorsArrayAndHash[0]
    colorsArray = colorsArray / 255.0
    print(colorsArray)
    hash = colorsArrayAndHash[1]

    ob = bpy.context.active_object
    totalMats = len(ob.data.materials)

    mul = 3
    matName = str("OneColor")
    #bpy.data.materials[matName].diffuse_color = 0.0, 0.0, 0.0, 1.0
    bpy.data.materials[matName].diffuse_color = colorsArray[0][0], colorsArray[0][1], colorsArray[0][2], 1.0
    """ for i in range(totalMats):
        matName = str("FaceMat_") + str(i)
        bpy.data.materials[matName].diffuse_color = colorsArray[0][(mul*i) + 0], 0.0, 0.0, 1.0 """

    """ bpy.data.collections[0].hide_viewport = False
    bpy.data.collections[0].hide_render = False
    bpy.data.collections[0].hide_select = False """

    bpy.context.layer_collection.children['Background'].exclude = True

    bpy.ops.export_scene.gltf(filepath = dir + "\\GeneratedSingle" + "\\" + hash + ".glb")

    bpy.context.layer_collection.children['Background'].exclude = False

    bpy.context.scene.render.filepath = dir + "\\GeneratedSingle" + "\\" + hash + ".png"
    bpy.ops.render.render(write_still = True)

    bpy.context.layer_collection.children['Background'].exclude = True
    print("----------------END " + str(l) + "----------------")

endTime = time.time()
print("TOTAL TIME for " + str(numberOfModels) + ": " + str(endTime - startTime))
