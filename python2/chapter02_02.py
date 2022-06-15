# 객체 지향

class Car():
    """
    Car Class
    Author : So hee
    Date: 2022.06.15
    """

    # 클래스 변수
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info: {} {}".format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1


# self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 7000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
print(car1.__dict__)

# Docstring
print(Car.__doc__)

print('------------------------------------------------------------')

# 실행
car1.detail_info()
Car.detail_info(car1)

car2.detail_info()
Car.detail_info(car2)

print('------------------------------------------------------------')

# 비교 -> 다 같은 class 때문에 같음

print(id(car1.__class__), id(car2.__class__), id(car3.__class__))

# 공유 확인
print(car1.car_count)
print(car1.__dict__)
print(dir(car1))

# 접근
print(car1.car_count)
print(Car.car_count)

# 에러
Car.detail_info(car1)

del car2
# 삭제 확인
print(Car.car_count)

# 인스턴스 네임스페이스에 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수)


