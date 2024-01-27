import bpy
import bmesh

obj_name = "my_shape"

# create the mesh data
mesh_data = bpy.data.meshes.new(f"{obj_name}_data")

# create the mesh object using the mesh data
mesh_obj = bpy.data.objects.new(obj_name, mesh_data)

# add the mesh object into the scene
bpy.context.scene.collection.objects.link(mesh_obj)

# create a new bmesh
bm = bmesh.new()

# create a list of vertex coordinates
vert_coords = [
    (1, 1, 0),
    (2, 1, 1),
    (3, 1, 2),
    (4, 1, 3),

    (1, 2, 0),
    (2, 2, 4),
    (3, 2, 4),
    (4, 2, 2),

    (1, 3, 0),
    (2, 3, 4),
    (3, 3, 4),
    (4, 3, 1),

    (1, 4, 0),
    (2, 4, 0),
    (3, 4, 0),
    (4, 4, 0),
]

# create and add a vertices
for coord in vert_coords:
    bm.verts.new(coord)

# create a list of vertex indices that are part of a given face
face_vert_indices = [
    (0, 1, 5, 4),
    (1, 2, 6, 5),
    (2, 3, 7, 6),

    (4, 5, 9, 8),
    (5, 6, 10, 9),
    (6, 7, 11, 10),

    (8, 9, 13, 12),
    (9, 10, 14, 13),
    (10, 11, 15, 14)
]

bm.verts.ensure_lookup_table()

for vert_indices in face_vert_indices:
    bm.faces.new([bm.verts[index] for index in vert_indices])

# writes the bmesh data into the mesh data
bm.to_mesh(mesh_data)

# [Optional] update the mesh data (helps with redrawing the mesh in the viewport)
mesh_data.update()

# clean up/free memory that was allocated for the bmesh
bm.free()
