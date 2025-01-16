class FuzzyAvoidFront: # I create this big class in order to get a better structure of my data and functions and so that it can be easyly called in the other files.

    print("Avoid Front") # To inform that got in to the class
    def __init__(self, FRS, FLS, F, near, medium, far, nearF, mediumF, farF, low, med, high, left, straight, right, 
                 BnearFRS, BmediumFRS, BfarFRS, BnearFLS, BmediumFLS, BfarFLS, BnearF, BmediumF, BfarF): #Initializing the variables
        self.FRS = FRS  
        self.FLS = FLS
        self.F = F
        self.near = near
        self.medium = medium
        self.far = far
        self.nearF = nearF
        self.mediumF = mediumF
        self.farF = farF
        self.low = low
        self.med = med
        self.high = high
        self.left = left
        self.straight = straight
        self.right = right
        self.upper_edge_FRS_value = 0
        self.lower_edge_FRS_value = 0
        self.upper_edge_FLS_value = 0
        self.lower_edge_FLS_value = 0
        self.upper_edge_F_value = 0
        self.lower_edge_F_value = 0
        self.BnearFRS = BnearFRS
        self.BmediumFRS = BmediumFRS
        self.BfarFRS = BfarFRS
        self.BnearFLS = BnearFLS
        self.BmediumFLS = BmediumFLS
        self.BfarFLS = BfarFLS
        self.BnearF = BnearF
        self.BmediumF = BmediumF
        self.BfarF = BfarF


    # With the upper edge functions I go through the lists comparing the input with the elements in order to see in where should I do the formulas to get the upper edge value
    # I created booleans variables as flags in order to work with them in the rules. 

    # For the Front Right Sensor
    def upper_edge_FRS(self):
        for i in range(1, len(self.near)):  # I start in the second element of the list in order to facilitate the value assigment of the variables.   
            if self.FRS >= self.near[i-1] and self.FRS <= self.near[i]: # if the input is equal or higher to the previous value of the list and equal or less to the actual value of the list, then...
                if self.FRS == self.near[i]: #This is a filter, to not get 0 as numerator in the formula and to avoid problems on the rules. 
                    self.upper_edge_FRS_value = 1
                else:
                    a = self.near[i-1] # Assigning values 
                    c = self.near[i]
                    self.upper_edge_FRS_value = (c - self.FRS) / (c - a) # Getting the value of the upper edge
                self.BnearFRS = True # Activate the flag
                
        for i in range(1, len(self.medium)):  
            if self.FRS >= self.medium[i-1] and self.FRS <= self.medium[i]:
                if self.FRS == self.medium[i]:
                    self.upper_edge_FRS_value = 1
                else:
                    a = self.medium[i-1]
                    c = self.medium[i]
                    self.upper_edge_FRS_value = (c - self.FRS) / (c - a)
                self.BmediumFRS = True # Activate the flag
                self.BnearFRS = False # Desactivate the previous flag

        for i in range(1, len(self.far)):  
            if self.FRS >= self.far[i-1] and self.FRS <= self.far[i]:
                if self.FRS == self.far[i]:
                    self.upper_edge_FRS_value = 1
                else:
                    a = self.far[i-1]
                    c = self.far[i]
                    self.upper_edge_FRS_value = (c - self.FRS) / (c - a)
                self.BfarFRS = True
                self.BmediumFRS = False

    # I do the same looping method for the lower edge function just with small changes as the formula being the main one

    def lower_edge_FRS(self):
        for i in range(1, len(self.near)):  
            if self.FRS >= self.near[i-1] and self.FRS <= self.near[i]:
                a = self.near[i-1]
                b = self.near[i]
                self.lower_edge_FRS_value = (self.FRS - a) / (b - a) # input minus previous over actual minus previous
                if self.lower_edge_FRS_value != 0: # If some value has been asign to the variable, I break it here in order to just keep this value and not move on comparing as this is the lower edge.
                    break

        if self.lower_edge_FRS_value == 0: #If the value is still 0 as declared at the beggining, it gets into the function.
            for i in range(1, len(self.medium)):  
                if self.FRS >= self.medium[i-1] and self.FRS <= self.medium[i]:
                    a = self.medium[i-1]
                    b = self.medium[i]
                    self.lower_edge_FRS_value = (self.FRS - a) / (b - a)
                    if self.lower_edge_FRS_value != 0:
                        break

        if self.lower_edge_FRS_value == 0:
            for i in range(1, len(self.far)):  
                if self.FRS >= self.far[i-1] and self.FRS <= self.far[i]:
                    a = self.far[i-1]
                    b = self.far[i]
                    self.lower_edge_FRS_value = (self.FRS - a) / (b - a)
                    if self.lower_edge_FRS_value != 0:
                        break

    # For the Front Left Sensor
    def upper_edge_FLS(self):
        for i in range(1, len(self.near)):  
            if self.FLS >= self.near[i-1] and self.FLS <= self.near[i]:
                if self.FLS == self.near[i]:
                    self.upper_edge_FLS_value = 1
                else:
                    a = self.near[i-1]
                    c = self.near[i]
                    self.upper_edge_FLS_value = (c - self.FLS) / (c - a)
                self.BnearFLS = True

        for i in range(1, len(self.medium)):  
            if self.FLS >= self.medium[i-1] and self.FLS <= self.medium[i]:
                if self.FLS == self.medium[i]:
                    self.upper_edge_FLS_value = 1
                else:
                    a = self.medium[i-1]
                    c = self.medium[i]
                    self.upper_edge_FLS_value = (c - self.FLS) / (c - a)
                self.BmediumFLS = True
                self.BnearFLS = False  

        for i in range(1, len(self.far)):  
            if self.FLS >= self.far[i-1] and self.FLS <= self.far[i]:
                if self.FLS == self.far[i]:
                    self.upper_edge_FLS_value = 1
                else:
                    a = self.far[i-1]
                    c = self.far[i]
                    self.upper_edge_FLS_value = (c - self.FLS) / (c - a)
                self.BfarFLS = True
                self.BmediumFLS = False

    def lower_edge_FLS(self):
        for i in range(1, len(self.near)):  
            if self.FLS >= self.near[i-1] and self.FLS <= self.near[i]:
                a = self.near[i-1]
                b = self.near[i]
                self.lower_edge_FLS_value = (self.FLS - a) / (b - a)
                if self.lower_edge_FLS_value != 0:
                    break

        if self.lower_edge_FLS_value == 0:
            for i in range(1, len(self.medium)):  
                if self.FLS >= self.medium[i-1] and self.FLS <= self.medium[i]:
                    a = self.medium[i-1]
                    b = self.medium[i]
                    self.lower_edge_FLS_value = (self.FLS - a) / (b - a)
                    if self.lower_edge_FLS_value != 0:
                        break

        if self.lower_edge_FLS_value == 0:
            for i in range(1, len(self.far)):  
                if self.FLS >= self.far[i-1] and self.FLS <= self.far[i]:
                    a = self.far[i-1]
                    b = self.far[i]
                    self.lower_edge_FLS_value = (self.FLS - a) / (b - a)
                    if self.lower_edge_FLS_value != 0:
                        break
    
    # For the front sensor
    def upper_edge_F(self):
        for i in range(1, len(self.near)):  
            if self.F >= self.nearF[i-1] and self.F <= self.nearF[i]:
                if self.F == self.nearF[i]:
                    self.upper_edge_F_value = 1
                else:
                    a = self.nearF[i-1]
                    c = self.nearF[i]
                    self.upper_edge_F_value = (c - self.F) / (c - a)
                self.BnearF = True

        for i in range(1, len(self.mediumF)):  
            if self.F >= self.mediumF[i-1] and self.F <= self.mediumF[i]:
                if self.F == self.mediumF[i]:
                    self.upper_edge_F_value = 1
                else:
                    a = self.mediumF[i-1]
                    c = self.mediumF[i]
                    self.upper_edge_F_value = (c - self.F) / (c - a)
                self.BmediumF = True
                self.BnearF = False

        for i in range(1, len(self.far)):  
            if self.F >= self.farF[i-1] and self.F <= self.farF[i]:
                if self.F == self.farF[i]:
                    self.upper_edge_F_value = 1
                else:
                    a = self.farF[i-1]
                    c = self.farF[i]
                    self.upper_edge_F_value = (c - self.F) / (c - a)
                self.BfarF = True
                self.BmediumF = False

    def lower_edge_F(self):
        for i in range(1, len(self.near)):  
            if self.F >= self.nearF[i-1] and self.F <= self.nearF[i]:
                a = self.nearF[i-1]
                b = self.nearF[i]
                self.lower_edge_F_value = (self.F - a) / (b - a)
                if self.lower_edge_F_value != 0:
                    break

        if self.lower_edge_F_value == 0:
            for i in range(1, len(self.mediumF)):  
                if self.F >= self.mediumF[i-1] and self.F <= self.mediumF[i]:
                    a = self.mediumF[i-1]
                    b = self.mediumF[i]
                    self.lower_edge_F_value = (self.F - a) / (b - a)
                    if self.lower_edge_F_value != 0:
                        break

        if self.lower_edge_F_value == 0:
            for i in range(1, len(self.far)):  
                if self.F >= self.farF[i-1] and self.F <= self.farF[i]:
                    a = self.farF[i-1]
                    b = self.farF[i]
                    self.lower_edge_F_value = (self.F - a) / (b - a)
                    if self.lower_edge_F_value != 0:
                        break
    

    #For the rules I find the min of the values and append it to the rules according to the speed and direction related
                        
    def calculate_firing_strength(self):
        rules = []

        # Applying the rules based on the Excel file
        if self.BnearFRS and self.BnearF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BnearFRS and self.BnearF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BnearFRS and self.BnearF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BnearFRS and self.BmediumF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BnearFRS and self.BmediumF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BnearFRS and self.BmediumF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BnearFRS and self.BfarF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BnearFRS and self.BfarF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BnearFRS and self.BfarF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BmediumFRS and self.BnearF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BnearF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BnearF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BmediumFRS and self.BmediumF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BmediumF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BmediumF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BmediumFRS and self.BfarF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BfarF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BmediumFRS and self.BfarF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "right"))
        if self.BfarFRS and self.BnearF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BnearF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BnearF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BmediumF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BmediumF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BmediumF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BfarF and self.BnearFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BfarF and self.BmediumFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "left"))
        if self.BfarFRS and self.BfarF and self.BfarFLS:
            rules.append((min(self.upper_edge_FRS_value, self.upper_edge_F_value, self.upper_edge_FLS_value), "low", "straight"))

        print(rules)
        return rules

    # To get the centroid according to the values respected

    def centroid(self, values):
        centroid = (min(values) + max(values)) / len(values)  # Weighted avereged formula.
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
        self.direction_output = (direction_numerator / denominator) if denominator != 0 else 0 # direction
        
        print(f"Defuzzified Speed Output: {self.speed_output}")
        print(f"Defuzzified Direction Output: {self.direction_output}")
      
    # A function to call all the functions

    def run(self):
        print("run")
        self.upper_edge_FRS()
        self.lower_edge_FRS()
        self.upper_edge_FLS()
        self.lower_edge_FLS()
        self.upper_edge_F()
        self.lower_edge_F()
    
        # Firing strengths based on rules
        rules = self.calculate_firing_strength()
        
        # Defuzzifying the output                        
        self.defuzzify(rules)



