import numpy as np
import pyvista
from pyvista import examples
import trimesh

def trimesh_():
    mesh = trimesh.load_mesh("ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl")
    #print(mesh.is_watertight)
    #print(mesh.volume)

    mesh.vertices -= mesh.center_mass#colocamos el modelo en su centro de masa
    
    #aplicamos filtro de laplaciano
    trimesh.smoothing.filter_laplacian(mesh,lamb=1,iterations=15,implicit_time_integration=False,volume_constraint=True,laplacian_operator=None)
    
    
    mesh.apply_scale(1/3)#aplicamos una reduccion de escala para que el modelo no se salga de la escena
    print(mesh.vertices.shape, mesh.faces.shape, mesh.triangles.shape, mesh.bounds)#imprimimos datos de debug
    
    mesh.show()
    
    

def pyvista_():
    #sextant_file = examples.vrml.download_sextant()
    pl = pyvista.Plotter()
    pl.import_vrml("HBP29-WT-ID2-HC43-LacMol-3-Espina 136.wrl")
    pl.show()   
 
trimesh_()    
#pyvista_()