import open3d as o3d
import numpy as np
from scipy.interpolate import interp1d
from tqdm import tqdm

# Cargar las mallas
mesh1 = o3d.io.read_triangle_mesh('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl')
mesh2 = o3d.io.read_triangle_mesh('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 850.stl')
mesh1_v=np.asarray(mesh1.vertices).shape[0]
mesh2_v=np.asarray(mesh2.vertices).shape[0]
print("In 1:",mesh1_v,"In 2:",mesh2_v)#61154 91580
# Decimar las mallas
if mesh1_v < mesh2_v:
    target_vertex=round(mesh1_v*0.1)
else:
    target_vertex=round(mesh2_v*0.1)
target_triangles=100+2*target_vertex

print("target:",target_vertex,target_triangles)
mesh1=mesh2
while (np.asarray(mesh1.vertices).shape[0] > target_vertex):
    mesh1=mesh1.simplify_quadric_decimation(target_number_of_triangles=target_triangles)
    print("Decimated to", target_triangles, "faces, mesh has", np.asarray(mesh1.vertices).shape[0], "vertex")
    target_triangles = target_triangles - (np.asarray(mesh1.vertices).shape[0] - target_vertex)

print('output mesh has', np.asarray(mesh1.vertices).shape[0], 'vertex and', 'faces')
'''
while(mesh1_decimated.vertices)
mesh1_decimated = mesh1.simplify_quadric_decimation(target_number_of_triangles=target_num_vertices)
mesh2_decimated = mesh2.simplify_quadric_decimation(target_number_of_triangles=target_num_vertices)

# Obtener los vértices decimados
vertices1 = np.asarray(mesh1_decimated.vertices)
vertices2 = np.asarray(mesh2_decimated.vertices)
print(vertices1.shape,vertices2.shape)

# Normalizar los vectores
norm1 = np.linalg.norm(vertices1, axis=1)
