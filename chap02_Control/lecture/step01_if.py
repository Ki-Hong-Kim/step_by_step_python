"""
제어문 : 조건문(if), 반복문(while, for)
python 블럭 : 콜론과 들여쓰기

형식 1)
if 조건식 :
    실행문
    실행문
"""

var = 10
if var >= 15:
    print('var =', var)
    print('var는 15보다 크거나 같다.')


'''
 형식2)
if 조건식 :
    실행문1
else :
    실행문2
'''
var = 2
if var >= 5:
    print('var는 5보다 크거나 같다.')
else:
    print('var는 5보다 작다.')

# 키보드 점수 입력 -> 60점 이상 : 합격, 미만 : 불합격
score = int(input("점수 입력 :"))

if int(input("점수 입력 :")) >= 60:
    print('합격')
else:
    print('불합격')

import datetime  # module 임포트 (R에서 library 와 같음)

today = datetime.datetime.now()  # module.class.method() == 모듈 datetime 에 datetime 클래스의 기능중인 현재시각 출력을 사용함
print(today)

# 요일 반환
week = today.weekday()
print(week)  # 0 ~ 4 평일 5, 6 주말  // 2가 수요일

if week >= 5:
    print('오늘은 휴일')
else:
    print('오늘은 평일')

'''
if 조건식1 :
    실행문
elif 조건식2 :
    실행문
else :
    실햄문
'''
#  문2) 키보드 score 입력 : A(100~90), B(90~80), C, D, F(59미만) 출력
score = int(input("점수입력(0~100): "))
# 전역변수 : score, grade
if score >= 90:
    print(" A 학점 ")
    grade = "A 학점"
elif score >= 80:
    grade = "B 학점"
elif score >= 70:
    grade = "C 학점"
elif score >= 60:
    grade = "D 학점"
else:
    grade = "F 학점"
    print(" F 학점 ")

print('당신의 점수는 %d이고, 등급은 %s이다.' % (score, grade))

# 블럭 if vs 라인 if
num = 9
if num >= 5:
    result = num * 2
else:
    result = num + 2

print(result)

# 라인 if
# 형식) 변수 = 참 if 조건문 else 거짓
result = num * 2 if num >= 5 else num + 2
# [해석] 조건식이 참이라면 num * 2 를 수행 거짓이라면 num + 2를 수행
print(result)
