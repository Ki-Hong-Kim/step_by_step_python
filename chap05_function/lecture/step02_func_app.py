"""
사용자 정의 함수 응용
"""


# 1. 텍스트 전처리 용도 함수
def clean_text(texts):
    from re import sub
    texts_re = texts.lower()  # 1. 소문자 변경
    text_re2 = sub('[0-9]', '', texts_re)  # 2. 숫자 제거
    punc_str = '[.,;:?!]'  # 3. 문장 부호 제거
    text_re3 = sub(punc_str, '', text_re2)
    spec_str = '[@#$%^&*~()]'  # 4. 특수문자 제거
    text_re4 = sub(spec_str, '', text_re3)
    text_re5 = sub('[a-z]', '', text_re4)
    text_re6 = sub('  ', ' ', text_re5)  # 5. 공백 제거
    return text_re6

# 텍스트 전처리 2
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print('텍스트 전처리 전')
print(texts)
print(len(texts))

print('텍스트 전처리 후')
text_re = [clean_text(i) for i in texts]
print(text_re)

# 2. 표본의 분산과 표준편차
from statistics import mean, variance, stdev

dataset = [2, 4, 5, 6, 1, 8]
print(mean(dataset))
print(variance(dataset))
print(stdev(dataset))

'''
분산 = sum((x변량 - 산술평균)**2) / n-1
표준편차 = sqrt(분산) 
'''
avg = mean(dataset)

from statistics import mean
from math import sqrt


def var_std(dataset):
    avg = mean(dataset)  # 산술평균
    diff = [(x - avg) ** 2 for x in dataset]
    diff_sum = sum(diff)

    var = diff_sum / (len(dataset) - 1)
    std = sqrt(var)
    return var, std


var, std = var_std(dataset)
print('분산', var)
print('표준편차', std)
