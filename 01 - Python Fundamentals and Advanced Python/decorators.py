def my_decorator(func):

    def wrapped():
        print("wrapped func executed")
        func()
        print("func executed")

    return wrapped

@my_decorator
def hello_world():
    print("hello world")

hello_world()
