class LowerString(str):
    def __new__(cls, obj=''):
        instance = super().__new__(cls, str(obj).lower())
        return instance

test_number = 1
with open(f'tests/{test_number}', 'r') as file:
    content_input = file.read()
    print(f'My Test Result')
    exec(content_input)

print('--------------------------------------------------------------------------')

with open(f'tests/{test_number}.clue', 'r') as file:
    content_output = file.read()
    print('Stepic Result')
    print(content_output)
