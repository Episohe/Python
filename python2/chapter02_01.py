"""
객체지향 (OOP)

- 프로그램을 실제 세상에 가깝게 모델링하는 기법
- 데이터를 추상화시켜 속성과 행위를 가진 객체로 만들고, 그 객체 간의 상호작용을 통해 로직을 구현하는 프로그래밍 방법
- 코드 중복을 방지하고 재사용성을 높임

객체지향(OOP) 원칙

- 캡슐화
- 추상화
- 상속
- 다형성

클래스 (Class)

- 특별한 데이터와 메서드의 집합
- 설계도(틀)
- 메모리상에 올라가지 않음

객체 (Object)

- 하나의 class로 만들어진 여러 instance(object)는 각각 **독립적**이다.

"""
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트 구조 -> 관리 불편 / 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)
print('-----------------------------------------------------')

# dictionary 구조
# 코드 반복, 중첩 문제(키), 키 조회 예외 처리

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {'color': 'white', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'car_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dicts[1]

print(car_dicts)
print('-----------------------------------------------------')


# 클래스 구조
# 구조 설계 후 재사용 증가, 코드 반복 최소화, 메소드 활용
class Car():
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    def __reduce__(self):
        pass


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)

print(dir(car1))

print('-------------------------------------------------------------------------')
# list 출력 -> repr
car_list = [car1, car2, car3]

print(car_list)
print('-------------------------------------------------------------------------')
# str 출력
for i in car_list:
    print(i)
