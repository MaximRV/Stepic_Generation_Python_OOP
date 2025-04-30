from functools import total_ordering

@total_ordering
class Month:
    def __init__(self,year,month):
        self.year = year
        self.month = month
    def __repr__(self):
        return f'{self.__class__.__name__}({self.year}, {self.month})'

    def __str__(self):
        return f'{self.year}-{self.month}'

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.year,self.month) == (other.year, other.month)
        elif isinstance(other, tuple):
            return (self.year,self.month) == other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return (self.year, self.month) > (other.year, other.month)

        if isinstance(other, tuple):
            return (self.year, self.month) > other

        return NotImplemented

test_number = 7

with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)



