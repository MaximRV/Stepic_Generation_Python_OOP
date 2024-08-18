class User:
    def __init__(self, name: str, age: int):

        if isinstance(name, str) and name.isalpha():  # проверка имени перед заменой
            self._name = name
        else:
            raise ValueError('Некорректное имя')

        if isinstance(age, int) and age in list(range(0, 111)):  # проверка возраста
            self._age = age
        else:
            raise ValueError('Некорректный возраст')

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():  # проверка имени перед заменой
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age in list(range(0, 111)):  # проверка возраста
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')


try:
    user = User('Gvido_1956', '67')
except ValueError as e:
    print(e)

