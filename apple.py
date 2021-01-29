
import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print("created")

    def area(self):
        return self.radius*self.radius*math.pi

roundedShape = Circle(10)
print(roundedShape.area())
print(math.pi)
