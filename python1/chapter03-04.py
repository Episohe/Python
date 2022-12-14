# 튜플
# 리스트와 비교
# 튜플 자료형(순서, 중복 o / 수정, 삭제 x)

# 선언
a = ()
b = (1,)  # 원소가 하나일 경우 뒤에 , 를 붙여줘야 튜플로 인식함.
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

print('>>> 튜플 인덱싱')
print('d : ', d[1])
print('d : ', d[0] + d[1] + d[1])
print('d : ', d[-1])

# 수정 불가
# d[0] = 1500  Tuples don't support item assignment

print('>>>> 슬라이싱')
print('d : ', d[0:3])
print('d : ', d[2:])
print('e : ', e[2][1:3])

print('>>> 튜플 연산')
print('c +d :', c + d)
print('c * 3', c * 3)

numbers = (5, 2, 3, 1, 4)
print('a :', )

# packing unpacking
# packing
tuple1 = ('foo', 'bar', 'buz', 'far')

print(">>>> packing")
print(tuple1)
print(tuple1[0])
print(tuple1[-1])

# 언패킹
(x1, x2, x3, x4) = tuple1

print(">>> unpacking")
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

tuple2 = (1, 2, 3)
tuple3 = 4,
x1, x2, x3 = tuple2
x4, x5, x6 = 4, 5, 6

print(tuple2)
print(tuple3)
print(x1, x2, x3)
print(x4, x5, x6)
