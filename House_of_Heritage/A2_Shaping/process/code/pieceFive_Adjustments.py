# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import Rhino.Geometry as rg
import Rhino as rh
import rhinoscriptsyntax as rs

import ghpythonlib.components as ghc


import math



adj_levels = []
test = []



# The pattern for the i values and ranges was found by trial and error
# the report elaborates on these strings, but basically the displacement must be adjusted for certain
# groups of triangles. This is where that happens.

for i in range(len(all_pairs)):
    if 0<= i <= 11:
        for j in range(len(all_pairs[i])):
            x = (i)
            adj_levels.append(x)
    elif 12<= i <= 15:
        i = i-9
        for j in range(len(all_pairs[i])):
            x =(i)
            adj_levels.append(x)

    elif 16<= i <= 18:
        i = i-7
        for j in range(len(all_pairs[i])):
            x =(i)
            adj_levels.append(x)
    elif i==19:
        i = i -9
        for j in range(len(all_pairs[i])):
            x = (i)
            adj_levels.append(x)

    elif i==20:
        i = i -9
        for j in range(len(all_pairs[i])):
            x = (i)
            adj_levels.append(x)
    elif 21<= i <= 23:
        i = i -12
        for j in range(len(all_pairs[i])):
            x = (i)
            adj_levels.append(x)
    elif i==24:
        i = 0
        for j in range(len(all_pairs[i])):
            x = (i)+8
            adj_levels.append(x)
#wrong point
    elif i==25:
        i = 1
        for j in range(len(all_pairs[i])):
            x = (i)+6
            adj_levels.append(x)
