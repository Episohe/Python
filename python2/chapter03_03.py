# Chapter03_03
# Special Method ( = Magic Method)
# python 핵심 -> 시퀀스(sequence), 반복(iterator), 함수(function), 클래스(class)

# class 안에서 정의할 수 있는 특별한(built in) 메소드

# 객체 -> python Data 추상화
# 모든 객체 -> id, type -> value
from math import sqrt

# 일반적 Tuple
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

len1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(len1)

from collections import namedtuple

# namedTuple 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3[0])
print(pt3.x)
print(pt4)

len2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y ** 2))
print(len2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # default = False (중복값 및 예약어)

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point1(**temp_dict)  # Tuple -> * / dictionary -> **

print(p1)
print(p2)
print(p3)

# rename 테스트
print(p4)  # Point(x=10, y=20, _2=30, _3=40)
print(p5)

# 사용(인덱스 & key 둘다 가능)
print(p1[0] + p2[1])
print(p1.x + p2.y)

# Unpacking
x, y = p2
print(x, y)

# namedtuple Method
temp = [52, 38]

# List -> namedTuple
p4 = Point1._make(temp)
print(p4)

# _field : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict   원래 Dictionary -> 정렬x
print(p1._asdict())
print(p4._asdict())

# 실습
# 반 20명, 4개의 반(A,B,C,D)

Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print(numbers)
print(ranks)

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

print(len(students))
print(students)

# 추천
student2 = [Classes(rank, number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                        for n in range(1, 21)]]

print(len(students))
print(students)
