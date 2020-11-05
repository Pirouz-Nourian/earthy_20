# AR3B011 EARTHY (2020/21 Q1)
# Zaatari Refugee Camp Heritage Center Project: "Bayt alturath"
# Group Members: Selina Bitting, Barbara Foolen de Oliveira, Inaka Sema, Yamini Patidar, Maimuna Bala Shehu


import rhinoscriptsyntax as rs
import math
import cmath



# This section is explained with diagrams in the report, however to summarize the arccos and arcsin
# are used to map out locations of the triangles by distance and angle so distance comes first, and 
# then the order moves counterclockwise from the horizontal 'seam' in the pattern on the right.


#ORDERING
############
aw = 1
dw = 100000000000
order_values = []
degs = []
dists = []
for ti in tri_info:
    sdeg = math.degrees(ti[1])
    cdeg = math.degrees(ti[2])
    if 90 >= sdeg >= 0 and 90>=cdeg>=0:
        deg = sdeg
    elif 90 >= sdeg >= 0 and 180>=cdeg>=90:
        deg = cdeg
    elif 0 >= sdeg >= -90 and 180>=cdeg>=90:
        deg = 360 - cdeg
    elif 0 >= sdeg >= -90 and 90>=cdeg>=0:
        deg = 360 + sdeg
    
    order_value = aw * deg + dw * ti[0]
    order_values.append(order_value)
    degs.append(deg)
    dists.append(ti[0])
    
def argsort(seq):
    #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    #by unutbu
    return sorted(range(len(seq)), key=seq.__getitem__)

order = argsort(order_values)


tri_sorted = [tri[id] for id in order]
degs_sorted = [degs[id] for id in order]
dists_sorted = [dists[id] for id in order]
sorted_info = [(order_values[id], degs[id], dists[id]) for id in order]  

