class Numbers:
    def __init__(self):
        self.my_list = []

    def add_number(self, n: int):
        self.my_list.append(n)

    def get_even(self):
        return [i for i in self.my_list if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.my_list if i % 2 != 0]



numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())