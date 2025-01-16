class Fuzzy: # I create this big class in order to get a better structure of my data and functions and so that it can be easyly called in the other files.

    print("Right Edge") # To inform that got in to the class
    def __init__(self, RFS, RBS, near, medium, far, low, med, high, left, straight, right, BnearRFS, BmediumRFS, BfarRFS, BnearRBS, BmediumRBS, BfarRBS): #Initializing the variables 
        self.RFS = RFS  
        self.RBS = RBS  
        self.near = near
        self.medium = medium
        self.far = far
        self.low = low
        self.med = med
        self.high = high
        self.left = left
        self.straight = straight
        self.right = right
        self.upper_edge_RFS_value = 0
        self.lower_edge_RFS_value = 0
        self.upper_edge_RBS_value = 0
        self.lower_edge_RBS_value = 0
        self.BnearRFS = BnearRFS
        self.BmediumRFS = BmediumRFS
        self.BfarRFS = BfarRFS
        self.BnearRBS = BnearRBS
        self.BmediumRBS = BmediumRBS
        self.BfarRBS = BfarRBS

    # With the upper edge functions I go through the lists comparing the input with the elements of the lists in order to see where should I do the formulas to get the upper edge value
    # I created booleans variables as flags in order to work with them in the rules. 

    def upper_edge_RFS(self):
        for i in range(1, len(self.near)): # I start in the second element of the list in order to facilitate the value assigment of the variables.   
            if self.RFS >= self.near[i-1] and self.RFS <= self.near[i]: # if the input is equal or higher to the previous value of the list and equal or less to the actual value of the list, then...
                if self.RFS == self.near[i]: #This is a filter, to not get 0 as numerator in the formula and to avoid problems on the rules. 
                    self.upper_edge_RFS_value = 1  
                else:
                    a = self.near[i-1] # Assigning values 
                    c = self.near[i]
                    self.upper_edge_RFS_value = (c - self.RFS) / (c - a) # Getting the value of the upper edge
                self.BnearRFS = True #Activate the flag
                
        for i in range(1, len(self.medium)):  
            if self.RFS >= self.medium[i-1] and self.RFS <= self.medium[i]:
                if self.RFS == self.medium[i]:
                    self.upper_edge_RFS_value = 1
                else:
                    a = self.medium[i-1]
                    c = self.medium[i]
                    self.upper_edge_RFS_value = (c - self.RFS) / (c - a)
                self.BmediumRFS = True # Activate the flag
                self.BnearRFS = False # Desactivate the previous flag

        for i in range(1, len(self.far)):  
            if self.RFS >= self.far[i-1] and self.RFS <= self.far[i]:
                if self.RFS == self.far[i]:
                    self.upper_edge_RFS_value = 1
                else:
                    a = self.far[i-1]
                    c = self.far[i]
                    self.upper_edge_RFS_value = (c - self.RFS) / (c - a)
                self.BfarRFS = True
                self.BmediumRFS = False
            
            #Print the flags
            print(self.BnearRFS)
            print(self.BmediumRFS)
            print(self.BfarRFS)
    
    # I do the same looping method for the lower edge function just with small changes as the formula being the main one

    def lower_edge_RFS(self):
        for i in range(1, len(self.near)):  
            if self.RFS >= self.near[i-1] and self.RFS <= self.near[i]:
                a = self.near[i-1]
                b = self.near[i]
                self.lower_edge_RFS_value = (self.RFS - a) / (b - a) # input minus previous over actual minus previous
                if self.lower_edge_RFS_value != 0: # If some value has been assign to the variable, I break it here in order to just keep this value and not move on comparing as this is the lower edge.
                    break

        if self.lower_edge_RFS_value == 0: #If the value is still 0 as declared at the beggining, it gets into the function. 
            for i in range(1, len(self.medium)):  
                if self.RFS >= self.medium[i-1] and self.RFS <= self.medium[i]:
                    a = self.medium[i-1]
                    b = self.medium[i]
                    self.lower_edge_RFS_value = (self.RFS - a) / (b - a)
                    if self.lower_edge_RFS_value != 0:
                        break

        if self.lower_edge_RFS_value == 0:
            for i in range(1, len(self.far)):  
                if self.RFS >= self.far[i-1] and self.RFS <= self.far[i]:
                    a = self.far[i-1]
                    b = self.far[i]
                    self.lower_edge_RFS_value = (self.RFS - a) / (b - a)
                    if self.lower_edge_RFS_value != 0:
                        break

    # The same logic for the RBS input
                        
    def upper_edge_RBS(self):
        for i in range(1, len(self.near)):  
            if self.RBS >= self.near[i-1] and self.RBS <= self.near[i]:
                if self.RBS == self.near[i]:
                    self.upper_edge_RBS_value = 1
                else:
                    a = self.near[i-1]
                    c = self.near[i]
                    self.upper_edge_RBS_value = (c - self.RBS) / (c - a)
                self.BnearRBS = True


        for i in range(1, len(self.medium)):  
            if self.RBS >= self.medium[i-1] and self.RBS <= self.medium[i]:
                if self.RBS == self.medium[i]:
                    self.upper_edge_RBS_value = 1
                else:
                    a = self.medium[i-1]
                    c = self.medium[i]
                self.upper_edge_RBS_value = (c - self.RBS) / (c - a)
                self.BnearRBS = False
                self.BmediumRBS = True

        for i in range(1, len(self.far)):  
            if self.RBS >= self.far[i-1] and self.RBS <= self.far[i]:
                if self.RBS == self.far[i]:
                    self.upper_edge_RBS_value = 1
                else:
                    a = self.far[i-1]
                    c = self.far[i]
                    self.upper_edge_RBS_value = (c - self.RBS) / (c - a)
                self.BmediumRBS = False
                self.BfarRBS = True

    def lower_edge_RBS(self):
        for i in range(1, len(self.near)):  
            if self.RBS >= self.near[i-1] and self.RBS <= self.near[i]:
                a = self.near[i-1]
                b = self.near[i]
                self.lower_edge_RBS_value = (self.RBS - a) / (b - a)
                if self.lower_edge_RBS_value != 0:
                    break

        if self.lower_edge_RBS_value == 0:
            for i in range(1, len(self.medium)):  
                if self.RBS >= self.medium[i-1] and self.RBS <= self.medium[i]:
                    a = self.medium[i-1]
                    b = self.medium[i]
                    self.lower_edge_RBS_value = (self.RBS - a) / (b - a)
                    if self.lower_edge_RBS_value != 0:
                        break

        if self.lower_edge_RBS_value == 0:
            for i in range(1, len(self.far)):  
                if self.RBS >= self.far[i-1] and self.RBS <= self.far[i]:
                    a = self.far[i-1]
                    b = self.far[i]
                    self.lower_edge_RBS_value = (self.RBS - a) / (b - a)
                    if self.lower_edge_RBS_value != 0:
                        break


    #For the rules I find the min of the values and append it to the rules according to the speed and direction related
                        
    def calculate_firing_strength(self):
        rules = []
        
        # Applying the rule table
        if self.BnearRFS and self.BnearRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "low", "left"))
        if self.BnearRFS and self.BmediumRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "low", "left"))
        if self.BnearRFS and self.BfarRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "low", "left"))
        if self.BmediumRFS and self.BnearRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "low", "right"))
        if self.BmediumRFS and self.BmediumRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "medium", "straight"))
        if self.BmediumRFS and self.BfarRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "medium", "left"))
        if self.BfarRFS and self.BnearRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "medium", "right"))
        if self.BfarRFS and self.BmediumRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "high", "right"))
        if self.BfarRFS and self.BfarRBS:
            rules.append((min(self.upper_edge_RFS_value, self.upper_edge_RBS_value), "medium", "right"))

        print(rules)
        return rules
    
    # To get the centroid according to the values respected

    def centroid(self, values):
        centroid = (min(values) + max(values)) / len(values) # Weighted avereged formula.
        return centroid

    # The function with formulas to get the speed and direction

    def defuzzify(self, rules): # Mapping speed and direction labels to their corresponding fuzzy membership functions.
        speed_values = {"low": self.low, "medium": self.med, "high": self.high}
        direction_values = {"left": self.left, "straight": self.straight, "right": self.right}
        
        speed_numerator, direction_numerator, denominator = 0, 0, 0 # Variables to calculate 

        for (strength, speed, direction) in rules: # Iterating over each rule in the form (strength, speed, direction).
            speed_numerator += strength * self.centroid(speed_values[speed]) # Accumulates the numerator for speed using the rule's strength and the centroid of the speed's membership function.
            direction_numerator += strength * self.centroid(direction_values[direction]) # Accumulates the numerator for direction using the rule's strength and the centroid of the direction's membership function.
            denominator += strength # Accumulates the denominator which is the sum of all rule strengths.

        # Defuzzified outputs using the formulas.
        # If the denominator is 0 (to avoid division by zero), the output is set to 0.
        self.speed_output = speed_numerator / denominator if denominator != 0 else 0 # speed
        self.direction_output = -(direction_numerator / denominator) if denominator != 0 else 0 # direction. I multiply by -1 since the performance at turning was inverse at the begining.
        
        print(f"Defuzzified Speed Output: {self.speed_output}")
        print(f"Defuzzified Direction Output: {self.direction_output}")
      
    # A function to call all the functions
    def run(self):
        self.upper_edge_RFS()
        self.lower_edge_RFS()
        self.upper_edge_RBS()
        self.lower_edge_RBS()
    
        # Firing strengths based on rules
        rules = self.calculate_firing_strength()
        
        # Defuzzifying the output
        self.defuzzify(rules)


# All below was for trying my code without implementing the class to the turtlebot


# # List and variables 
# near = [0, 0.60, 0.65]
# medium = [0.6, 0.65, 0.70]
# far = [0.65, 0.7, 1.0]
# low = [0.01, 0.05, 0.1]
# med = [0.1, 0.15, 0.2]
# high = [0.2, 0.25, 0.3]
# left = [-0.3, -0.2, -0.1]
# straight = [-0.1, 0.0, 0.1]
# right = [0.1, 0.2, 0.3]

# # Variables for the rules 
# BnearRFS = False
# BmediumRFS = False
# BfarRFS = False
# BnearRBS = False
# BmediumRBS = False
# BfarRBS = False

# RFS = 1.5
# RBS = 0.2

# corre = Fuzzy(RFS = RFS, RBS = RFS, near=near, medium=medium, far=far, low=low, med=med, high=high, left=left, straight=straight, right=right, BnearRFS=BnearRFS, BmediumRFS=BmediumRFS, BfarRFS=BfarRFS, BnearRBS=BnearRBS, BmediumRBS=BmediumRBS, BfarRBS=BfarRBS)
# corre.run()

