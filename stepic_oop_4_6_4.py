class Color:
    def __init__(self, code):
        self.hexcode = code

    @property
    def hexcode(self):
        return self.color

    @hexcode.setter
    def hexcode(self, code):
        self.color = code
        self.r = int(self.color[0:2], 16)
        self.g = int(self.color[2:4], 16)
        self.b = int(self.color[4:], 16)

hexcodes = ['FC5A5E', '13AABE', '851149', 'AAAAAA', 'FFFFFF', 'B6A1D8', 'ABCDEF', 'FEDCBA', '123456', '999999']
count = 1
for hc in hexcodes:
    color = Color(hc)
    print(f'Цвет № {count}')
    print(color.hexcode)
    print(color.r, color.g, color.b, sep='\n')
    print()
    count += 1