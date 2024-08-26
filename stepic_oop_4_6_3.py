class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if (self.b ** 2 - 4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** (1 / 2)) / (2 * self.a)

    @property
    def x2(self):
        if (self.b ** 2 - 4 * self.a * self.c) < 0:
            return None
        else:
            return (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** (1 / 2)) / (2 * self.a)

    @property
    def view(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}".replace('+ -', '- ')

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, info):
        self.a, self.b, self.c = info

polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (5, 3, 1)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
