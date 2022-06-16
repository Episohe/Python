# Chapter03_02
# Special Method ( = Magic Method)
# python 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# class 안에서 정의할 수 있는 특별한(built in) 메소드

# class 예제2
# 벡터(x,y) (5,2)
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50, 15)
# Max((5,10)) = 10


class Vector(object):
    def __init__(self, *args):
        """
        Create a Vector, example : v = Vector(5, 10)
        :param arg:
        :return:
        """
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        :return: vector information.
        """
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        """
        :param other:
        :return: vector addition of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        """
        :param y:
        :return: vector multi
        """
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        """
        configure (0, 0)
        :return:
        """
        print('Warning!!!')
        return bool(max(self._x, self._y))


print(Vector.__init__.__doc__)

# Vector instance 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1 * 3)
print(v2 * 10)
print(bool(v1), bool(v2))
print(bool(v3))
