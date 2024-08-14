class Knight:
    def __init__(self, horizontal=None, vertical=None, color=None):

        if horizontal in [ chr(i) for i in range(97, 105)]:
            self.horizontal = horizontal
        else:
            raise ValueError("Допустимы a-h")

        if vertical in list(range(1, 9)):
            self.vertical = vertical
        else:
            raise ValueError("Допустимы 1-8")

        if color == "black" or color == "white":
            self.color = color
        else:
            raise ValueError("Допустимые цвета Черный или Белый")

    def get_char(self):
        return "N"

    def can_move(self, x2: str, y2: int):

        difference_product = (ord(self.horizontal) - ord(x2)) * (self.vertical - y2)

        if difference_product == 2 or difference_product == -2:
            return True
        return  False

    def move_to(self, x2: str, y2: int):
        if self.can_move(x2,y2):
            self.horizontal = x2
            self.vertical = y2

    def draw_board(self):
        for i in range(8, 0, -1):
            for j in range(1, 9):
                if (self.vertical - i) * (ord(self.horizontal) - 96 - j) == 2 or (self.vertical - i) * (ord(self.horizontal) - 96 - j) == -2:
                    print("*", end="")
                elif i == self.vertical and j == ord(self.horizontal) - 96:
                    print("N", end="")
                else:
                    print(".", end="")
            print()

