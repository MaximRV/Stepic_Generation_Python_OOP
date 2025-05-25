class RaiseTo:
    def __init__(self, degree):
        self.degree = degree
    def __call__(self, x):
        return x ** self.degree

test_number = 4
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)