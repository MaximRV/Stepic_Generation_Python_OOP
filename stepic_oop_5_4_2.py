
class Money:
    def __init__(self, amount):
        self.amount = amount
    def __str__(self):
        return f'{self.amount} руб.'
    def __pos__(self):
        return Money(abs(self.amount))
    def __neg__(self):
        return Money(-abs(self.amount))




test_number = 5
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print()

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)