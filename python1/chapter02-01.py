# Chapter02-1
# 파이썬 완전 기초 과정
# print 사용법

# 기본 출력 (외국 기업 및 외국 개발자는 작은따옴표를 많이 활용한다.)
print('Python')
print("Python")
print('''Python''')
print("""Python""")

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep='|')  # >>> P|Y|T|H|O|N
print('P', 'Y', 'T', 'H', 'O', 'N', sep=' ')  # >>> P Y T H O N
print('P', 'Y', 'T', 'H', 'O', 'N', sep=',')  # >>> P,Y,T,H,O,N
print('010', '1212', '2323', sep='-')  # >>> 010-1212-2323

# end 옵션
print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')  # >>> Welcome to IT News Web Site

# file 옵션 (별도의 파일로 출력)
import sys

print('Learn Python', file=sys.stdout)
print()

# format 사용(d : 3, s : 'python', f : 3.1454545)
print('%s %s' % ('one', 'two'))  # >>> one two
print('{} {}'.format('one', 'two'))  # >>> one two
print('{1} {0}'.format('one', 'two'))  # >>> two one

# %
print('%10s' % 'nice')  # >>>       nice
print('{:>10}'.format('nice'))  # >>>       nice

print('%-10s' % 'nice')  # >>> nice
print('{:10}'.format('nice'))  # >>> nice

print('{:_>10}'.format('nice'))  # >>> ______nice
print('{:^10}'.format('nice'))  # >>>    nice     (중앙 정렬)

print('%.5s' % 'nice')  # >>> nice
print('%.5s' % 'pythonstudy')  # >>> pytho(5자리로 절삭 하여 반환)
print('{:10.5}'.format('pythonstudy'))  # >>> pytho   (공간은 10자리지만 5글자까지만 반환)

# %d
print('%d %d' % (1, 2))  # >>> 1 2
print('{} {}'.format(1, 2))  # >>> 1 2

print('%4d' % 42423242)  # >>> 42423242
print('{:4d}'.format(42))  # >>>  42(앞에 두자리 공백)

# %f
print('%1.8f' % 3.14343434343434)  # >>> 3.14343434(정소부는 1자리, 소수부는 8자리 까지 출력)
print('%f' % 3.14343434343434)  # >>> 3.143434
print('{:f}'.format(3.14343434343434))  # >>> 3.143434

print('%06.2f' % 3.141592653589793)  # 003.14
print('{:06.2f}'.format(3.141592653589793))  # 003.14
