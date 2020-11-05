# The aim of this script is to generate the necessary areas for the communal or family dwelling based on the number of people convert it into the measurements of the modular system
# The no. of modular blocks for each space are then converted into clusters of necessary proportions.
# The logic for connecting them with the courtyard is established and the blocks are split into lists based on directions and floors.
import math 
module_size = 2.25
final_module_matrices = []


class communal_dwelling :

    def __init__(self,nos):
        self.nos = nos

    def area_distribution(self):# We take out the areas required for each space based on research and referances . The number of people and the area required per person is used to generate the areas for each space
        num = self.nos
        Entrance = num * 0.45
        Living_room = num * 5
        Kitchen = num * 1.2
        Courtyard = num*5
        Iwan = num * 0.9
        Farm = num * 3.0
        Equipment_room = num * 0.2
        areas = {"Courtyard": Courtyard, "Entrance": Entrance, "Iwan": Iwan,
                "Living_room": Living_room, "Kitchen": Kitchen, "Farm": Farm}
        return areas

    def blocks_house (self) :# Taking out the modules from the areas
        area_com_dwg = self.area_distribution()
        courtyard_blocks = list(area_com_dwg.values())
        courtyard_blocks_values =[]
        for i in courtyard_blocks:
            a = int(int(i) / module_size)
            if a < 1 :
                b = 2
            else:
                b=a
            courtyard_blocks_values.append(b)
        return courtyard_blocks_values

    def matrix_generator_for_riwaq(self,variable_a):
        a= variable_a
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
        
        if matrix[0]<=4:
             matrix_mod = (4,4)
        else: 
             matrix_mod = matrix 

        return matrix_mod
    
    def matrix_generator_for_incremental_spaces(self,variable_b):
        a= variable_b
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
        elif c < d < c*1.1:
            y_grid.append(c+1)
        else:
            y_grid.append(c+2)
        matrix = (int(c), int(y_grid[0]))
        if matrix[0]<=2:
             matrix = (2,3)
        else: 
            matrix = matrix

        return matrix
               
    def matrix_generator_for_toilets(self):
        nos =self.nos
        a = nos % 2
        if a > 0:
            b = nos+1
        else:
            b = nos
        Toilet_num = int(b/3)
        Toilet_tuples= (2,2*Toilet_num),(2,2*Toilet_num)
        Toilet_shower_list=list(Toilet_tuples)
        return Toilet_shower_list

    def riwaq_matrix (self):
        b = self.blocks_house()
        c=b[0]
        d= list(self.matrix_generator_for_riwaq(c))
        e = [x+2 for x in d]
        return e

    def Bedroom_matrix (self):
        nos =self.nos
        a = nos % 2
        if a > 0:
            b = nos+1
        else:
            b = nos
        Bedroom_num = int(b/2)
        Bedroom_matrix=[]
        for i in range(Bedroom_num):
            i= (2,3)
            Bedroom_matrix.append(i)
        return Bedroom_matrix

    def Incremental_space_matrix (self): #Living_room,Kitchen,Farm
        spaces= self.blocks_house()
        incremental_spaces=spaces[3:]
        Incremental_space_tuples= []
        for i in incremental_spaces:
            a =self.matrix_generator_for_incremental_spaces(i)
            Incremental_space_tuples.append(a)
        return Incremental_space_tuples
    
    def priority_list_definition (self):
        # Priority List : Entrance,Staircase, Iwan, Living Room,Kitchen,Farm,Toilets,Shower,Bedroom
        # 0 = South , 1 = East , 2= North , 3= West 
        priority_list_incremental_spaces = [[0, 1, 2, 3],[3, 0, 1, 2],[0, 3, 1, 2], [2, 1, 3, 0], [1, 3, 2, 0],[3, 0, 1, 2],[3, 0, 1, 2],[3, 0, 1, 2]]
        priority_list_bedroom =[]
        nos =self.nos
        a = nos % 2
        if a > 0:
            b = nos+1
        else:
            b = nos
        Bedroom_num = int(b/2)
        for i in range(Bedroom_num):
            a=[2, 1, 3, 0] 
            priority_list_bedroom.append(a)
        for i in priority_list_bedroom :
            priority_list_incremental_spaces.append(i)
        
        return priority_list_incremental_spaces

    def Final_list_of_modules_of_spaces (self):
        # Priority List : Entrance,Staircase,Iwan, Living Room,Kitchen,Farm,Toilets,Shower,Bedroom
        # 0 = South , 1 = East , 2= North , 3= West
        toilet_modules= self.matrix_generator_for_toilets()
        bedroom_modules = self.Bedroom_matrix()
        Final_list_of_modules_of_spaces=[(1,3),(2,3),(3,3)]
        Living_Kitchen_Toilet = self.Incremental_space_matrix()
        for i in Living_Kitchen_Toilet :
            Final_list_of_modules_of_spaces.append(i)
        for i in toilet_modules:
            Final_list_of_modules_of_spaces.insert(-1,i)
        for i in bedroom_modules :
            Final_list_of_modules_of_spaces.append(i)

        return Final_list_of_modules_of_spaces 
    
    def sides_available_for_connection (self):
        riwaq_matrix_extraction = self.riwaq_matrix()
        Number_of_sides = [riwaq_matrix_extraction[0],riwaq_matrix_extraction[1],riwaq_matrix_extraction[0],riwaq_matrix_extraction[1]]
        return Number_of_sides

    def smallest_side_connection_per_function (self):
        all_modules = self.Final_list_of_modules_of_spaces()
        first_value_of_tuples = []
        for i in all_modules :
            first_value_of_tuples.append(i[0])
        return first_value_of_tuples

    def Sorting_into_directions_as_per_priority(self):
        # Priority List : Entrance,Staircase,Iwan, Living Room,Kitchen,Farm,Toilets,Shower,Bedroom
        # 0 = South , 1 = East , 2= North , 3= West
        priority_list_all_spaces = self.priority_list_definition()
        Direction_Lengths = self.sides_available_for_connection() 
        lengths_spaces= self.smallest_side_connection_per_function()
        final_list_of_modules = self.Final_list_of_modules_of_spaces()
        Result_of_lists = [[], [], [], []]
        Remainder_spaces = []
        for i in range(len(lengths_spaces)):
            inputValueCurrentlyBeingRead = lengths_spaces[i]
            pList = priority_list_all_spaces[i]
            #print (inputValueCurrentlyBeingRead)
            #print("pList", pList)
            for j in range(len(pList)):
                selectedPriorityValue = pList[j]
                spaceAvailableInSelectedLocation = Direction_Lengths[selectedPriorityValue]
               # print("spaceAvailableInSelectedLocation",
                   # spaceAvailableInSelectedLocation)
               # print("selectedPriorityValue", selectedPriorityValue)
                if spaceAvailableInSelectedLocation >= inputValueCurrentlyBeingRead:
                    Direction_Lengths[selectedPriorityValue] = spaceAvailableInSelectedLocation - \
                        inputValueCurrentlyBeingRead
                    Result_of_lists[selectedPriorityValue].append(
                        final_list_of_modules[i])
                    break
                elif j == (len(pList))-1:
                   # print("for loop complete")
                    Remainder_spaces.append(final_list_of_modules[i])
        East_Direction = Result_of_lists[1]
        North_Direction = Result_of_lists[2]
        West_Direction = Result_of_lists[3]
        South_Direction = Result_of_lists[0]
        return ["SENW",East_Direction,North_Direction,West_Direction,South_Direction],["Remainder_spaces",Remainder_spaces]

    def Sorting_into_directions_as_per_priority_for_bounding_box(self):
        # Priority List : Entrance,Staircase,Iwan, Living Room,Kitchen,Farm,Toilets,Shower,Bedroom
        # 0 = South , 1 = East , 2= North , 3= West
        priority_list_all_spaces = self.priority_list_definition()
        Direction_Lengths = self.sides_available_for_connection() 
        lengths_spaces= self.smallest_side_connection_per_function()
        final_list_of_modules = self.Final_list_of_modules_of_spaces()
        Result_of_lists = [[], [], [], []]
        Remainder_spaces = []
        for i in range(len(lengths_spaces)):
            inputValueCurrentlyBeingRead = lengths_spaces[i]
            pList = priority_list_all_spaces[i]
            #print (inputValueCurrentlyBeingRead)
            #print("pList", pList)
            for j in range(len(pList)):
                selectedPriorityValue = pList[j]
                spaceAvailableInSelectedLocation = Direction_Lengths[selectedPriorityValue]
               # print("spaceAvailableInSelectedLocation",
                   # spaceAvailableInSelectedLocation)
               # print("selectedPriorityValue", selectedPriorityValue)
                if spaceAvailableInSelectedLocation >= inputValueCurrentlyBeingRead:
                    Direction_Lengths[selectedPriorityValue] = spaceAvailableInSelectedLocation - \
                        inputValueCurrentlyBeingRead
                    Result_of_lists[selectedPriorityValue].append(
                        final_list_of_modules[i])
                    break
                elif j == (len(pList))-1:
                   # print("for loop complete")
                    Remainder_spaces.append(final_list_of_modules[i])
        East_Direction = Result_of_lists[1]
        North_Direction = Result_of_lists[2]
        West_Direction = Result_of_lists[3]
        South_Direction = Result_of_lists[0]
        return [East_Direction,North_Direction,West_Direction,South_Direction]

    def Sorting_into_directions_as_per_priority_combined_dwellings(self,S,E,N,W):
        # Priority List : Entrance,Staircase,Iwan, Living Room,Kitchen,Farm,Toilets,Shower,Bedroom
        # 0 = South , 1 = East , 2= North , 3= West
        Direction_Lengths_original = self.sides_available_for_connection()
        Direction_Lengths =Direction_Lengths_original 
        input_gh_cull_index = [S,E,N,W]
        cull_index_final =[]
        for i in range(4) :
            if input_gh_cull_index[i] >0:
                cull_index_final.append(i)
        for i in cull_index_final :
           a= Direction_Lengths_original[i]*0
           Direction_Lengths_original.pop(i)
           Direction_Lengths_original.insert(i,0)
        priority_list_all_spaces = self.priority_list_definition()
        lengths_spaces= self.smallest_side_connection_per_function()
        final_list_of_modules = self.Final_list_of_modules_of_spaces()
        Result_of_lists = [[], [], [], []]
        Remainder_spaces = []
        for i in range(len(lengths_spaces)):
            inputValueCurrentlyBeingRead = lengths_spaces[i]
            pList = priority_list_all_spaces[i]
            #print (inputValueCurrentlyBeingRead)
            #print("pList", pList)
            for j in range(len(pList)):
                selectedPriorityValue = pList[j]
                spaceAvailableInSelectedLocation = Direction_Lengths[selectedPriorityValue]
                #print("spaceAvailableInSelectedLocation",
                    #spaceAvailableInSelectedLocation)
                #print("selectedPriorityValue", selectedPriorityValue)
                if spaceAvailableInSelectedLocation >= inputValueCurrentlyBeingRead:
                    Direction_Lengths[selectedPriorityValue] = spaceAvailableInSelectedLocation - \
                        inputValueCurrentlyBeingRead
                    Result_of_lists[selectedPriorityValue].append(
                        final_list_of_modules[i])
                    break
                elif j == (len(pList))-1:
                    #print("for loop complete")
                    Remainder_spaces.append(final_list_of_modules[i])
        East_Direction = Result_of_lists[1]
        North_Direction = Result_of_lists[2]
        West_Direction = Result_of_lists[3]
        South_Direction = Result_of_lists[0]
        return ["SENW",East_Direction,North_Direction,West_Direction,South_Direction],["Remainder_spaces",Remainder_spaces] 

    @property
    def Bounding_box(self):
        SENW = self.Sorting_into_directions_as_per_priority_for_bounding_box()
        South_Direction =SENW[0]
        if len(South_Direction)  == 1:
            South_Dimention = South_Direction[0][1]
        else:    
            South_Dimention =max(South_Direction[1])

        East_Direction =SENW[1]
        if len(East_Direction) == 1 :
            East_Dimention = East_Direction[0][1]
        else:    
            East_Dimention =max(East_Direction[1])

        North_Direction =SENW[2]
        if len(North_Direction) == 1 :
            North_Dimention = North_Direction[0][1]
        else:    
            North_Dimention =max(North_Direction[1])

        West_Direction =SENW[3]
        if len(West_Direction) ==  1 :
            West_Dimention = West_Direction[0][1]
        else:    
            West_Dimention =max(North_Direction[1])

        Dimentions_bounding_box = [(East_Dimention*1.5 +West_Dimention*1.5),"x", (South_Dimention*1.5 +North_Dimention*1.5) ]
        return Dimentions_bounding_box

    def num_sides_per_direction(self):
        SENW = self.Sorting_into_directions_as_per_priority_for_bounding_box()
        South_Direction =SENW[0]
        if len(South_Direction)  == 1:
            South_Dimention = South_Direction[0][1]
        else:    
            South_Dimention =max(South_Direction[1])

        East_Direction =SENW[1]
        if len(East_Direction) == 1 :
            East_Dimention = East_Direction[0][1]
        else:    
            East_Dimention =max(East_Direction[1])

        North_Direction =SENW[2]
        if len(North_Direction) == 1 :
            North_Dimention = North_Direction[0][1]
        else:    
            North_Dimention =max(North_Direction[1])

        West_Direction =SENW[3]
        if len(West_Direction) ==  1 :
            West_Dimention = West_Direction[0][1]
        else:    
            West_Dimention =max(North_Direction[1])

        return South_Dimention , East_Dimention , North_Dimention , West_Dimention

Family_1 = communal_dwelling(13)
print(Family_1.Sorting_into_directions_as_per_priority_combined_dwellings(0,1,1,0))
#print(Family_1.riwaq_matrix())
print(Family_1.Bounding_box)

