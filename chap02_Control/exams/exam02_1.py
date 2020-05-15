"""
step02 문제
"""

'''
문1) 다음 밑변, 윗변, 높이를 이용하여 사다리꼴의 넓이를 구하시오.

    조건1) 밑변(base), 윗변(upper), 높이(height)
              밑변 = 12, 윗변 = 7, 높이 = 9
    조건2) 사다리꼴 넓이(area) = (밑변 + 윗변) * 높이 / 2
    조건3) 소수점 3자리 까지 출력 : format()이용 

   <<화면출력 결과>>
 밑변 입력 : 12
 윗변 입력 : 7
 높이 입력 : 9
 사다리꼴 넓이 =  85.500
'''
base = 12
upper = 7
height = 9

print("밑변 입력: ", base)
print("윗변 입력: ", upper)
print("높이 입력: ", height)
print("사다리꼴 넓이 = %2.3f" % ((base + upper) * height / 2))  # 정수자리 2자리제한 / 소숫점자리 3글자
print("사다리꼴 넓이 = ", format((base + upper) * height / 2, '2.3f'))
