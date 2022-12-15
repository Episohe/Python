# dictionary
# 범용적으로 가장 많이 사용하는 자료구조형
# 딕셔너리 자료형(순서x, 키 중복x, 수정 o, 삭제 o

# 선언
a = {'name': 'Kim', 'phone': '01022223333', 'birth': '870928'}
b = {0: 'Hello Python'}
c = {'arr': [1, 2, 3, 4]}
d = {
    'Name': 'Sunny',
    'City': 'Seoul',
    'Age': 33,
    'Grade': 'A',
    'Status': 'True'
}

e = dict([
    ('Name', 'Sunny'),
    ('City', 'Seoul'),
    ('Age', 33),
    ('Grade', 'A'),
    ('Status', 'True')
])

f = dict(
    Name='Sunny',
    City='Seoul',
    Age=33,
    Status=True
)

print('a : ', type(a), a)
print('b : ', type(b), b)
print('c : ', type(c), c)
print('d : ', type(d), d)
print('e : ', type(e), e)
print('f : ', type(f), f)
print('========================')
print('a의 name', a['name'])
print('a의 name', a.get('name1'))
print('b : ', b[0])
print('b : ', b.get(0))
print('f : ', f.get('City'))
print('f : ', f.get('Age'))
print('=========================')

# 중요!!!
# [''] key가 존재하지 않으면 -> 에러발생
# get('') key가 존재하지 않으면 -> None으로 처리

# 딕셔너리 추가 (key를 중복할 수 없기 때문에 같은 key가 있으면 덮어쓰고 없으면 새로 생성한다.
a['address'] = 'seoul'
print('a : ', a)
a['rank'] = [1, 2, 3]
print('a : ', a)

# 딕셔너리 길이
print('============길이')
print('e의 길이 : ', len(e))
print('c의 길이 : ', len(c))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print('a : ', a.keys())
print('b : ', b.keys())
print('c : ', c.keys())
print('d : ', d.keys())

print('a : ', list(a.keys()))
print('b : ', list(b.keys()))
print('d : ', list(d.keys()))

print(">>>>>>>values")
print('a : ', a.values())
print('b : ', b.values())
print('d : ', d.values())

print('a : ', list(a.values()))
print('b : ', list(b.values()))
print('d : ', list(d.values()))

print(">>>>>>>>>>>items")
print('a : ', a.items())
print('b : ', b.items())
print('d : ', d.items())

print('a : ', list(a.items()))
print('b : ', list(b.items()))
print('d : ', list(d.items()))

print('a의 Name', a.pop('name'))
print('a : ', a)

print('c', c.pop('arr'))
print('c : ', c)

# 무작위로 꺼낸다 ( = 딕셔너리는 순서가 없기 때문에 )
print(">>>>>popitem")
print('f : ', f.popitem())
print('f : ', f)
print('f : ', f.popitem())
print('f : ', f)

# in method 인 메서드
print('a에 birth : ', 'birth' in a)
print('d에 City : ', 'Color' in d)

# 수정 & 추가
a['test'] = 'test_dict'
print('a : ', a)

a['address'] = 'dj'
print('a : ', a)

a.update(birth='910108')
print('a : ', a)
temp = {'address': 'Busan'}

a.update(temp)
print('a : ', a)
