from math import pi

class Circle:
    def __init__(self, r: int):
        self.radius = r
        self.diameter = 2 * r
        self.area = pi * (r)**2


circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)