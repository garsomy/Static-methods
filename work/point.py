class Point:
    MIN_COORD = 0
    MAX_COORD = 100
    z = 35634


    def __init__(self, x, y):
        self.__x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD < x < self.MAX_COORD:
            self.x = x
        if self.MIN_COORD < x < self.MAX_COORD:
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left

    # def __getattribute__(self, item):
    #     if item == '_Point__x':
    #         raise ValueError('Value Error')
    #     return object.__getattribute__(self, item)

    def __str__(self):
        return f'X = {self.x}, Y = {self.y}'

    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        print('getattr' + item)

    def __delattr__(self, item):
        object.__delattr__(self, item)




p = Point(1,6)
p.j = 15
Point.__setattr__(p, 'k', 5452)

print(p.__dict__)
del p.j
print(p.__dict__)