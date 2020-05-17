"""
List 특징
 - 1차원 배열 구조
    형식) 변수 = [값1, 값2, ...]
 - 다양한 자료형 저장 가능
 - index 사용, 순서 존재
    형식) 변수[index], index = 0
- 값 수정(추가, 삽입, 수정, 삭제)

extend
append
sort
lst 에 연산
"""

# 1. 단일 list
lst = [0, 1, 2, 3, 4]
print(lst, type(lst), len(lst))

for i in lst:
    print(i, end= " ")

    print(lst[i-1:])  # 변수[start : stop]
print("\n", lst[i-1:])

for i in lst:
    print(lst[: i])


# 처음 / 마지막 데이터 추출

x = list(range(1, 101))  # 1 ~ 100
print(x)
print(x[:5])
print(x[-5:])  # 뒤에서 5번째 부터 마지막 까지

'''
index 형식
변수[start=0 : stop-1 : step=1]
'''
print(x[:])     # 전체 데이터
print(x[::2])   # [ 0 :: step=2] : 홀수
print(x[1::2])  # [start = 1 :: step=0] : 짝수
print(x[1:50:3])# 1부터 50까지 step = 3

# 2. 중첩 list : [[], []]  ->  1차원
a = ['a', 'b', 'c']
b = [10, 20, 5, True, 'hong', a]
print(b)         # [10, 20, 5, True, 'hong', ['a', 'b', 'c']]
print(b[5])      # ['a', 'b', 'c']
print(b[5][1])   # b
print(b[5][1:])  # ['b', 'c']
print(type(a), type(b), '\n', id(a), id(b))
# <class 'list'>   <class 'list'>
#  2147239354056   2147239234504

# 3. 값 수정 (추가, 삽입, 수정, 삭제)
num = ['one', 'two', 'three', 'four']
print(len(num))  # 4
num.append('five')  # 원소 추가
print(num)  # ['one', 'two', 'three', 'four', 'five']
num.remove('five')  # 원소 삭제
print(num)  # ['one', 'two', 'three', 'four']
num.insert(0, 'zero')  # 첫번째 위치에 원소 삽입
print(num)  # ['zero', 'one', 'two', 'three', 'four']
num[0] = 0  # 원소 수정 (첫번째 위치의 원소를 숫자 0으로 수정)
print(num)  # [0, 'one', 'two', 'three', 'four']

# 4. list 연산 (+(결합), *(확장))
# 1) list 결합
x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y    # new object
print(z, type(z))  # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장
x2 = x
x3 = x
x2.extend(y)
print(x2)     # [1, 2, 3, 4, 1.5, 2.5] -- 단일 list

#  (결합과 확장의 차이점 : 새로운 object가 생기는지)

# 3) list 추가
x.append(y)  # 기존 object
print(x)     # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]] -- 중첩 list

# 4) list 곱샘(*)
lst = [1, 2, 3, 4]
result = lst * 2  # list 2번 반복
print(result)     # [1, 2, 3, 4, 1, 2, 3, 4]  = len(lst)가 2배가 됨

# 5. list 정렬
result.sort()  # 기본: 오름차순
print(result)  # [4, 4, 3, 3, 2, 2, 1, 1]

result.sort(reverse=True)  # 내림차순
print(result)  # [4, 4, 3, 3, 2, 2, 1, 1]

'''
# 6. scala vs vector
scala 변수  : 한 개의 상수(값)를 갖는 변수(크기)
vector 변수 : 다수의 값을 갖는 변수(크기, 일정한 방향)  
'''
dataset = []  # 빈 list
size = int(input("vector size : "))  # scala 변수

for i in range(size):
    dataset.append(i+1)  # vector 변수 생성 (i 는 0부터 시작)
    print(dataset)
print(dataset)

'''
7. list에서 원소 찾기
if 값 in list :
    참 실행문
else :
    거짓 실행문
'''

if 5 in dataset:
    print("있다 있어!")
else:
    print("없다 없어..")
