# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import Rhino.Geometry as rg
import Rhino as rh
import rhinoscriptsyntax as rs

import ghpythonlib.components as ghc


import math

origin = rs.AddPoint(origin)


# This portion takes the triangle and gets its vertices. Then, the vertices are tested to find which is closest
# to the origin point. This is then returned separately from the other points.

def getCorners (curve):
    seg = rg.Polyline.GetSegments(curve)
    corners = []
    
    dist = []
    for i in seg:
        lineseg = rg.Line.ToNurbsCurve(i)
        pt = rg.NurbsCurve.PointAtEnd.GetValue(lineseg)
        corners.append(pt)
    new = rs.AddPolyline([corners[0],corners[1],corners[2],corners[0]])
    pts = rs.PolylineVertices(new)
    pts = rs.CullDuplicatePoints(pts)
    test = rs.Distance(origin,pts)
    minDist = min(test)
    #print(minDist)
    index = test.index(minDist)
    minPoint = pts[index]
    #print(minPoint)
    del pts[index]
    cornerPoints = pts
    #print(len(cornerPoints))
    return cornerPoints[0],cornerPoints[1], minPoint

# This picks an arbitrary point of the triangle

def getOneCorner (curve):
    seg = rg.Polyline.GetSegments(curve)
    lineseg = rg.Line.ToNurbsCurve(seg[0])
    pt = rg.NurbsCurve.PointAtEnd.GetValue(lineseg)
    corner = pt
    return corner

# The points are displaced by the brick height, and then all added to one list with the four corners.

def duplicatePoints(corner_one,corner_two):
    corner_one = rs.AddPoint(corner_one)
    corner_two = rs.AddPoint(corner_two)
    one = rs.PointCoordinates(corner_one)
    z_one = one[2]-bH
    new_corner_one = rs.AddPoint(one[0],one[1],z_one)
    #new_corner_one = rs.CreatePoint(one[0],one[1],z_one)
    two = rs.PointCoordinates(corner_two)
    z_two = two[2]-bH
    new_corner_two = rs.AddPoint(two[0],two[1],z_two)
    #new_corner_two = rs.CreatePoint(two[0],two[1],z_two)
    four_corners = []
    four_corners.append(corner_one)
    four_corners.append(corner_two)
    four_corners.append(new_corner_two)
    four_corners.append(new_corner_one)
    return four_corners

# Duplicate one point and displace by the brick height 

def duplicatePoint(point):
    base = rs.AddPoint(point)
    coord = rs.PointCoordinates(base)
    z_move = coord[2]-bH
    new_base = rs.AddPoint(coord[0],coord[1],z_move)
    return new_base


modules = []
points = []

vector_base = []
angle_piece = []
flat_piece = []


# an inner rectangular face is created to be used for the extrude to point command, which extrudes this 
# new rectangle toward the point closest to the origin


# the flat face is simply extruded straight

for i in range(len(all_pairs)):
    for angle,flat in all_pairs[i]:
        facet_points = getCorners(angle)
        rectangle = duplicatePoints(facet_points[0],facet_points[1])
        rectangle = rs.AddPolyline([rectangle[0],rectangle[1],rectangle[2],rectangle[3],rectangle[0]])
        angle_ext = rs.ExtrudeCurvePoint(rectangle,facet_points[2])
        flat_pointOne = getOneCorner(flat)
        flat_pointTwo = duplicatePoint(flat_pointOne)
        flat = rs.AddPolyline(flat)
        flat_ext = rs.ExtrudeCurveStraight(flat,flat_pointOne,flat_pointTwo)

        vector_base.append(flat_pointOne)
        modules.append([angle_ext,flat_ext])
        angle_piece.append(angle_ext)
        flat_piece.append(flat_ext)
        #print(flat_piece)
        
        



vertical_modules = []

new_modules = []

# the modules are displaced according to the level value multiplied by the brick height

for i in range(len(modules)):
    h = -(levels[i]*bH)
    new_angle = rs.MoveObject(angle_piece[i],[0,0,h])
    new_modules.append(new_angle)
    new_flat = rs.MoveObject(flat_piece[i],[0,0,h])
    new_modules.append(new_flat)

