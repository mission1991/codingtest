'''
문자열을 입력받아서, 같은 문자가 연속적으로 반복되는 경우에 그 반복 횟수를 표시하여 문자열을 압축하기.

입력 -> aaabbcccccca
출력 -> a3b2c6a1
'''
# dictionary 사용
a = input()
b = {}

for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1
print(b)