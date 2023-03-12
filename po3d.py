import open3d as o3d
import numpy as np
from scipy.interpolate import interp1d
import trimesh


center = (0, 0, 0)
cube = o3d.geometry.TriangleMesh.create_icosahedron(radius=1.0)
cube.compute_vertex_normals()
cube.translate(center)



center = (0, 0, 0)
cube2 = o3d.geometry.TriangleMesh.create_icosahedron(radius=1.5)
cube2.compute_vertex_normals()
cube2.translate(center)
R = cube2.get_rotation_matrix_from_xyz((0, np.pi, np.pi))# 45
#cube2.rotate(R)

vertices1 = np.asarray(cube.vertices)
triangles1 = np.asarray(cube.triangles)
vertices2 = np.asarray(cube2.vertices)
triangles2 = np.asarray(cube2.triangles)

#pcd= o3d.geometry.PointCloud()
#pcd.points = o3d.utility.Vector3dVector(vertices1)
#pcd.compute_vertex_normals()
#o3d.visualization.draw_geometries([pcd])
temp_mesh = o3d.geometry.TriangleMesh()
temp_mesh.vertices=o3d.utility.Vector3dVector(vertices1)
temp_mesh.compute_vertex_normals()
print('done')

def morbius(x,y):
    global vertices1, vertices2, triangles1, triangles2
    if x:       
        vertices1=vertices1[vertices1[:, 2].argsort()]  # sort ay day
        vertices1 = vertices1[vertices1[:, 1].argsort(kind='mergesort')]  # sort ay month
        vertices1 = vertices1[vertices1[:, 0].argsort(kind='mergesort')]
        #triangles1= triangles1[triangles1[:, 2].argsort()]  # sort ay day
        #triangles1 = triangles1[triangles1[:, 1].argsort(kind='mergesort')]  # sort ay month
        #triangles1 = triangles1[triangles1[:, 0].argsort(kind='mergesort')]
    
    if y:    
        vertices2= vertices2[vertices2[:, 0].argsort()]  # sort ay day
        vertices2 = vertices2[vertices2[:, 1].argsort(kind='mergesort')]  # sort ay month
        vertices2 = vertices2[vertices2[:, 2].argsort(kind='mergesort')]
        #triangles2=triangles2[triangles2[:, 2].argsort()]  # sort ay day
        #triangles2 = triangles2[triangles2[:, 1].argsort(kind='mergesort')]  # sort ay month
        #triangles2 = triangles2[triangles2[:, 0].argsort(kind='mergesort')]

#morbius(True,False)    
    
#print(vertices1.shape,triangles1.shape,vertices2.shape,triangles2.shape)
#print(vertices1,triangles1,vertices2,triangles2)



num_frames = 5
interp_vertices = []
interp_triangles = []#testing
for i in range(num_frames):
    alpha = i / (num_frames - 1)
    interp_vertices.append((1 - alpha) * vertices1 + alpha * vertices2)
    #interp_triangles.append((1 - alpha) * triangles1 + alpha * triangles2)
    
    alpha = 0.03
    

'''num_frames = 5
phases = np.linspace(0, 1, num_frames)
# Interpolamos los puntos de cada malla para cada fase
interp_vertices = np.zeros((num_frames, vertices1.shape[0], vertices2.shape[1]))
interp_triangles = np.zeros((num_frames, triangles1.shape[0], triangles2.shape[1]))
for i, phase in enumerate(phases):
    # Calculamos la distancia mínima entre cada punto de la primera malla y la segunda malla
    distances = o3d.geometry.PointCloud.compute_point_cloud_distance(o3d.geometry.PointCloud(vertices1), o3d.geometry.PointCloud(vertices2))
    closest_points_indices = np.argmin(distances, axis=1)

    # Interpolamos los puntos de las dos mallas utilizando la distancia mínima
    interp_vertices[i] = (1 - phase) * vertices1 + phase * vertices2[closest_points_indices]
'''
'''phases = np.linspace(0, 1, num_frames)
interp_vertices = np.zeros((num_frames, vertices1.shape[0], vertices2.shape[1]))
interp_triangles = np.zeros((num_frames, triangles1.shape[0], triangles2.shape[1]))
for i, phase in enumerate(phases):
    f = interp1d([0, 1], [vertices1, vertices2],kind='nearest', axis=0)
    interp_vertices[i] = f(phase)
    f = interp1d([0, 1], [triangles1, triangles2],kind='nearest', axis=0)
    interp_triangles[i] = f(phase)
    print(interp_vertices[i])'''


meshes = []
def visual_pre():
    global meshes
    for i in range(num_frames):
        interp_mesh = o3d.geometry.TriangleMesh()
        interp_mesh.vertices = o3d.utility.Vector3dVector(interp_vertices[i])
        interp_mesh.triangles = o3d.utility.Vector3iVector(interp_triangles[i])
        #interp_mesh.triangles = o3d.utility.Vector3iVector(triangles1)
        center = (i*5, 0, 0)
        interp_mesh.translate(center)
        meshes.append(interp_mesh)

def visualize():        
    visual_pre()   
    o3d.visualization.draw_geometries(meshes,mesh_show_wireframe=True)
'''vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(cube)
vis.run()
vis.destroy_window()'''

