from math import pi

class Circle:
    def __init__(self, radius, diameter=None):
        self._radius = radius
        self._diameter = 2 * radius
        self._area = pi * (radius**2)

    def get_radius(self):
        return self._radius

    def get_diameter(self):
        return self._diameter

    def get_area(self):
        return self._area