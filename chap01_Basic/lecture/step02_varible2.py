"""
step01 에서 공부했던 내용 +
"""

# 1 변수 생성 방법
'''
python 에서 변수명의 조건!!
 1. 영문자(대, 소문자 구분), 숫자, 언더바(_) 를 사용할 수 있다.
 2. 변수명의 첫 자리에는 숫자가 올 수 없다
 3. 파이썬에 저장되어있는 약속된 단어들(ex) True, False, import, from)은 변수명으로 사용할 수 없다 
'''
# 올바른 변수명 예시
var1 = "올바른 변수명"
Var1 = "var1과 다른 올바른 변수명"
var1_3 = "다른 올바른 변수명"
_var1 = "또다른 올바른 변수명"
Var1_ = "색다른 올바른 변수명"

# 틀린 예시
'''
1var = "오류나는 변수명"
+var = "오류나는 변수명"
var.test = "오류나는 변수명"   ( R 에서는 .이 변수명에 사용되지만 python에서 .은 
'''

'''
step01 에서 
형식) 변수명 = 값 or 수식 or 다른 변수명 이렇게 설명했다.
이번에는 변수명에 수식 그리고 다른 변수명을 입력하는 작업을 해보겠다.
'''
# 연습
# 변수에 수식
var1 = 5 + 7
print(var1, type(var1)) # 결과 값 : 12 <class 'int'>

# 변수에 기존 변수에 저장된 값을 그대로 저장
var2 = var1
print(var2, type(var2)) # 결과 값 : 12 <class 'int'>

var1 = 1

# 변수에 값을 넣는것은 = 하나로 여러게 변수를 생성 가능하고 변수명과 저장될 값들은 순서대로 저장된다
v1, v2 = 100, 200
print(v1, v2)
# 이 작업 설명을 순서대로 저장된다고 했지만 여기서 순서대로라는것은 방향성만 갖고 시간의 의미는 없다
# 순서대로 라는 의미를 위해 다음 작업을 해보자

v1, v2 = v2, v1
# 위 작업에 순서대로가 시간의 의미까지 포함된다면 v1에 v2 값이 저장되고 v2에 v2가 저장된 v1값이 반영되어야 한다는 의미이다
# 하지만
print(v1, v2)  # 200, 100
# 결과에 따르면 v2가 저장되지 않은 v1값이 v2에 반영이 되어있다.
# 방향성은 있지만 동시에 작업을 하는 것!!

# 2. 연산자 : 산술, 관계, 논리
num1 = 100
num2 = 50  # 이 두 변수를 통해 여러 계산을 해보자

# 2.1 사칙연산
add = num1 + num2
mnus = num1 - num2
mult = num1 * num2
div = num1 / num2

# 2.2
div2 = num1 // num2 # 몫을 구할때는 // 을 이용한다
div3 = num1 % num2  # 나머지 값을 구할때는 % 를 이용한다
square = num1**2  # 제곱을 할때는 ** 를 이용한다
# num1^2 은 R에서 사용한다

print(add, mnus, mult)
print(div, div2, div3)
print(square)


# 3. 관계 연산자
# 1) 동등비교
bool_re = num1 == num2
print(bool_re)

bool_re = num1 != num2
print(bool_re)

# 2) 대소관계 : >, >=, <, <=
bool_re = num1 >= num2
print(bool_re)

print("논리 연산자")  # or, and, not
bool_re = num1 <= num2 or num1 <= 10
print(bool_re)  # False

bool_re = num2 <= num1 <= 10
print(bool_re)  # False
