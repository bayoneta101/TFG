import vtk

def decimation():
    
    reader = vtk.vtkSTLReader()
    reader.SetFileName('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl')
    reader.Update()
    obj1 = reader.GetOutput()
    mesh1=obj1.GetOutput()#vtkpolydata
    
    reader2 = vtk.vtkSTLReader()
    reader2.SetFileName('ImageToStl.com_hbp29-wt-id2-hc43-lacmol-3-espina 136.stl')
    reader2.Update()
    obj2 = reader2.GetOutput()
    mesh2=obj2.GetOutput()#vtkpolydata
    
    print("Before decimation\n"
          "-----------------\n"
          "There are " + str(inputPoly.GetNumberOfPoints()) + "points.\n"
          "There are " + str(inputPoly.GetNumberOfPolys()) + "polygons.\n")

    decimate = vtkDecimatePro()
    decimate.SetInputData(inputPoly)
    decimate.SetTargetReduction(.10)
    decimate.Update()

    decimatedPoly = vtkPolyData()
    decimatedPoly.ShallowCopy(decimate.GetOutput())

    print("After decimation \n"
          "-----------------\n"
          "There are " + str(decimatedPoly.GetNumberOfPoints()) + "points.\n"
          "There are " + str(decimatedPoly.GetNumberOfPolys()) + "polygons.\n")


if __name__ == "__main__":
    decimation()