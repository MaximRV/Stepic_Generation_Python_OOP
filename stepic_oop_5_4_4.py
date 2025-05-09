

class ColoredPoint:
    def __init__(self, x:str, y:str, color:tuple=(0, 0, 0)):
        self.x = x
        self.y = y
        self.color = color
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x}, {self.y}, {self.color})'

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __pos__(self):
        return ColoredPoint(self.x, self.y, self.color)

    def __neg__(self):
        return ColoredPoint(-self.x, -self.y, self.color)

    def __invert__(self):
        return ColoredPoint(self.y,self.x,(255-self.color[0],255-self.color[1],255-self.color[2]))

