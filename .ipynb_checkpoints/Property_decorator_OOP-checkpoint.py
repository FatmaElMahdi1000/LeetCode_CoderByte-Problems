class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height


rectangle = Rectangle(3, 4)
print(rectangle.width)
print(rectangle.height)
print(rectangle.area) #printing using the property. (using Method as a property)