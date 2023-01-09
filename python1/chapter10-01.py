# chapter 10-1
# 행맨 게임 만들기

# 기본 프로그램 제작 및 테스트

import time

# 처음 인사
name = input("What is your name?")

print("Hi," + name + ". Let's Play Hangman!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# 정답 단어
word = "python"

# 추측 단어
guesses = ""

# 기회
turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아 있을 경우
while turns > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내에 추측 문자가 포함 되어 있다면
        if char in guesses:
            # 추측 단어 출력
            print(char, end='')
        else:
            # 틀린 경우 대시로 처리
            print('_', end='')
            failed += 1
    print('')
    print(failed)
    if failed == 0:
        print()
        print()
        print('Congratulations! The guesses is correct!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    guess = input("guess a character.")

    # 단어 더하기
    guesses += guess

    # 정담 단어에 추측한 문자가 포함 되어 있지 않으면
    if guess not in word:
        turns -= 1
        # 오류 메세지
        print("Oops! Wrong")
        # 남은 기회 출력
        print("You have", turns, 'more Guesses!')

        if turns == 0:
            # 실패 메시지
            print("hangman game failed. Bye!")
