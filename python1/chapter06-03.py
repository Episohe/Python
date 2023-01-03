# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대 경로 : ..(부모) .(현재 디렉토리) -> 모듈 내부에서만 사용
# __init__.py : Python 3.3부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성을 추천함.

import python1.sub.sub1.module1
import python1.sub.sub2.module2

# 예제 1

# 사용
python1.sub.sub1.module1.mod1_test1()
python1.sub.sub1.module1.mod1_test2()

python1.sub.sub2.module2.mod2_test1()
python1.sub.sub2.module2.mod2_test2()

# 예제 2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print()
print()

# 예제
# 전체로 가져 오는 것은 지양!

module1.mod1_test1()
module1.mod1_test2()
