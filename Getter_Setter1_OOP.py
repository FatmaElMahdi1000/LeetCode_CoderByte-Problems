class Robot:
    def __init__(self, name):
        self.name = name
    def robot_name(self):
        return f"My robot name is: {self.name}"
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        return self.name

Robot1 = Robot('James')
print(Robot1.robot_name())
print(Robot1.get_name())
print(Robot1.set_name('Tony!'))