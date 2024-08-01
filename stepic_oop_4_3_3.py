class House:
    def __init__(self, color: str, rooms: int):
        self.color = color
        self.rooms = rooms

    def paint(self, new_color: str):
        self.color = new_color

    def add_rooms(self, n: int):
        self.rooms += n


house = House('white', 4)

print(house.color)
print(house.rooms)
