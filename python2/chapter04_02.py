# Chapter 04-02
# 시퀀스형
# 컨테이너 (container : 서로 다른 자료형[list, tuple, collections.deque)
# Flat : 한개의 자료형[str, bytes, bytearray, array-array, memoryView]
# 가변 : list, bytearray, array-array, memoryView, deque
# 불변 : tuple, str, bytes
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

print(divmod(100, 9))  # (11, 1)
print(divmod(*(100, 9)))  # (11, 1)
print(*(divmod(100, 9)))  # 11 1

print('------------------------------------')

x, y, *rest = range(10)
print(x, y, rest)  # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
x, y, *rest = range(2)
print(x, y, rest)
x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print('------------------------------------')

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))
print('------------------------------------')

l = l * 2
m = m * 2
print(l, id(l))  # (15, 20, 25, 15, 20, 25) 1267865429824
print(m, id(m))  # [15, 20, 25, 15, 20, 25] 1267861583936

l *= 2
m *= 2
print(l, id(l))  # (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 1267862094176
print(m, id(m))  # [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 1267861583936
print('------------------------------------')

# sort vs sorted
# reverse, key=Len, key=str.Lower, key=func...

# sorted : 정렬 후 객체 직접 반환
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print(f_list)
print('sorted -', sorted(f_list))
print('sorted -', sorted(f_list, reverse=True))  # 알파벳 역순
print('sorted -', sorted(f_list, key=len))  # 길이 순
print('sorted -', sorted(f_list, key=lambda x: x[-1]))  # 끝의 글자 기준 알파벳 순서
print('sorted -', sorted(f_list, key=lambda x: x[-1], reverse=True))  # 끝의 글자 기준 알파벳 역순
print('------------------------------------')

# sort : 정렬 후 객체 직접 변경

# 반환 값 확인(None)
print('sort -', f_list.sort(), f_list)
print('sort -', f_list.sort(reverse=True), f_list)
print('sort -', f_list.sort(key=len), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1]), f_list)
print('sort -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
print(f_list)  # 원본이 수정 됌

# List vs Array 적합한 사용법 설명
# List: 융통성, 다양한 자료형, 범용적 사용
# Array: 숫자 기반(리스트와 거의 호한 가능)
