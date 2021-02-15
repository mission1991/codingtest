''' 문자 재정렬
알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 청렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.
예시 -> K1KA5CB7
답변 -> ABCKK13
'''

data = input()

a = []
b = 0

for i in data:
    if i.isdigit():
        b += int(i)
    else:
        a.append(i)

a.sort()
#  숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if b != 0:
    a.append(str(b))

print(''.join(a))
