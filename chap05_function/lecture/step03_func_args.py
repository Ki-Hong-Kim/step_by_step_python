"""
함수의 가변인수
    - 한 개의 가인수로 여러개의 실인수를 받는 인수
    형식)  def 함수명(*인수)
"""


# 1. tuple 형으로 받는 가변인수
def Func1(name, *names):  # *가 붙은 인수는 가변인수를 의미함
    print(name)  # 홍길동
    print(names)  # ('이순신', '유관순')


Func1('홍길동', '이순신', '유관순')

# 패키지.모듈
import scatter.scatter_module  # 방법1) import 패키지.모듈
from scatter.scatter_module import Avg, var_std  # 방법2)

datas = [2, 3, 5, 7, 8]
avg1 = scatter.scatter_module.Avg(datas)
avg2 = Avg(datas)
print(avg1)
print(avg2)

var, std = var_std(datas)
print('var = ', var)
print('std = ', std)


def statis(func, *data):
    if func == 'sum':
        return sum(data)
    elif func == 'avg':
        return Avg(data)
    elif func == 'var':
        return var_std(data)
    elif func == 'std':
        return var_std(data)
    else:
        return '해당 함수 없음'


print('sum =', statis('sum', 1, 2, 3, 4, 5))
print('avg =', statis('avg', 1, 2, 3, 4, 5))
var, _ = statis('var', 1, 2, 3, 4, 5)  # 함수 결과가 2개를 가져올때 필요한것만 받으려면 _를 이용해 불필요한 데이터 안받음
print('var =', var)
_, std = statis('std', 1, 2, 3, 4, 5)
print('std =', std)


# 2. dict형 가변인수
def person(w, h, **other):
    print('w = ', w)
    print('h = ', h)
    print(other)


# 3. 함수를 인수로 받기
def square(x):
    return x ** 2


def my_func(func, datas):
    result = [func(d) for d in datas]
    return result


datas = [1, 2, 3, 4, 5]
my_func(square, datas)
