# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import math
import cmath

bH = blockHeight # user input
blockFace = blockFace # from piece 4
blockLevel = blockLevel # from piece 4

triangles = []
for i in range(len(blockLevel)):
  levelH = bH*blockLevel[i]
  for j in range(blockFlace):
    # take polyline from blockFace[i]
    # move vertically by bH
    triangles.append(# moved polylines)