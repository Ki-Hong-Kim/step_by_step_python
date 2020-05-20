# 텍스트 전처리
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
print(len(texts), type(texts))

from re import sub  # R에서 gsub 와 유사
# from package.module import class or function
# from module import class or function

# 1. 소문자 변경
for i in texts:
    print(i.lower())

texts_re = [i.lower() for i in texts]
print('texts_re1 : ', texts_re)

# 2. 숫자 제거
text_re2 = [sub('[0-9]', '', i) for i in texts_re]
print('text_re2 : ', text_re2)

# 3. 문장 부호 제거
punc_str = '[.,;:?!]'
text_re3 = [sub(punc_str, '', i) for i in text_re2]
print('text_re3 : ', text_re3)

# 4. 특수문자 제거
spec_str = '[@#$%^&*~()]'
text_re4 = [sub(spec_str, '', i) for i in text_re3]
print('text_re4 : ', text_re4)

# 5. 공백 제거 : 'abtta a' -> ''.join('abtta', 'a')
text_re5 = [sub(' ', '', i) for i in text_re4]
text_re5 = [''.join(i.split()) for i in text_re4]
print('text_re5 : ', text_re5)
