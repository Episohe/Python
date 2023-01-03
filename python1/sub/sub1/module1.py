import inspect


# from ..sub2 import module2

# module2.py
def mod1_test1():
    print("Module -> Test1")
    print("Path :", inspect.getfile(inspect.currentframe()))


def mod1_test2():
    print("Module -> Test2")
    print("Path : ", inspect.getfile(inspect.currentframe()))
