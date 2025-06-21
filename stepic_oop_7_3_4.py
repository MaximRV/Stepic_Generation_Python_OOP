class TitledText(str):
    def __new__(cls, text, title):
        instance = super().__new__(cls, text)
        instance._title = title
        return instance

    def __init__(self, text, title):
        self._title = title

    def title(self):
        return self._title






test_number = 1
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result / Stepic Result')
    print()
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('-----------------------------------------')
    print()
    print(content_output)


