class DevelopmentTeam():
    def __init__(self):
        self.junior = []
        self.senior = []

    def add_junior(self, *args):
        self.junior.extend([(elem,'junior') for elem in args])

    def add_senior(self, *args):
        self.senior.extend([(elem,'senior') for elem in args])


    def __iter__(self):
        return (elem for elem in self.junior + self.senior)




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