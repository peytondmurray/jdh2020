import bpy
import mathutils
import numpy as np
import matplotlib.cm as cm
import tqdm

scale = 0.5
step = 11       # Only show every 39th cone; this can be lowered depending on computer resources
radius = 0.5
length = 0.7
vertices = 32
time_dilation_factor = 1 # Must be int

data = np.load('data.npy')

nz, ny, nx = data.shape[1:4]

# Generate a master cone. Set the rotation mode to 'AXIS_ANGLE'
#bpy.ops.mesh.primitive_cone_add(
#    vertices=vertices,
#    radius1=radius,
#    radius2=0.0,
#    depth=length,
#    location=(0, 0, 0)
#)

master_cone = bpy.context.active_object
master_cone.rotation_mode = 'QUATERNION'
scene = bpy.context.scene

# Make a new cone object for each location. The name of the cones should include the indices, i.e., Cone(ix,iy,iz)
n_cones = 0
for iz in range(nz):
    for iy in tqdm.trange(ny, desc='Adding cones'):
        for ix in range(nx):
            if n_cones % step == 0:
                object = master_cone.copy()
                object.data = master_cone.data.copy()
                object.location = (ix*scale, iy*scale, iz*scale)
                object.name = f'Cone({ix},{iy},{iz})'
                object.rotation_mode = 'QUATERNION'
                new_mat = bpy.data.materials.new(name=f'Cone({ix},{iy},{iz})')
                new_mat.use_nodes = True
                object.data.materials.append(new_mat)
                scene.collection.objects.link(object)
            n_cones += 1

bpy.data.objects.remove(master_cone)

for i in tqdm.tqdm(range(data.shape[0]), desc='Animating frame'):
    n_cones = 0
    for iz in range(nz):
        for iy in range(ny):
            for ix in range(nx):
                if n_cones % step == 0:

                    color = cm.RdBu_r(data[i, iz, iy, ix, 2])
                    
                    name = f'Cone({ix},{iy},{iz})'
                    object = bpy.data.objects[name]
                    material = bpy.data.materials[name]
                    
                    m = mathutils.Vector(data[i, iz, iy, ix])
                    object.rotation_quaternion = m.to_track_quat('Z','Y')
                    material.node_tree.nodes[1].inputs[0].default_value = [color[0], color[1], color[2], 1]
                    material.node_tree.nodes[1].inputs[0].keyframe_insert(data_path='default_value', frame=i*time_dilation_factor)
                    object.keyframe_insert(data_path='rotation_quaternion', frame=i*time_dilation_factor)
                n_cones += 1
