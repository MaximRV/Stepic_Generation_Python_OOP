class Scales:
    def __init__(self):
        self.right_side = 0
        self.left_side = 0
    def add_right(self, m: int = 0):
        self.right_side += m
    def add_left(self, m: int = 0):
        self.left_side += m
    def get_result(self):
        if self.right_side == self.left_side:
            return  "Весы в равновесии"
        elif  self.right_side > self.left_side:
            return "Правая чаша тяжелее"
        elif self.right_side < self.left_side:
            return "Левая чаша тяжелее"



scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())