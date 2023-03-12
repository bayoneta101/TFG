import pymeshlab as ml
import numpy as np
import open3d as o3d

ms1=ml.MeshSet()
ms1.load_new_mesh("HBP29-WT-ID2-HC43-LacMol-3-Espina 136.wrl")
m1=ms1.current_mesh()
print("In1 vertex:",m1.vertex_number(),"In1 faces:",m1.face_number())

ms2=ml.MeshSet()
ms2.load_new_mesh("HBP29-WT-ID2-HC43-LacMol-3-Espina 850.wrl")
m2=ms2.current_mesh()

mesh1 = o3d.geometry.TriangleMesh()
mesh1.vertices = o3d.utility.Vector3dVector(m1.vertex_matrix())
mesh1.triangles = o3d.utility.Vector3iVector(m1.face_matrix())
mesh1.compute_vertex_normals()
pcd= mesh1.sample_points_poisson_disk(3000)


'''mesh1.vertices = o3d.utility.Vector3dVector(m2.vertex_matrix())
mesh1.triangles = o3d.utility.Vector3iVector(m2.face_matrix())
pcd2= mesh1.sample_points_poisson_disk(8000)'''

radii = [0.005, 0.01, 0.02, 0.04]
rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
    pcd, o3d.utility.DoubleVector(radii))

o3d.visualization.draw_geometries([pcd, rec_mesh])
'''vertices1= m1.vertex_matrix()
triangles1 = m1.face_matrix()
vertices2 = m2.vertex_matrix()
triangles2 = m2.face_matrix()'''