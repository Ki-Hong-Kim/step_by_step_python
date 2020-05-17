
"""
 리스트 내포
    - list 에서 for 문 사용          ** 실행문은 조건이 참일경우에만 실행
    형식1) 변수 = [실행문 for 변수 in 열거형 객체]
        실행순서  : 1. for 문 > 2. 실행문 > 3. 변수 저장
    형식2) 변수 = [실행문 for 변수 in 열거형객체 if 조건식]
        실행순서 : 1. for 문 > 2. if문 > 3. 실행문 > 4. 변수 저장
"""

# 형식1) 변수 = [실행문 for 변수 in 열거형 객체]
# x각 변량에 제곱
x = [2, 4, 1, 3, 7]

# x**2
data = []
for i in x:
    print(i**2)
    data.append(i**2)
print(data)   # [4, 16, 1, 9, 49]

data2 = [i**2 for i in x]
print(data2)  # [4, 16, 1, 9, 49]

# 형식2) 변수 = [실행문 for in 열거형객체 if 조건식]
# 1 ~ 100 -> 3의 배수
num = list(range(1, 101))
print(num)
data3 = [i for i in num if i % 3 == 0]
# 복잡하게 작성한 ver
data3 = []
for i in num:
    if i % 3 == 0:
        data3.append(i)

data3_1 = [i % 3 for i in num if i % 3 == 0] # % 는 나머지 값을 의미한다

# 내장함수 + 리스트 내포
print("sum = ", sum(x))  # 17
data4 = [[1, 3, 5], [4, 5], [7, 8, 9]]  # 중첩 list
result = [sum(d) for d in data4]
print(result)
