won = input("원화 금액을 입력 하세요>>>>")
dollar = input("환율을 입력 하세요>>>>")

try:
    print(int(won) /  int(dollar))
except ValueError as e : # 예외 발생시 실행 되는 코드
    print("예외가 발생했습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생했습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행 되는 코드")
finally:  # 파일 닫기
    print("무조건 실행 되는 코드")

