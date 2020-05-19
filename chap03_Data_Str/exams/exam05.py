"""
step04, 05 문제

 문1) 중복 되지 않은 직위 출력 하시오.
 문2) 각 직위별 빈도수를 출력하시오.

 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] : list -> set -> list
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} -> dict
"""

position = ['과장', '부장', '대리', '사장', '대리', '과장']
# 문1
position2 = set(position)
print(position2, type(position2))

# 문2 - 1
lev = {}
for i in position:
    if i in lev:
        lev[i] += 1
    else:
        lev[i] = 1
print(lev)

lev = {}
for i in position:
    lev[i] = lev.get(i, 0) + 1
print(lev)
