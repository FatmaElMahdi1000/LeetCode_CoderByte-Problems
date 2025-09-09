class circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    def calculations(self):
        area = self.pi * (self.radius**2)
        circumference = 2 * self.pi * self.radius
        return f"circles's Area {area} and  circumference {circumference}"

result = circle(15)
print(result.calculations())