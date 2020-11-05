# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import math
import cmath


numSides = int(numSides)
subDiv = int(subDiv)
diam = diameter

goldenRatio = (1 + math.sqrt(5)) / 2


# Method & base code for drawing the penrose pattern is derived from this source:
# https://preshing.com/20110831/penrose-tiling-explained/


# Color, 0 is red and 1 is blue

# Triangles as tuples in form (color,A,B,C), and are complex numbers

# Function defining the manner of subdivision
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
# Currently prefer a decagon (typical for penrose pattern)
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

# Within the if color ==0 (or 1) statement...
# For red triangles: use the A,B,C (real [x] and imaginary [y] values. 
# Create Point3d with coordinates
# D represents the calculation of the centroid, which then gets a Point3d value.
# Centroid of Triangle: https://www.mathopenref.com/coordcentroid.html

# Calculate distances from origin (center of entire shape) to centroid of tri
# Calculate the arcsin and arcos using x and y coordinates of centroid 

# Append the geometries to redTri/bluTri and tri
# Append the information to tri_info


redTri = []
for color, A, B, C in triangles:
    if color == 0:
        Apt = rs.AddPoint(A.real, A.imag, 0)
        Bpt = rs.AddPoint(B.real, B.imag, 0)
        Cpt = rs.AddPoint(C.real, C.imag, 0)
        Dx = ((A.real+B.real+C.real)/3)
        Dy = ((A.imag+B.imag+C.imag)/3)
        Dpt = rs.AddPoint(Dx, Dy, 0)
        distToCenter = rs.Distance(origin, Dpt)
        Dsin = Dy / distToCenter
        Dcos = Dx / distToCenter
        DSa = math.asin(Dsin)
        DCa = math.acos(Dcos)
        singleTri = rs.AddPolyline((Apt,Bpt,Cpt,Apt))
        redTri.append(singleTri)
        tri.append(singleTri)
        tri_info.append([distToCenter, DSa, DCa])

bluTri = []
for color, A, B, C in triangles:
    if color == 1:
        Apt = rs.AddPoint(A.real, A.imag, 0)
        Bpt = rs.AddPoint(B.real, B.imag, 0)
        Cpt = rs.AddPoint(C.real, C.imag, 0)
        Dx = ((A.real+B.real+C.real)/3)
        Dy = ((A.imag+B.imag+C.imag)/3)
        Dpt = rs.AddPoint(Dx, Dy, 0)
        distToCenter = rs.Distance(origin, Dpt)
        Dsin = Dy / distToCenter
        Dcos = Dx / distToCenter
        DSa = math.asin(Dsin)
        DCa = math.acos(Dcos)
        singleTri = rs.AddPolyline((Apt,Bpt,Cpt,Apt))
        bluTri.append(singleTri)
        tri.append(singleTri)
        tri_info.append([distToCenter, DSa, DCa])



