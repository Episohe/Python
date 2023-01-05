# 내장 함수
# 자주 사용하는 함수 위주의 실습
# 사용하다보면 자연스럽게 숙당 -> 외우려고 하지 말것

# 절대값
# abs

print(abs(-3))  # >>> 3

# all : iterable 요소 검사(참.거짓)
print(all([1, 2, '']))  # >>> False

# any : 하나라도 True이면 True 반환
print(any([1, 2, 0]))  # >>> True

# chr : 아스키 -> 문자
print(chr(67))  # >>> C
# ord : 문자 -> 아스키
print(ord('C'))  # >>> 67

# enumerate : 인덱스 + Iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']):
    print(i, name)

    # >>> 0 abc
    # >>> 1 bcd
    # >>> 2 efg


# filter : 반복 가능한 객체 요소를 지정한 함수 조건에 맞는 값 추출
def conv_pos(x):
    return abs(x) > 2


print(list(filter(conv_pos, [-1, -3, 2, 0, 5])))  # >>> [-3, 5]

# 람다식으로 변환
print(list(filter(lambda x: abs(x) > 2, [-1, -3, 2, 0, 5])))  # >>> [-3, 5]

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))  # >>> 3185338024304

# len : 요소의 길이를 반환
str_len = len('abcdefg')
print(str_len)  # >>> 7

# min, max : 최대값, 최소값
print(max([1, 2, 3]))  # >>> 3
print(max('python study'))  # >>> y

print(min([1, 2, 3]))  # >>> 1
print(min('python study'))  # 공백이 가장 작기 때문에 빈값이 출력
print(min('pythonstudy'))  # >>> d


# map : 반복 가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x):
    return abs(x)


print(list(map(conv_abs, [1, -3, 2, 0, -5])))  # >>> [1, 3, 2, 0, 5]
print(list(map(lambda x: abs(x), [1, -3, 2, 0, -5])))  # >>> [1, 3, 2, 0, 5]

# pow : 제곱값 반환
print(pow(2, 10))  # >>> 1024

# range 반복 가능한 객체(Iterable) 반환
print(range(1, 10, 2))  # >>> range(1, 10, 2)
print(list(range(1, 10, 2)))  # >>> [1, 3, 5, 7, 9]
print(list(range(0, -15, -1)))  # >>>  [0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]

# round : 반올림

# 소수점 두번째 자리까지 반올림
result = round(6.5781, 2)
print(result)  # >>> 6.58

result = round(5.6)
print(result)  # >>> 6

# sorted : 반복 가능한 객체(Iterable)정렬 후 반환
a = sorted([6, 7, 3, 1, 8])
print(a)  # >>> [1, 3, 6, 7, 8]

b = sorted(['p', 'y', 't', 'h', 'o', 'n'])
print(b)  # >>> ['h', 'n', 'o', 'p', 't', 'y']

# sum : 반복 가능한 객체의 합 반환
c = sum([6, 7, 8, 9, 10])
print(c)  # >>> 40
d = sum(range(1, 101))
print(d)  # >>> 5050

# type : 자료형 확인
print(type(3))  # >>> <class 'int'>
print(type(list(range(1, 10))))  # >>> <class 'list'>

# zip : 반복 가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))  # >>> [(10, 40), (20, 50), (30, 60)]

# 짝이 없는 것은 반환 하지 않는다.
print(list(zip([10, 20, 30], [40, 50])))  # >>> [(10, 40), (20, 50)]

print(type(list(zip([10, 20, 30], [40, 50]))[0]))  # >>> <class 'tuple'>
