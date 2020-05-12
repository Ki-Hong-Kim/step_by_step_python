"""
반복문(while)
while 조건식 :
    실행문
    실행문
"""

# 카운터, 누적변수
cnt, tot = 0, 0  # 변수 초기화 1
cnt = tot = 0  # 변수 초기화 2

while cnt < 5:  # 조건식이 True 라면 -> Loop(명령문 집합) 실행
    cnt += 1    # 실행문의 순서 중요
    tot += cnt
    print(cnt, tot)

# 문1 1~100 까지 합 출력하기
cnt = tot = 0
data = []
while cnt < 100:
    cnt += 1
    tot += cnt
    print(cnt, tot)
    if cnt % 2 == 0:  # cnt 를 2로 나눴을때 나머지가 0인 == 2의 배수 라면 뒤에오는 실행문을 실행하라
        data.append(cnt)  # 짝수값만 빈 리스트에 추가
print(data)

print("1~100까지 합 : %d" % tot)
print("짝수 값 :", data)

# 문2) 1~100 사이에서 5의 배수이면서 3의 배수가 아닌 값만 append 하기
cnt = 0
data = []

while cnt < 100:
    cnt += 1
    if cnt % 5 == 0 and cnt % 3 != 0:
        data.append(cnt)

print(data)  # 5의 배수이면서 3의 배수가 아닌 수들

# 무한 Loop 에는 종료조건 필요
while True:
    num = int(input("숫자 입력 :"))
    if num == 0:
        print("프로그램 종료")
        break  # 탈출(exit) : 종료 조건
    print("num = ", num)

# random : 난수 생성
import random

help(random.random)
help(random.choice)
help(random.randint)  # 지정한 범위 내에서의 난수 정수 뽑기

r = random.random()  # 모듈.난수(0~1 난수)
print('r = ', r)

r = random.randint(1, 5)  # (start, end)
print(r)  # 범위내의 정수 랜덤하게 선택

r = random.choice("가나다라")
print(r)

# 문3) 난수 0.01 미만이면 종료, 아니면 난수 개수 출력
# 조건 2
cnt = tot = 0
while True:
    ran = random.random()
    cnt += 1
    if ran < 0.01:
        print("프로그램 종료")
        print("난수 = ", ran, "누적 반복횟수 = ", cnt)
        break
    else:
        print("난수 = ", ran, "누적 반복횟수 = ", cnt)

# 조건 2
cnt = tot = 0
while True:
    ran = random.random()
    cnt += 1
    if ran < 0.01:
        print("프로그램 종료", '\n', '난수 = ', ran, '\n', '누적 반복횟수 = ', cnt)
        break
    else:
        pass
print("난수 = ", ran, "반복횟수 = ", cnt)

'''
숫자 맞추기 게임 만들기
숫자 범위 : 1~10
myInput == computer : 성공(exit) -> 종료 조건
myInput > computer : '더 작은 수 입력'
myInput < computer : '더 큰 수 입력'
'''
print(" >>> 숫자 맞추기 게임 <<< ")
compute = random.randint(1, 50)
while True:
    myInput = int(input("예상 숫자 입력 : "))  # 사용자 입력
    if myInput == compute:
        print(' 성공 ')
        break
    elif myInput > compute:
        print('더 작은 수 입력')
    else:
        print('더 큰 수 입력')

'''
continue vs break
 - 반복문에서 사용되는 명령어
 - continue : 반복을 지속, 다음 문장 skip
 - break : 반복 멈춤
'''

i = 0
while i < 10:
    i += 1

    if i == 3:
        continue
    if i == 6:
        break
    print(i)  # 1 2 4 5    3과 6은 제외됨
# continue 와 pass 의 차이
# continue 위치해있는 곳 다음 실행문을 강제한다는 의미
# pass는 실행할게 없을때 사용 (임시용)
