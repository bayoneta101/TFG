

# noinspection PyUnresolvedReferences
import vtkmodules.vtkInteractionStyle
# noinspection PyUnresolvedReferences
import vtkmodules.vtkRenderingOpenGL2
from vtk import (vtkSphereSource, vtkPolyData, vtkDecimatePro)
from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkIOGeometry import vtkSTLReader
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer
)
import vtk

def get_program_parameters():
    import argparse
    description = 'Read a .stl file.'
    epilogue = ''''''
    parser = argparse.ArgumentParser(description=description, epilog=epilogue,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('filename', help='42400-IDGH.stl')
    args = parser.parse_args()
    return args.filename


def main():
    colors = vtkNamedColors()

    #filename = get_program_parameters()
    filename ="ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl"
    
    reader = vtkSTLReader()
    reader.SetFileName(filename)
    reader.Update()
    obj=reader.GetOutputPort()
    vtkdata=reader.GetOutput()#vtkpolydata
    
    print("Before decimation\n"
          "-----------------\n"
          "There are " + str(vtkdata.GetNumberOfPoints()) + "points.\n"
          "There are " + str(vtkdata.GetPolys().GetNumberOfCells()) + "polygons.\n")
    
    decimate = vtkDecimatePro()
    decimate.SetInputData(vtkdata)
    decimate.SetTargetReduction(.80)
    decimate.Update()
    decimatedPoly = vtkPolyData()
    decimatedPoly.ShallowCopy(decimate.GetOutput())

    print("After decimation \n"
          "-----------------\n"
          "There are " + str(decimatedPoly.GetNumberOfPoints()) + "points.\n"
          "There are " + str(decimatedPoly.GetPolys().GetNumberOfCells()) + "polygons.\n")
    
    mapper = vtkPolyDataMapper()
    #mapper.SetInputConnection(obj)
    mapper.SetInputData(decimatedPoly)
    
    
    actor = vtkActor()
    actor.SetMapper(mapper)
    actor.GetProperty().SetDiffuse(0.8)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d('LightSteelBlue'))
    actor.GetProperty().SetSpecular(0.3)
    actor.GetProperty().SetSpecularPower(60.0)

    # Create a rendering window and renderer
    ren = vtkRenderer()
    renWin = vtkRenderWindow()
    renWin.AddRenderer(ren)
    renWin.SetWindowName('ReadSTL')

    # Create a renderwindowinteractor
    iren = vtkRenderWindowInteractor()
    iren.SetRenderWindow(renWin)

    # Assign actor to the renderer
    ren.AddActor(actor)
    ren.SetBackground(colors.GetColor3d('DarkOliveGreen'))

    # Enable user interface interactor
    iren.Initialize()
    renWin.Render()
    iren.Start()
    


if __name__ == '__main__':
    main()