# All below was for trying my code without implementing the class to the turtlebot

# # # List and variables 
# near = [0.0, 0.25, 0.6]
# medium = [0.25, 0.6, 0.7]
# far = [0.6, 0.7, 1.0]

# nearF = [0.0, 0.25, 0.75]
# mediumF = [0.25, 0.75, 0.85]
# farF = [0.75, 0.85, 1.0]

# low = [0.01, 0.05, 0.1]
# med = [0.1, 0.15, 0.2]
# high = [0.2, 0.25, 0.3]
# left = [-0.3, -0.2, -0.1]
# straight = [-0.1, 0.0, 0.1]
# right = [0.1, 0.2, 0.3]



# # # Variables for the rules 
# BnearFRS = False
# BmediumFRS = False
# BfarFRS = False
# BnearFLS = False
# BmediumFLS = False
# BfarFLS = False
# BnearF = False
# BmediumF = False
# BfarF = False


# FRS = 0.3
# FLS = 0.5
# F = 0.4

# corre = FuzzyAvoidFront(FRS = FRS, FLS = FLS, F = F, near=near, medium=medium, far=far, nearF=nearF, mediumF=mediumF, farF=farF, low=low, med=med, high=high, left=left, straight=straight, right=right, BnearFRS=BnearFRS, BmediumFRS=BmediumFRS, BfarFRS=BfarFRS, BnearFLS=BnearFLS, BmediumFLS=BmediumFLS, BfarFLS=BfarFLS, BnearF=BnearF, BmediumF=BmediumF, BfarF=BfarF)
# corre.run()


