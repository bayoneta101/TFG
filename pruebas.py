import numpy as np
import trimesh

mesh = trimesh.load_mesh("ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl")
#print(mesh.is_watertight)
#print(mesh.volume)

mesh.vertices -= mesh.center_mass
#mesh.split()
mesh.show()