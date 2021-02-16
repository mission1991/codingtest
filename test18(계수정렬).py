'''
특별한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작한다.
데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능하다.
 0 ~ 9까지의 원소들 중 각 원소가 몇 번씩 나왔는가
'''

arr = [3, 1, 6, 5, 3, 7, 8, 1, 2, 3, 4, 9, 0, 8, 7, 0]

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1
print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')