"""
재귀호출(recursive call)
 - 함수 내에서 자신의 함수를 반복적으로 호출하는 기법
 - 반복적으로 변수의 값을 조정해서 연산 수행
ex) 1 ~ n 누적합 (1 + 2 + 3 + ... + n)
 - 반드시 종료조건 필요
"""


# 1. 카운터 : 1 ~ n
def Counter(n):
    if n == 0:  # 종료조건
        # print('프로그램 종료')
        return 0  # 함수 종료
    else:
        Counter(n - 1)  # 재귀호출
        '''
        1. stack : [5(first), 4(5-1), 3(4-1), 2(3-1), 1(2-1), 0(1-1)]
        2. stack 역순으로 출력
        '''
        print(n, end=' ')  # 2. 카운트 : 1 2 3 4 5


print(Counter(0))
print(Counter(5))  # 자장된 stack의 역순으로 출력


# 2. 누적(1 + 2 + 3 +  ~ + n)
def adder(n):
    if n == 1:  # 종료조건
        print('프로그램을 종료합니다')
        return 1
    else:
        result = n + adder(n - 1)  # 재귀 호출 -> 2. 누적
        '''
        stack : LIFO(후입선출)
        1. tack [5(first), 4(5-1), 3(4-1), 2(3-1)]   1(2-1) 종료조건이라 포함 안됨
        2. stack 역순으로 누적 : 1(종료조건 반환값) + [2 + 3 + 4 + 5] = 15
        '''
        print(result, end=' ')
        return result


adder(2)


def Factorial(n):
    if n == 1:
        return 1
    else:
        result = n * Factorial(n - 1)

        print(result, end=' ')
        return result

Factorial(5)
