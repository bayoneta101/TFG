import open3d as o3d
import numpy as np



# Cargar las mallas
mesh1 = o3d.io.read_triangle_mesh('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl')
mesh2 = o3d.io.read_triangle_mesh('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 850.stl')
mesh1_v=np.asarray(mesh1.vertices).shape[0]
mesh2_v=np.asarray(mesh2.vertices).shape[0]


# Decimar las mallas
print("In 1:",mesh1_v,"In 2:",mesh2_v)#61154 91580

#si tarda demasiado cambiar a mesh1 < mesh2
#configurado para reducir al 90 % la malla  mas pequeña
if mesh1_v > mesh2_v:
    target_vertex=round(mesh1_v*0.1)
else:
    target_vertex=round(mesh2_v*0.1)
target_triangles=100+2*target_vertex

print("target:",target_vertex,target_triangles)
mesh_array=[mesh1,mesh2]
for idx,i in enumerate(mesh_array):
    print('Input mesh has', np.asarray(i.vertices).shape[0], 'vertex')
    while (np.asarray(i.vertices).shape[0] > target_vertex):
        i=i.simplify_quadric_decimation(target_number_of_triangles=target_triangles)
        #print("Decimated to", target_triangles, "faces, mesh has", np.asarray(i.vertices).shape[0], "vertex")
        target_triangles = target_triangles - (np.asarray(i.vertices).shape[0] - target_vertex)
    print('output mesh has', np.asarray(i.vertices).shape[0], 'vertex and', 'faces')
    if idx==0: 
        #mesh1_decimated=i 
        mesh1=i
    else: 
        #mesh2_decimated=i
        mesh2=i
        
print('---')




# Obtener los vértices decimados
vertices1 = np.asarray(mesh1.vertices)
triangles1 = np.asarray(mesh1.triangles)
vertices2 = np.asarray(mesh2.vertices)
triangles2 = np.asarray(mesh2.triangles)

print(vertices1.shape,triangles1.shape,vertices2.shape,triangles2.shape)


'''# Normalizar los vectores
norm1 = np.linalg.norm(vertices1, axis=1)
norm2 = np.linalg.norm(vertices2, axis=1)
vertices1_norm = vertices1 / norm1[:, None]
vertices2_norm = vertices2 / norm2[:, None]'''


num_frames = 10
interp_vertices = []
interp_triangles = []#testing
for i in range(num_frames):
    alpha = i / (num_frames - 1)
    interp_vertices.append((1 - alpha) * vertices1 + alpha * vertices2)
#    interp_triangles.append((1 - alpha) * triangles1 + alpha * triangles2)

meshes = []
for i in range(num_frames):
    interp_mesh = o3d.geometry.TriangleMesh()
    interp_mesh.vertices = o3d.utility.Vector3dVector(interp_vertices[i])
    interp_mesh.triangles = mesh1.triangles
    meshes.append(interp_mesh)
    
o3d.visualization.draw_geometries(meshes,mesh_show_wireframe=True)