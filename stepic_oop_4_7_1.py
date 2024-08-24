class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diametr):
        return cls(diametr / 2)

circle = Circle(5)

print(circle.radius)