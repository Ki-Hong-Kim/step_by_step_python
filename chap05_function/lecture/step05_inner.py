"""
중첩함수(inner function

형식)
def outer_func(인수):
    실행문
    def inner_func(인수):
        실행문
    return inner_func

"""


# 1. 중첩함수 예
def a():  # outer 함수
    print('outer 함수 a 이다')

    def b():  # inner 함수
        print('inner 함수 b')

    return b


b = a()  # outer 함수 호출 - a 함수 = 일급 함수
b()  # inner 함수 호출 - b 함수 

# 2. 중첩함수 응용
'''
inner 함수 종류
getter(): 함수내의 data를 외부 획득자
setter(): 함수내의 data를 지정자 
'''


def outer_func(data):
    dataSet = data  # 데이터 저장

    # inner : 데이터 조작
    def tot():  # 합계
        tot_val = sum(dataSet)
        return tot_val

    def avg(tot_val):  # 평균 = 합계 / n
        avg_val = tot_val / len(dataSet)
        return avg_val

    # getter
    def getData():
        return dataSet

    # setter
    def setdata(newData):
        nonlocal dataSet  # outer 변수 (nonlocal을 써야 outer함수에서 dataSet을 가져옴)
        dataSet = newData  # dataSet: 지역변수 

    return tot, avg, getData, setdata


data = list(range(1, 101))
tot, avg, getData, setdata = outer_func(data)  # 일급함수(tot, avg)

tot_val = tot()  # 합계
avg_val = avg(tot_val)

print('tot =', tot_val)
print('avg =', avg_val)
print('dataset = ', getData())

newData = list(range(1, 51))
setdata(newData)  # dataSet 변경

# getter 이용: dataSet 확인
print('dataSet = ', getData())

# 3. 함수 장식자 : Tensorflow2.0
# - 기존 함수 결과의 시작부분과 종료부분에 기능을 추가해서 장식 역할
'''
형식) 
@함수장식자
def 함수명():
    실행문 
'''


# 함수장식자 작성
def hello_doco(func):  # outer: 함수를 인수로 받는 역할
    def inner():  # inner: 함수를 장식하는 역할 / hello 인수를 받음
        print('-'*20)
        func()  # 함수 실행
        print('-'*20)
    return inner


@hello_doco
def hello(name):
    print('my name is ', name, '!!!')


# 함수 호출
hello('김기홍')

# 구구단 장식하기
'''
**** 2단 ****
 2 * 1 = 2
 2 * 2 = 4
     .
     .
     .
 2 * 9 = 18
*************     
'''



# 구구단 함수 장식자
def gugu_deco(gugu_func):
    def inner(dan):
        print('*'*4, dan, '*'*4)
        gugu_func(dan)
        print('*'*20)
    return inner



# 구구단 계산
@gugu_deco
def gugu(dan):
    for i in range(1, 10):
        print("%d * %d = %d"%(dan, i, dan*i))

dan = int(input('단 입력(2~9): '))

gugu(dan)