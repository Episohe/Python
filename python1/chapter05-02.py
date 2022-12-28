# Chapter 05-02
# 파이썬 사용자 입력
# Input 사용법
# 기본 타입(Str)

# 예제 1
name = input('Enter your name')
grade = input('Enter your grade')
company = input('Enter your company')

print(name, grade, company)

# >>> sunny 10 kakao

# 예제 2
number = input("Enter number : ", )
name = input("Enter name : ", )

print("type of number", type(number))
print("type of name", type(name))

# type of number <class 'str'>
# type of name <class 'str'>

# 예제 3 (계산)
first_num = int(input("Enter first number : "))
second_num = int(input("Enter second number : "))

total = first_num + second_num
print("first_number + second_number : ", total)

# 예제 4
float_num = float(input("Enter a float number : "))

print("input float : ", float_num)
print("input type : ", type(float_num))

# 예제 5
print("FirstName - {0}, LastName - {1}".format(input("Enter first name : "), input("Enter last name : ")))
