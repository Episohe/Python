# Chapter 5 - 1
# 파이썬 함수의 중요성
# 파이썬 함수식 및 람다(lamda)

# 함수 정의 방법
# def function_name(parameter):
#   code

# 예제1
def first_func(w):
    print("Hello, ", w)
    # Hello, Goodboy


word = "Goodboy"

# 함수 호출
first_func(word)
print(first_func)


# 예제2
def return_function(w):
    value = "Hello, " + str(w)
    return value


x = return_function('Goodboy2')
print(x)


# Hello, Goodboy2


# 다중 반환
# 예제3
def func_mul(x1):
    y1 = x1 * 10
    y2 = x1 * 20
    y3 = x1 * 30
    return y1, y2, y2


x, y, z = func_mul(10)
print(func_mul(10))
print(type(func_mul(10)))


# 예제4 (리스트 리턴)
def func_mul3(x1):
    y1 = x1 * 10
    y2 = x1 * 20
    y3 = x1 * 30
    return [y1, y2, y2]


q = func_mul3(20)
print(type(q), q)


# <class 'list'> [200, 400, 400]


# 예제4 (딕셔너리 리턴)
def func_mul4(x1):
    y1 = x1 * 10
    y2 = x1 * 20
    y3 = x1 * 30
    return {'y1': y1, 'y2': y2, 'y3': y3}


q = func_mul4(20)
print(type(q), q)


# <class 'dict'> {'y1': 200, 'y2': 400, 'y3': 600}

# 중요
# *args, **kwargs

# *args (언팩킹)
def args_func(*args):  # 매개변수 명은 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('--------')


args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')


# **kwargs(언팩킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('Result : {}'.format(v), kwargs[v])
    print('---------')


kwargs_func(name1='Lee')
kwargs_func(name1='Lee', name2='Kim')
kwargs_func(name1='Lee', name2='Kim', name3='cho')


# 전체 혼합
def example(args_1, args2, *args, **kwargs):
    print(args_1, args2, args, kwargs)


example(10, 20, 'Lee', 'Kim', 'Park', 'Cho', age1=10, age2=20, age3=30)
print('---------')


# 중첩 함수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In Func")
    func_in_func(num + 100)


nested_func(100)


# 함수 호출 불가
# func_in_func()

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화_) -> 메모리 초기화
# 남발 시 가독성 오히려 감소

# def mul_func(a, b):
#     return a * b
#
#
# lambda a, b: a * b

# 일반 함수 -> 변수 할당
def mul_func(a, b):
    return a * b


mul_fun_var = mul_func
print(mul_fun_var(20, 50))

# 람다 함수 -> 할당
lambda_mul_func = lambda a, b: a * b
print(lambda_mul_func(50, 50))


def fun_final(a, b, func):
    print(a * b * func(100, 100))


fun_final(10, 20, lambda_mul_func)
