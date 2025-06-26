class AttrsIterator:
    def __init__(self, obj):
        self.obj_attr = list(obj.__dict__.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.obj_attr):
            result = self.obj_attr[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration



test_number = 1
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)
