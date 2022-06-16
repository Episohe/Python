# 객체 지향

class Car():
    """
    Car Class
    Author : So hee
    Date: 2022.06.16
    Description : Class, Station, Instance Method
    """

    # 클래스 변수(모든 instance 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return 'str: {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr: {} - {}'.format(self._company, self._details)

    # Instance Method
    # self: 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print("Car Detail Info: {} {}".format(self._company, self._details.get('price')))

    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price: {}'.format(self._company, self._details.get('price'))

    # Instance Method
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price: {}'.format(self._company,
                                                                   self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print("Please Enter 1 or More")
            return
        cls.price_per_raise = per
        print('Succeed! price increased!')

    # static Method
    # 이 차가 BMW에서 나온 차인지 확인 하는 함수
    @staticmethod
    def is_bmw(inst):
        if inst._company == "Bmw":
            return 'OK! This car is {}'.format(inst._company)
        return 'Sorry! This car is not Bmw'


# self 의미
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 7000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 전체 정보 출력
car1.detail_info()

# 가격 정보 출력 (좋지 않은 방법) 직접 접근
print(car1._details.get('price'))
print(car2._details['price'])

# 가격 정보 (인상 전)
print(car1.get_price())

# 가격 인상 (class Method 미사용)
Car.price_per_raise = 1.4

# 가격 정보 (인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())

# 가격 인상
Car.raise_price(1.6)

# is_Bmw (instance 호출 OR Class 호출)
print(car1.is_bmw(car1))
print(Car.is_bmw(car1))
print(car2.is_bmw(car2))
print(Car.is_bmw(car2))

