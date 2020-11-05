# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import math
import cmath

# Loop through the distances
# Creates an index of what 'level' the triangle is included in

levels = []
prev_d = dists_sorted[0]
i = 0
for d in dists_sorted:
    if abs(d - prev_d) > 0.0001:
        i += 1
        levels.append(i)
    else:
        levels.append(i)
    prev_d = d


