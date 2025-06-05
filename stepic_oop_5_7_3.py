from functools import total_ordering

@total_ordering
class RomanNumeral:
    def __init__(self, number:str):
        self.number = number
    def __str__(self):
        return f'{self.number}'

    def __int__(self):
        all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        dec = 0
        rom = self.number
        for i, r in all_roman:
            while rom.startswith(r):
                dec += i
                rom = rom[len(r):]
        return dec

    def to_roman(self, number: int) -> str:
        all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
                     (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
                     (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = ""
        for value, numeral in all_roman:
            while number >= value:
                result += numeral
                number -= value
        return result

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__int__() == other.__int__()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.__int__() < other.__int__()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.to_roman(self.__int__() + other.__int__()))
        return  NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.to_roman(self.__int__() - other.__int__()))
