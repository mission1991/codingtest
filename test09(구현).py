''' 완전탐색
8 X 8 체스판에 나이트는 L자로 움직인다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
여기서 행은 1 - 8로 표시, 열은 a - h로 표시한다.
나이트의 위치를 입력받고, 이동할 수 있는 경우의 수를 출력하시오.
'''

input_data = input()  # 현재 나이트 위치 입력
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지의 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)