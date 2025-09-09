class Robot:
    """Robot class: it helps creating and destructing Robots!"""
    population = 0 #class variable
    def __init__(self, name):
        self.name = name
        
    def Robot_Creation(self):
        """This Method: helps creating Robots!"""
        Robot.population += 1  #access the class variable here by mentioning the class name: Robot.population
        return f"we've a new Robot, named: {self.name}"
        
    def Robot_elimination(self):
        Robot.population -= 1
        return f"Robot: {self.name} died!"

    @classmethod  #to know the ultimate result of our population, and since it's a class variable we need to use a class method,clsass variables cannot accessed by the objects
    def number_of_Robots(cls):
        return f"the Robot Population is: {cls.population}!"

Robot1 = Robot("James")
print(Robot1.Robot_Creation())
print(Robot.number_of_Robots()) #this method has been accessed by the class :) , Class method
Robot2 = Robot("Fatma!")
print(Robot2.Robot_Creation())
print(Robot.number_of_Robots())
print(Robot1.Robot_elimination())
print(Robot.number_of_Robots())
print(Robot.__doc__) #printing class docstring
print(Robot.Robot_Creation.__doc__) #printing Method doc string 
