class Robot:
    def __init__(self, x, y):
        self.x = self.coordinate(x)
        self.y = self.coordinate(y)
        self.coord_list = [(self.x, self.y)]

    def coordinate(self, coord):
        if coord < 0 or coord > 100:
            raise ValueError('Ошибка. Координаты должы быть от 0 до 100')
        return coord

    def move(self, moves):
        for r_move in moves:
            if r_move == 'N':
                if self.y < 100:
                    self.y += 1
            elif r_move == 'S':
                if self.y > 0:
                    self.y -= 1
            elif r_move == 'E':
                if self.x < 100:
                    self.x += 1
            elif r_move == 'W':
                if self.x > 0:
                    self.x -= 1
                    self.coord_list.append((self.x, self.y))
            else:
                print('Ошибка в движении')

        return self.get_pos()

    def get_pos(self):
        return [(self.x, self.y)]

    def path(self):
        return self.coord_list







robot = Robot(8, 86)
print(robot.path())

robot.move('N')
robot.move('E')
robot.move('N')
robot.move('E')
print(robot.get_pos())

robot.move('NE')
robot.move('SW')
robot.move('WS')
robot.move('E')
robot.move('EE')
robot.move('NNEWNS')
print(robot.get_pos())

print(robot.path())
