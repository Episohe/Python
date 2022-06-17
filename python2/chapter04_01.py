# Chapter 04-01
# 시퀀스형
# 컨테이너 (container : 서로 다른 자료형[list, tuple, collections.deque)
# Flat : 한개의 자료형[str, bytes, bytearray, array-array, memoryView]
# 가변 : list, bytearray, array-array, memoryView, deque
# 불변 : tuple, str, bytes

# 리스트 및 튜플 고급
# 지능형 리스트(Comprehending Lists)
chars = '+_)(*&(#&*#)'
code_list1 = []

for s in chars:
    # 유니 코드 리스트
    code_list1.append(ord(s))
print(code_list1)  # [43, 95, 41, 40, 42, 38, 40, 35, 38, 42, 35, 41]

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)  # [43, 95, 41, 40, 42, 38, 40, 35, 38, 42, 35, 41]

# Comprehending List + Map, filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

print(code_list3)  # [43, 95, 41, 42, 42, 41]
print(code_list4)  # [43, 95, 41, 42, 42, 41]

# 문자열 출력
print([chr(s) for s in code_list1])
print('---------------------------------------------------------------------')

# Generator 생성
import array

# Generator: 한 번에 한 개의 항목을 생성(메모리 유지X)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))

print(tuple_g)  # <generator object <genexpr> at 0x000001FFFDCC9A10>
print(type(tuple_g))  # <class 'generator'>
print(next(tuple_g))  # 43
print(array_g)  # array('I', [43, 95, 41, 40, 42, 38, 40, 35, 38, 42, 35, 41])
print(type(array_g))  # <class 'array.array'>
print(array_g.tolist())  # [43, 95, 41, 40, 42, 38, 40, 35, 38, 42, 35, 41]

# 제네레이터 생성 예제
print(('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 21)):
    print(s)

# List 주의
marks1 = [['~'] * 3 for _ in range(4)]  # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2 = [['~'] * 3] * 4  # [['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]

# 수정
marks1[0][1] = 'x'  # [['~', 'x', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']]
marks2[0][1] = 'x'  # [['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~'], ['~', 'x', '~']]

# 증명
print([id(i) for i in marks1])  # [1484488919424, 1484488919360, 1484488919232, 1484488919168]
print([id(i) for i in marks2])  # [1484488919040, 1484488919040, 1484488919040, 1484488919040]
