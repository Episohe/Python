# Chapter 04-02
# For문
# 반복문 중요성
# 기본 For사용
# For문 패턴 실슬
# For-Else 구문


# 코딩의 핵심
# for in <collection>
# < Loop Body>

for v1 in range(10):  # 0~9
    print('V1 is : ', v1)

for v2 in range(1, 11):  # 1~10
    print('V2 is : ', v2)

for v3 in range(1, 11, 2):  # 1~10 중 두개씩 건너뜀
    print('V3 is : ', v3)

# 1~1000까지의 합을 구하기
sum1 = 0
for v in range(1, 1001):
    sum1 += v
print('1 ~ 1000 Sum : ', sum1)

print('1 ~ 1000 Sum :', sum(range(1, 1001)))

print('1~ 1000 4의 배수의 합 : ', sum(range(4, 1001, 4)))

# Iterables 자료형 반복
# 문자열
# 리스트
# 튜플
# 집합
# 딕셔너리

# iterable 함수 : range , reversed, enumerate, filter, map, zip

# 예제 1
names = ['Kim', 'Park', 'Cho', 'Yoo']

for i in names:
    print('you are : ', i)

# 예제 2
lotto_numbers = [11, 14, 34, 1, 31, 20]

for n in lotto_numbers:
    print('Current number : ', n)

# 예제 3 (문자열도 가능)
word = 'Beautiful'
for s in word:
    print('word : ', s)

# 예제 4
my_info = {
    'name': 'Lee',
    'Age': 33,
    'City': 'Seoul'
}

# key 값만 가져옴
for key in my_info:
    print('Key :', my_info[key])

# value 반환
for v in my_info.values():
    print('value : ', v)

# 예제 5
name = 'FineAppLE'

# 대문자로 출력 ( 소문자는 islower)
for n in name:
    if n.isupper():
        print(n)
    print(n.upper())

# break (즉시 멈춤)
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:
        print("Found : 34!")
        break
    else:
        print("Not found : ", num)

# continue (즉시 스킵)
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue

    print("current type : ", type(v))
    print("multiply by 2:", v * 3)

# else 구문
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 34:  # 45
        print("Found : 34!")
        break
else:
    print("Not Found 45...")

# 구구단 출력

for i in range(2, 10):
    for j in range(2, 10):
        print('{:4d}'.format(i * j), end='')
    print()

# 변환 예제
name = 'Aceman'
print('Reversed : ', reversed(name))
print('List : ', list(reversed(name)))
print('Tuple : ', tuple(reversed(name)))
print('Set : ', set(reversed(name)))  # 순서X
