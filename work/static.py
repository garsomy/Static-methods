def my_decorator(func):

    def wrapper():
        print('before decorator')
        func()
        print('after decorator')
    return wrapper

@my_decorator
def hello():
    print('Hello')

hello()