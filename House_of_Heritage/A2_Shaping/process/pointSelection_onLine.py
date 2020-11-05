"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "pnourian"
__version__ = "2020.08.21"

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
tolerance=10E-3
chosenVertices=[]
chosenIndices=[]

for i in range(v.Count):#vertex in v:
    vertex=v[i]
    #these are all the points coming from other script
    chosen=False
    for j in range(selectionCurves.Count):
        #insideInside=(selectionCurves[j].Contains(vertex, rg.Plane.WorldXY,tolerance)==rg.PointContainment.Inside)
        a = rg.Curve.ClosestPoint(selectionCurves[j],vertex,tolerance)
        print(a)
        if a[0]==False:
                continue
        else:
            chosenVertices.append(vertex)
            chosenIndices.append(i)
    #if chosen:
        #chosenVertices.append(vertex)
        #chosenIndices.append(i)
inBandVertices=chosenVertices
inBandIndices=chosenIndices
