class SuperString:
    def __init__(self, string: str):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int | float):
            return self.__class__(self.string * other)
        return NotImplemented

    def __rmul__(self,other):
        if isinstance(other, int | float):
            return self.__mul__(other)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int | float):
            m = len(self.string) // other
            return self.__class__(self.string[:m])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int | float):
            if other >= len(self.string):
                return self.__class__("")
            elif other == 0:
                return self.__class__(self.string)

            return self.__class__(self.string[:-other])
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int | float):
            if other >= len(self.string):
                return self.__class__("")
            return self.__class__(self.string[other:])
        return NotImplemented

