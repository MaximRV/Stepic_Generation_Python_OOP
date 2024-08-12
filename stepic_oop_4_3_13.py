class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street: str, house: int, flat: int):
        my_list = (street, house, flat)
        self.delivery_data.append(my_list)

    def get_houses_for_street(self, street: str):
        li = []
        [li.append(i[1]) for i in self.delivery_data if i[0] == street and i[1] not in li]
        return li

    def get_flats_for_house(self, street: str, house: int):
        li_2 = []
        [li_2.append(i[2]) for i in self.delivery_data if i[0] == street and i[1] == house and i[2] not in li_2]
        return li_2


postman = Postman()

delivery_data = [('Тульская', 149, 35), ('Запорожская', 19, 26), ('Сосновая', 33, 17), ('Высотная', 91, 44),
                 ('Шишкина', 143, 8), ('Иванова', 60, 38), ('Веселая', 115, 19), ('Учительская', 37, 70),
                 ('М.Горького', 167, 57), ('Северная', 128, 44), ('Железнодорожная', 121, 28), ('Пригородная', 39, 2),
                 ('Одесская', 176, 34), ('Высоцкого', 100, 24), ('Цветочная', 168, 49), ('Павлова', 35, 62),
                 ('Шолохова', 177, 8), ('Баумана', 27, 96), ('Димитрова', 170, 37), ('Папанина', 85, 59),
                 ('40 лет Победы', 167, 56), ('Весенняя', 165, 63), ('Дарвина', 77, 39), ('Лунная', 200, 79),
                 ('Иванова', 104, 20), ('Комсомольская', 38, 74), ('Дарвина', 149, 44), ('Льва Толстого', 174, 85),
                 ('Победы', 64, 45), ('Новоселов', 128, 22)]

for delivery in delivery_data:
    postman.add_delivery(*delivery)

print(postman.get_houses_for_street('Дарвина'))
print(postman.get_flats_for_house('Новоселов', 128))
