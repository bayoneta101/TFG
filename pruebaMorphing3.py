import pymeshlab as ml
import numpy as np

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


if m1.vertex_number() > m2.vertex_number():
    target_vertex=round(m1.vertex_number()*0.1)
else:
    target_vertex=round(m2.vertex_number()*0.1)
target_triangles=100+2*target_vertex
print("target vertex:",target_vertex,"target faces:",target_triangles)
print('---')
for idx,i in enumerate([ms1,ms2]):
    temp=i.current_mesh()
    print('---')
    print('Input mesh has',temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
    
    while (temp.vertex_number() > target_vertex):
        i.apply_filter('meshing_decimation_quadric_edge_collapse',targetfacenum=target_triangles)
        temp=i.current_mesh()
        print('Step mesh has', temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
        target_triangles = target_triangles - (temp.vertex_number() - target_vertex)
    
    print('output mesh has', temp.vertex_number(), 'vertex and', temp.face_number(), 'faces')
    print('---')
    if idx==0: 
        #mesh1_decimated=i 
        ms1=i
    else: 
        #mesh2_decimated=i
        ms2=i

#ms.apply_filter('meshing_decimation_quadric_edge_collapse',targetfacenum=20000)
#print(m.vertex_number(), 'vertex',m.face_number(), 'face')