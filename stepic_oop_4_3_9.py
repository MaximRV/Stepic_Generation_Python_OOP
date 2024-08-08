class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def abs(self):
        return (self.x **2 + self.y**2 )**(1/2)

vector = Vector(3, 4)

print(vector.x, vector.y)
print(vector.abs())