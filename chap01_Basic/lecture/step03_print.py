"""
따로 설명하지 않은 print에 대한 설명
1. print는 출력하고자하는 내용의 결과를 출력을 하는 기본적인 기능이다.
2. 1개 이상의 값을 출력한다
3. 여러 값들을 출력할 때에는 기본적으로 공백으로 구분해서 출력한다. (공백대신 다른 것으로 수정가능)
4. print 끝부분에는 줄바꿈기능이 기본값으로 있다 (수정가능)
"""
# 1.  1개의 기본 변수 출력
var1 = "test"
var2 = '테스트'
var3 = 33
print(var1)
print(var2)
print(var3)

# 2. 저장된 변수명 없이 출력
print('test')
# print(test) 여기서 test는 변수명으로 인식하기 때문에 NameError: name 'test' is not defined 라는 에러가 발생한다
print(2323)   # 변수명을 숫자로 할 수 없으므로 숫자는 따옴표, 쌍따옴표 필요 없음
print('3232') # 따옴표 쌍따옴표로 숫자를 출력하면 숫자로 인식을 안하고 문자로 인식합니다

# 3. 2개 이상 복합적으로 출력
print(var1, var2)
print(var1, '연습 입력')
print(var3, 33, 35)
print('연습', 33, var3)
# print() 괄호 안에서 ,로 구분한 부분은 출력결과를 보면 공백으로 바뀐것을 알수 있다..

# 3_1 2개 이상 복합적으로 출력 (구분 기준을 / 로 바꿔서)
print(var1, var2, sep='/') # 공백이 사라지고 / 가 나왔다.
print(var1, var2, var3, var3, sep='/')

# 3_2 2개 이상 복합적으로 출력 (끝 부분에 줄바꿈을 바꿔서)
# _1
print(var1)
print(var2) # var과 var2를 드래그 후 연속으로 실행하면 다음줄로 넘어가서 바뀌는 것을 알 수 있다.

# _2
print(var1, var2, end='/')
print(var1)  # _2 아래 2줄을 드래그 후 실행시키면 줄이 바뀌지 않고 / 을 기준으로 한 줄로 출력 되는 것을 알 수 있다.

# 4. print 결과에 format 적용해서 출력하기