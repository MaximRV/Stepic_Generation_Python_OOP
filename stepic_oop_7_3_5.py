
class SuperInt(int):
    def repeat(self,n:int=2):
        return SuperInt(str(self) + str(abs(self)) *(n - 1))

    def to_bin(self):
        if self >=0:
            return bin(self)[2:]
        return str(self)[0]  + bin(self)[3:]

    def next(self):
        return SuperInt(self + 1)

    def prev(self):
        return SuperInt(self - 1)

    def __iter__(self):
        return (SuperInt(i) for i in str(abs(self)))

        







test_number = 13
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)


