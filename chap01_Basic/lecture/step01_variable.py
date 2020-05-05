"""
변수 (Variable)
 - 자료를 저장하는 메모리 이름
 - 저장되는 데이터의 type에 대한 설정이 따로 필요 없다. (R과 동일)
 - 형식) 변수명 = 값 or 수식 or 다른 변수명
"""

# 1. 문자형 변수 생성 방법
var1 = 'hello'
var1_2 = 'hello'
var1_3 = "hello"
var2 = 'hello world'
# 여러 변수에 hello 와 hello world 라는 데이터를 저장

# 저장된 결과 확인 방법
print(var1)
print(var1_2)
print(var1_3)
print(var2)
# var2 만 제외하고 나머지 변수가 저장한 데이터는 같음 (여기서 데이터 저장시 '' 와 "" 큰 차이가 없다는 것을 알 수 있다)
# 빅데이터를 다룰때 중복되는 데이터들이 많지만 구분을 하기 위해 변수명에 차이를 둠

# 변수에 데이터 저장시 '' 와 "" 차이를 조금 더 정확하게 확인하는 방법
# id는 데이터값에 부여된 고유 번호를 호출하는 함수
print(id(var1))   # 2384215297840
print(id(var1_2)) # 2384215297840
print(id(var1) == id(var1_2) == id(var1_3))  # 결과 True


# 저장된 데이터의 type 확인 방법
print(type(var1))
print(type(var2))
# 따로 지정 안했지만 저동으로 str(string)이라는 type이 지정됨
# 변수에 데이터를 입력할때 '데이터' or "데이터" 이런 식으로 입력을 하면 문자형 type을 저장한다는 의미

# 2. 여러 type
# 숫자형
var3 = 100
var3_2 = 99.99
print(type(var3), type(var3_2)) # 결과 : int(integer) 정수형 / float(floating point number) 실수형

# 논리형 (True, False)
'''
논리형?
데이터를 분석하다보면 특정 조건에 부합한지 확인을 해야하는 경우가 많은데 그럴때 필요한 데이터 type 이다.
위에서 사용했드시 우리가 평소에 사용하는 = 은 같다라는 의미가 아니고 데이터 부여의 의미를 갖고있다.
python 에서 같다의 의미는 == 이고 같지 않다는 != 이다 (이상과 이하 초과와 미만은 일상에서 사용하는 비교연산자 사용방법은 같다 )
'''
# 예시
var4 = 500
var5 = 499.9
print(var4 == var5) # 해석 var4 와 var5 는 같은가?   결과: False
print(var4 != var5) # 해석 var4 와 var5 는 다른가?   결과: True
print(var4 >= var5) # 해석 var4 는 var5에 비해 크거나 같은가?   결과: True