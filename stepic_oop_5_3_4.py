from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        if len(version.split('.')) == 1:
            self.version = version + '.0.0'
        elif len(version.split('.')) == 2:
            self.version = version + '.0'
        else:
            self.version = version

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.version}')"

    def __str__(self):
        return self.version

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.version.split('.') == other.version.split('.')
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return tuple(int(i) for i in self.version.split('.')) > tuple(int(i) for i in other.version.split('.'))
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
