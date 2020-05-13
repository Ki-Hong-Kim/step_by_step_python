"""
반복문 (for)
형식)
for 변수 in 열거형 객체 :
    실행문
    실행문

열거형 객체(iterable)에 올 수 있는 데이터 타입 : string, list, tuple, set/dictionary
제너레이터 식 : 변수 in 열거형 객체
   (원소 순회 -> 변수 넘김) 순차적으로 열거형 객체에서 변수를 가져와 새로지정할 변수에 입력한다는 뜻
"""

# 1. string 열거형 객체 이용
string = '나는 홍길동 입니다.'
print(len(string))

num = list(range(10))
num2 = 250
len(num)

for s in string:  # string의 길이 만큼 반복
    print(s)

for s in string.split(sep=" "): # 구분자를 기준으로 추출해서 구분된 수만큼 반복
    print(s)

# 2. list 열거형 객체 이용
help(list)  # class
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))
print(len(lst))

lst2 = []
for i in lst:
    print(i, end=" ")
    # print 하고 끝 부분에 \n 이 기본값으로 있는데 " " 공백으로 설정하면서
    # 다음에 출력되는 기능이 붙어서 나옴
    lst2.append(i ** 2)  # 원소 추가(순서 보장)
    print(lst2)
    # lst의 길이만큼 반복했다면 이 위치에서 종료

print(lst2)

print("lst2 :", lst2)

# 1~100 까지 원소를 갖는 list 객체 생성
# range( start = 1, stop = 10, step = 1 ) --- 1 ~ 9 까지
# range( 2, 21, 2) --- 2 ~ 20 까지 2씩 증가
lst3 = list(range(1, 101))
print(lst3)

# 3. range 열거형 객체 이용
'''
 range(n) : 0 ~ n-1 정수
 range(start, stop) : start ~ stop-1 정수
 range(start, stop, step) : start ~ stop-1 (step 만큼 변하는) 정수
'''
num1 = range(10)  # 0~9
num2 = range(1, 10)  # 1~9
num3 = range(1, 10, 2)  # 1 3 5 7 9
print(list(num1), list(num2), list(num3), sep="\n")

for i in num1:
    print(i, end=' ')

# 4. list + range 열거형 객체 이용 #
idx = list(range(5))
idx2 = range(5)
# 출력결과 확인!!
print(idx)   # [0, 1, 2, 3, 4]
print(idx2)  # range(0, 5)

z = []
for i in idx:
    print(i, end=" ")
    z.append(i**2)

print(z)
'''    
# 문) list1에 1 ~ 100 까지 100개의 원소를 갖는 vector를 생성하고,
      list2에 3의 배수만 저장하기 
'''
list1 = list(range(1, 101))
list2 = []
for i in list1:
    if i % 3 == 0:  # 3 으로 나눴을때 나머지가 0인
        list2.append(i)
    else:
        pass
print(list2)

# index 이용 : 분류정확도
y = [1, 0, 2, 1, 0]  # 관측값 _ 범주형(0, 1, 2)
y_pred = [1, 0, 2, 0, 0]  # 예측값 _ 범주형(0, 1, 2)
size = len(y)
acc = 0

for i in range(size):  # range(5) : 0 ~ 4
    fit = int(y[i] == y_pred[i])  # int(True / False) -> 1 / 0
    acc += fit * 20  # 누적 변수
    print(fit)

print('분류정확도 = ', acc)

# 5. 이중 for 문
# 1) 구구단 예
for i in range(2, 10):  # 구구단 2단부터 9단까지  (i = 단수)
    print('*** %d단 ***' % i)

    for j in range(1, 10):  # 1 ~ 9 (j = 곱수)
        print("%d * %d = %d" % (i, j, (i * j)))
    print()  # line skip

para = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""
# 2) 문자열 처리
sents = []  # 문장 저장
words = []  # 단어 저장
for sent in para.split("\n"):  # 문단 -> 문장
    sents.append(sent)  # sents에 줄바꿈 단위로 분할한 구간 저장
    for word in sent.split():  # 문장 -> 단어   split의 기본값은 ' '
        words.append(word)  # 단어 저장
print(sents, '\n', '나뉜 문장 개수 :', len(sents), '\n', words, '\n', '나뉜 단어 개수 :', len(words))

# 제너레이터 식 : 변수 in 열거형 객체
'''
for 변수 in 열거형 객체 :
  -> 객체의 원소 수 만큼 반복
if 값 in 열거형 객체 :
  -> 객체의 원소 중에서 값이 있으면 True 아니면 False
'''

if input('검색단어 입력 : ') in words:  # ['나는', '홍길동', '입니다.', '주소는', '서울시', '입니다.', '나이는', '35세', '입니다.']
    print("해당 단어 있음")
else:
    print("해당 단어 없음")
