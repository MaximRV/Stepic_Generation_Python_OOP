
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return f"{self.name} {self.surname}"

    def set_fullname(self, fullname: str):
        self.name, self.surname = fullname.split()


    fullname = property(get_fullname, set_fullname)


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)