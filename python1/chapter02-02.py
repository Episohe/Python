# Chapter02-2
# 파이썬 변수
# 1. 변수 할당 설명
# 2. Object identity
# 3. 변수 네이밍 규칙
# 4. 예약어


# 1. 변수 할당 설명
# 다양한 변수 선언법
# 기본 선언
n = 700

# 출력
# print(n)
# print(type(n))

# 동시 선언
x = y = z = 700
# print(x, y, z)

# 재선언 (마지막 값으로 재할당함)
var = 75
var = "Change Value"

# print(var)
# print(type(var))

# Object Refernces를 보면 아래 단계로 실핻된다.
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# . 콘솔 출력

# 예1)
print(300)
print(type(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))

m = n

# m -> 777 <- n

print(m, n)
print(type(m), type(n))

m = 400

print(m, n)
print(type(m), type(n))

# id(identity)확인 : 객채의 고유 값

m = 800
n = 655

print(id(m))
print(id(n))
print(id(m) == id(n))

m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))

# 다양한 변수 선언(네이밍 규칙)
# Camel Case : numberOfCollegeGraduates -> Method
# Pascal Case : NumberOfCollegeGraduates -> Class
# Snake Case : number_of_college_graduates

# 허용하는 변수 선언 법
age = 1
Age = 1
aGe = 1
AGE = 1
a_g_e = 1
_age = 1
age_ = 2
_AGE = 1

# 예약어
"""
python reserved words

False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal yield
break	for	not	
class	from	or	
continue	global	pass	
"""
# python reserved words
