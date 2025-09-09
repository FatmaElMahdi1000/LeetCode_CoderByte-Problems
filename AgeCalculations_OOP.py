current_year = 2025
class age:
    #current_year = 2025
    def __init__(self, name, country, birth_year):
        self.birth_year = birth_year
        self.name = name
        self.country = country 
        
    def age_calculation(self):
        print(f"{self.name} from {self.country} will turn {current_year - self.birth_year} TODAY!")

calculation = age("Mike", "Poland", 1996)
calculation.age_calculation()

#print(calculation.current_year) #Accessing the class attribute









