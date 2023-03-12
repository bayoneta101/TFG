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
print(vertices1,vertices2)
def morb():
    global vertices1,triangles1
    vertices1=vertices1[vertices1[:, 2].argsort()]  # sort ay day
    vertices1 = vertices1[vertices1[:, 1].argsort(kind='mergesort')]  # sort ay month
    vertices1 = vertices1[vertices1[:, 0].argsort(kind='mergesort')]
    triangles1= triangles1[triangles1[:, 2].argsort()]  # sort ay day
    triangles1 = triangles1[triangles1[:, 1].argsort(kind='mergesort')]  # sort ay month
    triangles1 = triangles1[triangles1[:, 0].argsort(kind='mergesort')]

morb()
interp_mesh = o3d.geometry.TriangleMesh()
interp_mesh.vertices = o3d.utility.Vector3dVector(vertices1)
interp_mesh.triangles = o3d.utility.Vector3iVector(triangles1)
o3d.visualization.draw_geometries([interp_mesh])
#pcd= o3d.geometry.PointCloud()
#pcd.points = o3d.utility.Vector3dVector(vertices1)
#pcd.compute_vertex_normals()
#o3d.visualization.draw_geometries([pcd])
def reconstruct():
    temp_mesh = o3d.geometry.TriangleMesh()
    pcd= o3d.geometry.PointCloud()
    temp_mesh.vertices=o3d.utility.Vector3dVector(vertices1)
    temp_mesh.compute_vertex_normals()


    pcd.points = temp_mesh.vertices
    pcd.normals= temp_mesh.vertex_normals
    radii = [0.005, 0.01, 0.02, 0.04]
    rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
        pcd, o3d.utility.DoubleVector(radii))
    o3d.visualization.draw_geometries([pcd, rec_mesh])
