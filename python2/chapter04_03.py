# Chapter 04-03
# 시퀀스형
# 컨테이너 (container : 서로 다른 자료형[list, tuple, collections.deque)
# Flat : 한개의 자료형[str, bytes, bytearray, array-array, memoryView]
# 가변 : list, bytearray, array-array, memoryView, deque
# 불변 : tuple, str, bytes
# 해시 테이블 : key에 value를 저장하는 구조
# key 값을 해싱 함수를 통하여 해쉬 주소가 나온다. -> key에 대한 value 정보를 가져올 수 있다.

# Dict 구조
# print(__builtins__.__dict__)


# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) list(가변형) -> hash 불가

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dic1 = {}
new_dic2 = {}

# Sefdefault  사용하지 않을 경우
for k, v in source:
    if k in new_dic1:
        new_dic1[k].append(v)
    else:
        new_dic1[k] = [v]
print(new_dic1)

# Setdefault 사용 할 경우
for k, v in source:
    new_dic2.setdefault(k, []).append(v)
print(new_dic2)

# 주의
new_dic3 = {k: v for k, v in source}
print(new_dic3)
