import bpy
import mathutils
import numpy as np
import matplotlib.cm as cm
import re
import tqdm

time_dilation_factor = 10 # Must be int

for action in tqdm.tqdm(bpy.data.actions, desc='Actions'):
    for fcurve in action.fcurves:
        for point in fcurve.keyframe_points:
            point.co.x *= time_dilation_factor
            point.handle_left.x *= time_dilation_factor
            point.handle_right.x *= time_dilation_factor