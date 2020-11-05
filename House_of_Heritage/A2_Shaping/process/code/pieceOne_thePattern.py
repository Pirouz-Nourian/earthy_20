# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu

# Please refer to the final report for more in-depth explanations of each element of the script. 

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math
import cmath


numSides = int(numSides)
subDiv = int(subDiv)
diam = diameter

goldenRatio = (1 + math.sqrt(5)) / 2

#red triangle is 36 degree angle at apex
#blue triangle is 108 angle at apex
#color, 0 is red and 1 is blue

#triangles as tuples in form (color,A,B,C)

#Complex numbers work well here since they can represent any point on the 2D plane 
#– the real component gives the x co-ordinate, while the imaginary component 
#gives the y co-ordinate


def subdivide(triangles):
    result = []
    for color, A, B, C in triangles:
        if color == 0:
            # Subdivide red triangle
            P = A + (B - A) / goldenRatio
            result += [(0, C, P, B), (1, P, C, A)]
        else:
            # Subdivide blue triangle
            Q = B + (A - B) / goldenRatio
            R = B + (C - B) / goldenRatio
            result += [(1, R, C, A), (1, Q, R, B), (0, R, Q, A)]
    return result

# Create wheel of red triangles around the origin
triangles = []
for i in range(numSides):
    B = cmath.rect(1, (2*i - 1) * math.pi / numSides)
    B = B*(diameter/2)
    C = cmath.rect(1, (2*i + 1) * math.pi / numSides)
    C = C*(diameter/2)
    if i % 2 == 0:
        B, C = C, B  # Make sure to mirror every second triangle
    triangles.append((0, 0j, B, C))


# Perform subdivisions
for i in range(subDiv):
    triangles = subdivide(triangles)



tri = []
tri_info = []

c_coord = []
c_points = []
# centroid https://www.mathopenref.com/coordcentroid.html

for color, A, B, C in triangles:
    Apt = rg.Point3d(-A.imag, A.real, 0)
    Bpt = rg.Point3d(-B.imag, B.real, 0)
    Cpt = rg.Point3d(-C.imag, C.real, 0)
    
    
    c_coord.append([-C.imag, C.real, 0])
    c_points.append(Cpt)
    Dy = ((A.real+B.real+C.real)/3)
    Dx = -((A.imag+B.imag+C.imag)/3)
    Dpt = rg.Point3d(Dx, Dy, 0)

    distToCenter = origin.DistanceTo(Dpt)
    
    Dsin = Dy / distToCenter
    Dcos = Dx / distToCenter
    DSa = math.asin(Dsin)
    DCa = math.acos(Dcos)
    singleTri = rg.Polyline([Apt,Bpt,Cpt,Apt])

    tri.append(singleTri)
    tri_info.append([distToCenter, DSa, DCa])

