# The aim of this script is to generate the necessary areas for the communal or family dwelling based on the number of people convert it into the measurements of the modular system
# The no. of modular blocks for each space are then converted into clusters of necessary proportions.
# The logic for connecting them with the courtyard is established and the blocks are split into lists based on directions and floors.
import math
nos = 13  # number_of_people
module_size = 2.25
final_module_matrices = []

# We take out the areas required for each space based on research and referances . The number of people and the area required per person is used to generate the areas for each space


def area_distribution_communal_dwelling(nos):
    Entrance = nos * 0.45
    Living_room = nos * 1.4
    Kitchen = nos * 1.2
    Courtyard = nos*2.25
    Iwan = nos * 0.9
    Farm = nos * 3.0
    Equipment_room = nos * 0.2
    areas = {"Courtyard": Courtyard, "Entrance": Entrance, "Iwan": Iwan,
             "Living_room": Living_room, "Kitchen": Kitchen, "Farm": Farm}
    return areas


# Taking out the modules from the areas
area_com_dwg = area_distribution_communal_dwelling(nos)
courtyard_blocks = area_com_dwg.values()
courtyard_blocks_values = []
for i in courtyard_blocks:
    a = int(int(i) / module_size)
    courtyard_blocks_values.append(a)

# print(courtyard_blocks_values)

# Defiing matrix for variable number of modules in a space based on the perfect proportions of a rectangle


def matrix_generator_for_functions(a):
    perfect_square = []
    y_grid = []
    for i in range(1, a+1):
        b = i*i
        if b <= a:
            perfect_square.append(b)

    c = math.sqrt(perfect_square[-1])
    d = a-perfect_square[-1]
    if d < c:
        y_grid.append(c)
    elif c < d < c*2:
        y_grid.append(c+1)
    else:
        y_grid.append(c+2)
    matrix = (int(c), int(y_grid[0]))

    return matrix

# print (matrix_generator_for_functions(25))


for i in courtyard_blocks_values:
    a = matrix_generator_for_functions(i)
    final_module_matrices.append(a)

#print (final_module_matrices)

#print (area_distribution_communal_dwelling(nos))

# Defining the blocks for the fixed size areas based on number of people(fixed number of modules per space)


def no_modules_bedroom_toilet(nos):
    a = nos % 2
    if a > 0:
        b = nos+1
    else:
        b = nos
    Bedroom_num = int(b/2)
    Toilet_shower_num = int(b/3)
    return Bedroom_num, Toilet_shower_num


matrix_for_Bedrooms = []
priority_list_Bedrooms = []
priority_list_Toilets = []
matrix_for_toilets = []
bedroom_no = (no_modules_bedroom_toilet(nos))[0]
toilet_no = (no_modules_bedroom_toilet(nos))[1]
print(bedroom_no,"bedroom_no")
for i in range(bedroom_no):
    i = (2, 3)
    matrix_for_Bedrooms.append(i)
    priority_list_Bedrooms.append([2, 1, 3, 0])

for i in range(toilet_no):
    i = (2, 2)
    matrix_for_toilets.append(i)
    priority_list_Toilets.append([3, 0, 1, 2])
farm = [final_module_matrices[5]]
split_index = len(final_module_matrices) + \
    len(matrix_for_Bedrooms) + len(matrix_for_toilets)
final_list_of_modules = final_module_matrices[1:4] + \
    matrix_for_Bedrooms + matrix_for_toilets + farm
final_list_of_modules.insert(1,(2,3))
print(final_list_of_modules)
extracting_minimum_segments = []
for i in final_list_of_modules:
    a = i[0]
    extracting_minimum_segments.append(a)

minimum_segments_required = sum(extracting_minimum_segments)

#print (final_list_of_modules)
# We check if the available segments match the required segments
courtyard_matrix = final_module_matrices[0]
available_segments_for_connection = (
    courtyard_matrix[0]+1) * (courtyard_matrix[1]+1)
print(minimum_segments_required)
riwan_matrix = [(courtyard_matrix[0]+2), (courtyard_matrix[1]+2)]
# generate the sides of the riwaq based on directions
# function which generates the numbers for the sides in each direction


def number_sides_direction(a, b):
    sides = []
    d = a+b
    for i in range(a, d):
        c = i
        sides.append(c)
    return sides

#Not nneded maybe better to takeout in grasshopper 
"""
East_sides = number_sides_direction(0, courtyard_matrix[0])
North_sides = number_sides_direction(East_sides[-1]+1, courtyard_matrix[1])
West_sides = number_sides_direction(North_sides[-1]+1, courtyard_matrix[0])
South_sides = number_sides_direction(West_sides[-1]+1, courtyard_matrix[1])
print(East_sides, North_sides, West_sides, South_sides)
"""

# lengths East,North,West,South in the stated order
Direction_Lengths = [riwan_matrix[0],
                     riwan_matrix[1], riwan_matrix[0], riwan_matrix[1]]
lengths_spaces = extracting_minimum_segments
# Priority List : Entrance, Iwan, Living Room , Kitchen, Bedroom ,Toilets, Farm
# 0 = South , 1 = East , 2= North , 3= West 
priority_list_incremental_spaces = [
    [0, 1, 2, 3], [0, 3, 1, 2], [2, 1, 3, 0], [1, 3, 2, 0]]
priority_list_all_spaces = priority_list_incremental_spaces + \
    priority_list_Bedrooms + priority_list_Toilets + [[2, 3, 0, 1]]
#print (len(priority_list_all_spaces))
print (len(lengths_spaces))
print((extracting_minimum_segments),"lengths_spaces")
print(priority_list_all_spaces)
print(Direction_Lengths)
# expected output = [0,2,0,3]
# The expected output from this step is to generate 4 lists in the cardinal directions containing tuples of the space modules
priority_list_all_spaces_index = range(len(priority_list_all_spaces))
Result_of_lists = [[], [], [], []]
Remainder_spaces = []
for i in range(len(lengths_spaces)):
    inputValueCurrentlyBeingRead = lengths_spaces[i]
    pList = priority_list_all_spaces[i]
    #print (inputValueCurrentlyBeingRead)
    print("pList", pList)
    for j in range(len(pList)):
        selectedPriorityValue = pList[j]
        spaceAvailableInSelectedLocation = Direction_Lengths[selectedPriorityValue]
        print("spaceAvailableInSelectedLocation",
              spaceAvailableInSelectedLocation)
        print("selectedPriorityValue", selectedPriorityValue)
        if spaceAvailableInSelectedLocation >= inputValueCurrentlyBeingRead:
            Direction_Lengths[selectedPriorityValue] = spaceAvailableInSelectedLocation - \
                inputValueCurrentlyBeingRead
            Result_of_lists[selectedPriorityValue].append(
                final_list_of_modules[i])
            break
        elif j == (len(pList))-1:
            print("for loop complete")
            Remainder_spaces.append(final_list_of_modules[i])


East_Direction = Result_of_lists[1]
North_Direction = Result_of_lists[2]
West_Direction = Result_of_lists[3]
South_Direction = Result_of_lists[0]

print(South_Direction,East_Direction, North_Direction, West_Direction)
print(Remainder_spaces)

# Things left to do :
# Setting priority number for first floor elements 
# Defining staircase
# Scripting for combined courtyards