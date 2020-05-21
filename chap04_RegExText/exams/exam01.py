"""
문1) 다음 emp '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하시오.

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
"""

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260김기홍"]

emp_list = []
emp_list2 = []
emp_list3 = []
for i in emp:
    temp = findall('[가-힣]{3,}', i)
    if temp:  # 만약 이름데이터가 없는 경우 빈 리스트를 저장하지 않기 위해서
        emp_list2.append(temp)
        emp_list.append(temp[0])
        emp_list3.extend(temp)
print(emp_list2)               # 다중리스트
print('names = ', emp_list)    # 단일리스트
print(emp_list3)

# 단순화 (형식=> 변수 = [실행문 for 변수 in 열거형객체]
names = []
names = [findall('[가-힣]{3,}', e)[0] for e in emp]

names.extend([findall('[가-힣]{3,}', e) for e in emp])
print(names)
