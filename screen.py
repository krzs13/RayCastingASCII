from player import Player


class Screen:
    def __init__(self):
        self.width = 100
        self.height = 25
        self.clean_screen = []
        self.screen = []
        self.maker(self.clean_screen)
        self.maker(self.screen)

    def maker(self, base):
        for y in range(self.height):
            base.append([])
            if y <= 12:
                for x in range(self.width):
                    base[y].append(' ')
            elif 13 <= y < 17:
                for x in range(self.width):
                    base[y].append('.')
            elif 17 <= y < 21:
                for x in range(self.width):
                    base[y].append(':')
            else:
                for x in range(self.width):
                    base[y].append(';')


    def cleaner(self):
        for y in range(self.height):
            for x in range(self.width):
                self.screen[y][x] = self.clean_screen[y][x]

    def printer(self):
        buffer = ''
        for y in range(self.height):
            buffer += ''.join(self.screen[y])
            if y > self.height - 1:
                buffer += '\n'
        print(buffer)