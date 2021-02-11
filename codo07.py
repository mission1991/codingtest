'''
사용자로부터 1~9 사이의 정수를 입력 받는다.
입력받은 정수의 수 만큼 O와 X로 표시된다.
row가 넘어갈 수록 O가 X로 바뀌어 출력된다.

입력 예시: 6
출력 예시:
OOOOOO
OOOOOX
OOOOXX
OOOXXX
OOXXXX
OXXXXX
XXXXXX
'''

n = int(input("1~9 사이의 정수를 입력해주세요. : "))

for i in range(n + 1):
    print(('O' * (n - i)) + ('X' * i))

