class Snow:

    def __init__(self, num):
        self.num = num

    def make_snow(self, el):
        for i in range(self.num // el):
            print('*' * el)
        print('*' * (self.num % el))

    def __add__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        res = other if isinstance(other, int) else other.num
        return Snow(self.num + res)

    def __sub__(self, other):
        if not isinstance(other, (int, Snow)):
            raise TypeError
        res = other if isinstance(other, int) else other.num
        return Snow(self.num - res)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num * other)

    def __divmod__(self, other):
        if not isinstance(other, int):
            raise TypeError
        return Snow(self.num // other)



s = Snow(10)
s1 = Snow(10)
s2 = s * 10
s2.make_snow(100)
