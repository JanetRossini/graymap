import bpy
import bmesh
from os.path import expanduser


def file_to_verts(file_name):
    def adj(v):
        return 2*v + 1
    rows = file_to_rows(file_name)
    return [(adj(x), adj(y), z) for y, row in enumerate(rows) for x, z in enumerate(row)]


def file_to_rows(name):
    with open(name) as f:
        rows = [line_to_ints(line) for line in f]
    return rows


def line_to_ints(line):
    return [int(t) for t in (line.split()[1:-1])]


def make_faces(n_rows, n_cols):
    faces = []
    for row in range(n_rows - 1):
        row_origin = row * n_cols
        for col in range(n_cols - 1):
            lower_left = row_origin + col
            lower_right = lower_left + 1
            upper_right = lower_right + n_cols
            upper_left = upper_right - 1
            face = (lower_left, lower_right, upper_right, upper_left)
            faces.append(face)
    return faces


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
file_name = expanduser("~/Desktop/ph-heights.txt")
vert_coords = file_to_verts(file_name)


# create and add a vertices
for coord in vert_coords:
    bm.verts.new(coord)

# create a list of vertex indices that are part of a given face
face_vert_indices= make_faces(128, 128)

bm.verts.ensure_lookup_table()

for vert_indices in face_vert_indices:
    bm.faces.new([bm.verts[index] for index in vert_indices])

# writes the bmesh data into the mesh data
bm.to_mesh(mesh_data)

# [Optional] update the mesh data (helps with redrawing the mesh in the viewport)
mesh_data.update()

# clean up/free memory that was allocated for the bmesh
bm.free()
