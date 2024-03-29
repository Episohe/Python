# chapter 10-2
# 행맨 게임 만들기
# 프로그램 완성 및 최종 테스트
import csv
import random
import time

import winsound

# 처음 인사
name = input("What is your name?")

print("Hi," + name + ". Let's Play Hangman!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word.csv', 'r') as f:
    reader = csv.reader(f)
    # Header skip
    next(reader)
    for c in reader:
        words.append(c)

# 리스트 섞기
random.shuffle(words)

q = random.choice(words)

# 정답 단어
word = q[0].strip()

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
    if failed == 0:
        print()
        print()
        # 성공 사운드
        winsound.PlaySound('./sound/good.mp3', winsound.SND_FILENAME)
        print('Congratulations! The guesses is correct!')
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
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
            # 실패 사운드
            winsound.PlaySound('./sound/bad.mp3', winsound.SND_FILENAME)
            # 실패 메시지
            print("hangman game failed. Bye!")
