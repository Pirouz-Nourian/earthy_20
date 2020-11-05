# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import math
import cmath

levels = levels

#Create the list of triangles in the levels
sel_tri = []
for i in range(len(levels)):
    if levels[i]==selected_level:
        sel_tri.append(tris[i])


def addToBlock(slice,step):
    z = slice+step
    return z

# Use names to reinterpret values for next part of code

### WIP -- This part of the code will rebuild the triangles by selecting A/B/C imag/real
### Then add some z step to it in order to create a 'faceted face'
###############

triangles = complexTri_sorted
blockLevel = sel_tri

bH = blockHeight
blockFace = []
for i in range(len(levels)):
    horiz = bH*levels[i]
    stepUp = horiz + bH
    for color, A, B, C in triangles:
        Apt = rs.AddPoint(A.real, A.imag, addToBlock(horiz,stepUp))
        Bpt = rs.AddPoint(B.real, B.imag, addToBlock(horiz,stepUp))
        Cpt = rs.AddPoint(C.real, C.imag, addToBlock(horiz,stepUp))
        singleTri = rs.AddPolyline((Apt,Bpt,Cpt,Apt))
        blockFace.append(singleTri)

# Output the faces of the blocks to the next piece of code