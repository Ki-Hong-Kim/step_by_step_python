"""
[주요 메타문자]
. : 임의의 한 문자
.x : 임의의 한 문자 뒤에 x가 오는 문자열
^x : x로 시작하는 문자열(접두어 추출)
x$ : x로 끝나는 문자열(접미어 추출)
x. : x 다음에 임의의 한 문자가 오는 문자열(ex : t1, t2, ta -> t.)
x* : x가 0번 이상 반복
x+ : x가 1개 이상 반복
x? : x가 0 또는 1개 존재
x{m, n} : x가 m~n 사이 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
[x] : x문자 한 개 일치
"""


# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']

# 텍스트 전처리2
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

'''
# 라이브러리 임포트 하는 방법
import re  # 방법1) 정규포현식 모듈
re.findall()  # 방법1) 

from re import findall, match, sub  # 방법2) from 모듈 import 함수
findall()  # 방법2)
'''

import re
from re import findall

# 1. findall
# 형식: findall(pattern='메타문자 패턴', string='문자열')

# 1) 숫자 찾기
st1 = '1234 abc홍길동 ABC_555_6 이사도시'
print(re.findall('1234', st1))  # ['1234'] == list 타입
print(findall('[0-9]{3}', st1))  # 숫자가 연속 3번 나오는 값을 st1 에서 모두 가져오라
print(findall('[0-9]{3,}', st1))  # 숫자가 연속 3번 이상 나오는 값을 st1 에서 모두 가져오라
print(findall('\\d{3,}', st1))

# 2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))  # ['홍길동', '이사도시']
print(findall('[a-z]{3}', st1))  # ['abc']
print(findall('[A-z]{3}', st1))  # ['abc', 'ABC']
print(findall('[a-z|A-Z]{3}', st1))  # ['abc', 'ABC']

str_list = st1.split(sep=' ')
print(st1)
print(str_list)

names = []
names2 = []
for s in str_list:
    tmp = findall('[가-힣]{3,}', s)
    print(tmp)  # [], ['홍길동'], [], ['이사도시']
    if tmp:  # 빈리스트는 False, 내용이 있으면 True
        names.append(tmp)
        names2.append(tmp[0])

print(names)  # [['홍길동'], ['이사도시']] - 중첩 리스트
print(names2)  # ['홍길동', '이사도시'] - 단일 리스트

# 3. ^접두어 / 접미어$  문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
print(findall('^test', st2))  # ['test']
print(findall('test', st2))   # ['test', 'test']
print(findall('st$', st2))    # ['st']

# 종료 문자 찾기
print(findall('.bc', st2))  # ['abc', 'mbc']
print(findall('t.', st2))   # ['te', 't1', 'te']
print(findall('.t.', st2))  # ['st1', '5te']

# 4. 단어 찾기 (\\w): 한글, 영문자, 숫자, ... (인식가능) 불용어, 특수문자, ... (인식불가)
st3 = 'test^홍길동 abc 대한*민국 123$tbc'

words = findall('\\w{3,}', st3)  # 리스트로 반환
print(words)  # ['test', '홍길동', 'abc', '123', 'tbc']

# 5. 특정 문자열 제외
print(findall('[^t]+', st3))  # ['es', '^홍길동 abc 대한*민국 123$', 'bc']
print(findall('[^t]', st3))

# 특수 문자 제외
print(findall('[^^*$]+', st3))


# 2. match
# match(pattern='패턴', string='문자열')
#  - 패턴 일치 여부 반환(일치시: object 반환 / 불일치: NULL 반환)
from re import match

jumin = "123456-1234567"
jumin2 = "123456-5234567"
result = match("[0-9]{6}-[1-4]\\d{6}", jumin)
print(result[0])
result2 = match("[0-9]{6}-[1-4]\\d{6}", jumin2)
if result:
    print("정상 주민번호")
else:
    print("비정상 주민번호")

# 3. sub('pattern', 'rep', 'string')  string 에서 발견되는 pattern 을 rep 으로 대체
from re import sub
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
result = sub('[\^*$]', '', st3)
print(result)
