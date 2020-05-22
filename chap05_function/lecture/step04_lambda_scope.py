"""
1. 축약함수(lambda)
    - 한 줄 함수
    형식) 변수명 = lambda 인수: 리턴값
    ex) lambda x, y : x + y

2. scope
    - 전역변수, 지역변수(함수)
"""

# 1. 축약함수
# - 일반적 블럭형 함수
def adder(x, y):
    add = x + y
    return add

# - 축약 함수
add = lambda x, y: x + y
# [lambda x, y: x + y for 변수 in 열거형 객체]
re_add = add(500, 269)
print(re_add)

# 2. 전역변수
'''
전역변수 : 전지역에서 사용되는 변수
지역변수 : 특정 지역(함수)에서만 사용되는 변수
'''

x = 50  # 전역변수
def local_func(x):
    x += 50
    return x  # x = 100 (해당 함수가 종료되면 자동으로 소멸)

local_func(x)
print('x=', x)

def global_func( ):
    global x  # 전역변수
    x += 50

global_func()
print('x = ', x)