class MyClass:
    TOTAL_COUNTS = 0

    def __init__(self):
        MyClass.TOTAL_COUNTS = MyClass.TOTAL_COUNTS + 1

    @classmethod
    def total_counts(cls):
        print('Общее число = ', cls.TOTAL_COUNTS)



class ChildClass(MyClass):
    TOTAL_COUNTS = 0

    def __init__(self):
        ChildClass.TOTAL_COUNTS += 1    



m = MyClass()
m1 = MyClass()
MyClass.total_counts()
cc = ChildClass()
cc.total_counts()