# set 집합
# 특징 : 순서 x, 중복 x 수정 O, 삭제 O

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'que'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
print('e : ', type(e), e)
print('f : ', type(f), f)

# 튜플 변환(set -> tuple)
t = tuple(b)
print('t : ', type(t), t)
print('t : ', t[0])
print('t : ', t[1:3])

# 리스트 변환 (set -> list)
l = list(c)
l2 = list(e)

print('l : ', l)
print('l2 : ', l2)

# 길이
print(len(a))
print(len(b))
print(len(c))
print(len(d))

# 집합 차료형 활용
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([1, 3, 4, 6, 8, 10])

# 교집합
print('>>> 교집합')
print('s1 & s2 : ', s1 & s2)
print('s1 & s2 : ', s1.intersection(s2))

# 합집합
print('s1 | s2 : ', s1 | s2)
print('s1 | s2 : ', s1.union(s2))

# 차집합
print('s1 - s2 : ', s1 - s2)
print('s1 - s2 : ', s1.difference(s2))

# 중복 원소 확인
# false =>  교집합이 있음
print('>>> 교집합 확인')
print('s1 & s2 : ', s1.isdisjoint(s2))

# 부분 집합 확인
print('subset : ', s1.issubset(s2))
print('superset : ', s1.issuperset(s2))

# 추가 & 제거
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 : ', s1)

s1.remove(2)
print('s1 : ', s1)

# 없는 원소를 remocve 지울 때 key Error!
# s1.remove(7)

s1.discard(3)
print('>>> discard')
print('s1 : ', s1)

# 없는 원소를 지울 때 에러를 발생시키지 않는다!
s1.discard(7)

# 전부 삭제
s1.clear()
print('s1 : ', s1)
