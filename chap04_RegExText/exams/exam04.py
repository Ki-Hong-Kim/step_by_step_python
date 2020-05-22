"""
문4) 다음 texts 객체를 대상으로 단계별로 텍스트를 전처리하시오.


 <텍스트 전처리 후 결과>
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
"""

# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

from re import sub

print('전처리 전 : ', texts)

# 1. 소문자 변경 
c_texts1 = [i.lower() for i in texts]
print(c_texts1)

# 2. 숫자 제거 
c_texts2 = [sub("[0-9]","", i) for i in c_texts1]
print(c_texts2)

# 3. 문장부호 제거
punc_str = '[.,;:?!]'
c_texts3 = [sub(punc_str, "", i) for i in c_texts2]
print(c_texts3)

# 4. 영문자 제거 
c_texts4 = [sub('[A-Z]', "", i) for i in c_texts3]
c_texts4 = [sub('[a-z]', "", i) for i in c_texts4]
print(c_texts4)

# 5. 특수문자 제거
ex_str = '[~#$%^&*()]'
c_texts5 = [sub(ex_str, "", i) for i in c_texts4]
print(c_texts5)

# 6. 공백 제거(2칸 이상 공백 -> 1칸 공백)
c_texts6 = [sub("  ", " ", i) for i in c_texts5]
c_texts6 = [' '.join(i.split()) for i in c_texts5]
print(c_texts6)
