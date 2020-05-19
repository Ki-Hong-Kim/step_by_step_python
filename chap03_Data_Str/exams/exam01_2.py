"""
step2 관련 문제
"""
'''
A형 문) vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼 
          임의 숫자를 vector에 추가하고, vector의 크기를 출력하시오.
<출력 예시>
vector 수 : 3
4
2
5
vector 크기 : 3
'''
# A형 문제
import random

size = int(input('vector 수 : '))  # vector 크기 입력
lst = []
for i in range(size):
    lst.append(random.randint(min(list(range(size))), max(list(range(size)))))
print(lst)
print('vector 크기 :', len(lst))

"""
B형 문) .vector 수를 키보드로 입력 받은 후, 입력 받은 수 만큼
          임의 숫자를 vector에 추가한다.
          이후 vector에서 찾을 값을 키보드로 입력한 후
          해당 값이 vector에 있으면 "YES",  없으면 "NO"를 출력하시오
<출력 예시>
vector 수 : 5
1
2
3
4
5
3
YES

vector 수 : 3
1
2
4
3
NO
"""

def random_vecf():
    random_vec = []
    n = int(input('생성할 벡터의 수'))
    print('vector의 수 :', n)
    for i in list(range(n)):
        random_vec.append(random.randint(min(list(range(n))), max(list(range(n)))))

    print(random_vec)

    if int(input('찾고자하는 수')) in random_vec:
        print('yes')
    else:
        print('no')

random_vecf()
