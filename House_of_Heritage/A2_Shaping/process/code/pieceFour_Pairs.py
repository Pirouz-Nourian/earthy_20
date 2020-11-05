# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math
import cmath


levels = levels
tris = tris

# Here the triangles are numbered within their rings, such that ring/level 1 has triangle 0,1,2,3 and ring/level2 has triangle 0,1,2,3 in order
# to later pair them up with the order pattern



tris_leveled = []
this_level = []
for i, t in enumerate(tris):
    this_level.append(t)
    if levels[i] != levels[(i+1)%len(tris)]:
        tris_leveled.append(this_level)
        this_level = []

# The below order is found by manually going through the pattern and finding the pairs according to the defined logic. 

order = [[0,1], [1,2], [2,3], [3,5],[5,7],[7,10],[10,12],[12,13],[13,17],[17,20],[20,25],[25,26],[4,6],[6,9],[9,11],[11,14],[14,16],[16,21],[21,24],[18,22],[22,28],[19,23],[23,27],[27,31], [15,20],[14,15]]
all_pairs = []


# Here the pattern is fed to a loop, which then pulls the relevant triangles and gets (for example):
# triangle 0 of ring 0 and pairs it with triangle 0 of ring/level 1

for o in order:
    first_pairs = tris_leveled[o[0]]
    second_pairs = tris_leveled[o[1]]
    this_pairs = zip(first_pairs, second_pairs)
    all_pairs.append(this_pairs)

    

selected_pairs=[item for sublist in all_pairs[sel] for item in sublist]
