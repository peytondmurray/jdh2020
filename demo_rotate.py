import bpy
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors

obj = bpy.data.objects['Cone(0,0,0)']
mat = bpy.data.materials['Cone(0,0,0)']

for frame in range(150):
    
    fc = obj.animation_data.action.fcurves[2] # This is the 'rotation_euler' fcurve associated with the y-coordinate
    
    mz = np.cos(fc.evaluate(frame))
    normalizer = colors.Normalize(vmin=-1, vmax=1)
    
    mat.node_tree.nodes[1].inputs[0].default_value = cm.RdBu_r(normalizer(mz))
    mat.node_tree.nodes[1].inputs[0].keyframe_insert(data_path='default_value', frame=frame)
