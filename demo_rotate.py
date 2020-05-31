"""For the initial explanation at the beginning of the animation, use the
RdBu_r matplotlib colormap to set the color of the cone at (0, 0) from the
z-component of the cone orientation.
"""
import bpy
import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as colors

# Get the first cone and its corresponding material. This cone is manipulated
# as part of the explanation at the beginning of the animation.
obj = bpy.data.objects['Cone(0,0,0)']
mat = bpy.data.materials['Cone(0,0,0)']

for frame in range(150):

    # This is the 'rotation_euler' fcurve associated with the y-coordinate
    fc = obj.animation_data.action.fcurves[2]

    mz = np.cos(fc.evaluate(frame))
    normalizer = colors.Normalize(vmin=-1, vmax=1)

    # mat.node_tree.nodes[1] is the Principled BSDF shader which sets
    # the color of the cone.
    mat.node_tree.nodes[1].inputs[0].default_value = cm.RdBu_r(normalizer(mz))
    mat.node_tree.nodes[1].inputs[0].keyframe_insert(data_path='default_value', frame=frame)
