import numpy as np

import pyvista as pv
from scipy.interpolate import interp1d
from stl import mesh

# 'ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl'
# 'ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 850.stl'
# Cargar las mallas
mesh1 = mesh.Mesh.from_file('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl')
mesh2 = mesh.Mesh.from_file('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 850.stl')

# Obtener los vértices y las caras de ambas mallas
vertices1 = mesh1.vectors.reshape((-1, 3))
faces1 = np.arange(len(vertices1)).reshape((-1, 3))
vertices2 = mesh2.vectors.reshape((-1, 3))
faces2 = np.arange(len(vertices2)).reshape((-1, 3))

# Obtener el número total de frames
num_frames = 20

# Realizar la interpolación lineal de los vértices entre ambas mallas
vertices_interp = []
for i in range(3):
    f = interp1d([0, num_frames-1], [vertices1[:, i], vertices2[:, i]])
    vertices_interp.append(f(np.arange(num_frames)))
vertices_interp = np.stack(vertices_interp, axis=-1)

# Crear la malla inicial
malla = pv.PolyData(vertices_interp[0], faces1)

# Crear la ventana de visualización
plotter = pv.Plotter()
plotter.add_mesh(malla)

# Animar la transición de una malla a la otra
def update(frame):
    malla.points = vertices_interp[frame]
    plotter.update()

# Ejecutar la animación
plotter.show(interactive_update=True, auto_close=False)
for frame in range(num_frames):
    update(frame)
    plotter.render()
    plotter.show()
    input("Pulse enter para avanzar al siguiente frame...")