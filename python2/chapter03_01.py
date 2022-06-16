# Chapter03_01
# Special Method ( = Magic Method)
# python 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# class 안에서 정의할 수 있는 특별한(built in) 메소드

# 기본형
print(int(10))
print(int)
# 10
# <class 'int'>

print(dir(int))
print(dir(float))

n = 10

print(n + 100)
print(n.__add__(100))
# print(n.__doc__)
print('--------------------------------------------')
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()


# class 예제1
class Fruit:

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    def __add__(self, x):
        print('called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('called >> __le__')
        if self._price <= x._price:
            return True
        return False

    def __ge__(self, x):
        print('called >> __ge__')
        if self._price >= x._price:
            return True
        return False


s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1 + s2)
print(s1 - s2)
print(s2 - s1)
print(s1 >= s2)
print(s1 <= s2)

