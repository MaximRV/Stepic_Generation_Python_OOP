class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def fullname(self):
        return f"{self.name} {self.surname}"

    @fullname.setter
    def fullname(self, fullname: str):
        self.name, self.surname = fullname.split()

person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)