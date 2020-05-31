"""When keyframing rotations using quaternions in blender, the automatically
generated fcurves sometimes set erroneous orientations. As far as I can tell,
this arises from the fact that the method that blender uses to interpolate
between keyframes is not rotation-aware. As a simplified example, if

    Keyframe 1: orientation angle = 2°
    Keyframe 2: orientation angle = 358°

blender sets the orientation angle 180° at the frame in between the keyframes,
rather than 0° (as it should be).

This script examines every fcurve searching for these erroneous orientations,
and flips the object if need be.

Modified from https://blender.stackexchange.com/questions/58866/keyframe-interpolation-instability
"""
import bpy
from mathutils import Quaternion
import tqdm

for action in tqdm.tqdm(bpy.data.actions, desc='Actions'):

    # quaternion curves
    fqw = action.fcurves.find('rotation_quaternion', index = 0)
    fqx = action.fcurves.find('rotation_quaternion', index = 1)
    fqy = action.fcurves.find('rotation_quaternion', index = 2)
    fqz = action.fcurves.find('rotation_quaternion', index = 3)

    # invert quaternion so that interpolation takes the shortest path
    if fqw is not None and fqw.keyframe_points is not None and len(fqw.keyframe_points) > 0:
        endQuat = Quaternion(
            (
                fqw.keyframe_points[0].co[1],
                fqx.keyframe_points[0].co[1],
                fqy.keyframe_points[0].co[1],
                fqz.keyframe_points[0].co[1]
            )
        )

        for i in range(len(fqw.keyframe_points)-1):
            startQuat = endQuat
            endQuat = Quaternion(
                (
                    fqw.keyframe_points[i+1].co[1],
                    fqx.keyframe_points[i+1].co[1],
                    fqy.keyframe_points[i+1].co[1],
                    fqz.keyframe_points[i+1].co[1]
                )
            )

            if startQuat.dot(endQuat) < 0:
                endQuat.negate()
                fqw.keyframe_points[i+1].co[1] = -fqw.keyframe_points[i+1].co[1]
                fqx.keyframe_points[i+1].co[1] = -fqx.keyframe_points[i+1].co[1]
                fqy.keyframe_points[i+1].co[1] = -fqy.keyframe_points[i+1].co[1]
                fqz.keyframe_points[i+1].co[1] = -fqz.keyframe_points[i+1].co[1]
