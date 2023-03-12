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
print("In2 vertex:",m2.vertex_number(),"In2 faces:",m2.face_number())
#print(ml.print_filter_parameter_list('discrete_curvatures'))
print('---')

reduction_factor=0.10
if m1.vertex_number() > m2.vertex_number():
    target_vertex=round(m1.vertex_number()*reduction_factor)
else:
    target_vertex=round(m2.vertex_number()*reduction_factor)
target_triangles=100+2*target_vertex
print("target vertex:",target_vertex,"target faces:",target_triangles)
print('---')
for idx,i in enumerate([ms1,ms2]):
    temp=i.current_mesh()
    print('---')
    print('Input mesh has',temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
    
    while (temp.vertex_number() > target_vertex):
        i.apply_filter('meshing_decimation_quadric_edge_collapse',targetfacenum=target_triangles,preservetopology=False,preservenormal=True,optimalplacement=False)
        temp=i.current_mesh()
        print('Step mesh has', temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
        target_triangles = target_triangles - (temp.vertex_number() - target_vertex)
    
    print('output mesh has', temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
    print('---')
    if idx==0: 
        #mesh1_decimated=i 
        ms1=i
        m1=ms1.current_mesh()
    else: 
        #mesh2_decimated=i
        ms2=i
        m2=ms2.current_mesh()
        
vertices1= m1.vertex_matrix()
triangles1 = m1.face_matrix()
vertices2 = m2.vertex_matrix()
triangles2 = m2.face_matrix()
print(vertices1.shape,triangles1.shape,vertices2.shape,triangles2.shape)
#ms.apply_filter('meshing_decimation_quadric_edge_collapse',targetfacenum=20000)
#print(m.vertex_number(), 'vertex',m.face_number(), 'face')

'''#Normalizar los vectores
norm1 = np.linalg.norm(vertices1, axis=1)
norm2 = np.linalg.norm(vertices2, axis=1)
vertices1 = vertices1 / norm1[:, None]
vertices2 = vertices2 / norm2[:, None]'''

num_frames = 10
interp_vertices = []
interp_triangles = []#testing
interp_mesh=[]
for i in range(num_frames):
    alpha = i / (num_frames - 1)
    interp_vertices.append((1 - alpha) * vertices1 + alpha * vertices2)
    interp_triangles.append((1 - alpha) * triangles1 + alpha * triangles2)
    #msFrom=ms1
    #msTo=ms2
    #percmorph=alpha*100
    #msFrom.apply_filter('compute_coord_linear_morphing',targetmesh=msTo)
    #interp_mesh.append(msFrom)
    
meshes = []
for i in range(num_frames):
    interp_mesh = o3d.geometry.TriangleMesh()
    interp_mesh.vertices = o3d.utility.Vector3dVector(interp_vertices[i])
    interp_mesh.triangles = o3d.utility.Vector3iVector(interp_triangles[i])
    #interp_mesh.vertices = o3d.utility.Vector3dVector(interp_mesh[i].current_mesh().vertex_matrix())
    #interp_mesh.triangles = o3d.utility.Vector3iVector(interp_mesh[i].current_mesh().face_matrix())
    meshes.append(interp_mesh)
    
o3d.visualization.draw_geometries(meshes,mesh_show_wireframe=True)