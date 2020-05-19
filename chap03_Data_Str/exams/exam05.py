"""
step04, 05 문제

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.

 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict
"""

position = ['과장', '부장', '대리', '사장', '대리', '과장']
print(type(position))
# 문1
position2 = set(position)
print(position2, type(position2)) # set

# 문2 - 1
lev = {} # dict
for i in position:
    if i in lev:
        lev[i] += 1
    else:
        lev[i] = 1
print(lev)

lev = {}
for i in position:
    lev[i] = lev.get(i, 0) + 1 # lev.get(key값, 없다면 0 만약 키값이 있다면 0은 의미 없는 숫자로 바뀜)
print(lev)
