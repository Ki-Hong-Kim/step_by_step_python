"""
step02 문제
문1) message 에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용
  <출력결과>
[1, 0, 1, 0, 1]

문2) message 에서 'spam' 원소만 추출하여 spam_list 에 추가하시오.
      <조건> list + for + if 형식2) 적용

  <출력결과>
['spam', 'spam', 'spam']
"""

# 문1
message = ['spam', 'ham', 'spam', 'ham', 'spam']
# 내 답
dummy = []
for i in message:
    if i == 'spam':
        dummy.append(1)
    else:
        dummy.append(0)
print(dummy)
# 선생님 답
dummy = [1 if i == 'spam' else 0 for i in message]
print(dummy)

# 문2
spam_list = [m for m in message if m == "spam"]
print(spam_list)
