'''
이진 탐색
'''


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n개의 원소 설정 / target 찾을 값 설정
n, target = list(map(int, input().split()))
# n개 만큼 list 설정
array = list(map(int, input().split()))
array.sort()
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)

'''
bisect
데이터 개수 구하기
'''
# 파이썬 내장 라이브러리 사용
from bisect import bisect_left, bisect_right


def count_search(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_search(a, 4, 4))  # 값이 4인 개수 데이터 출력
print(count_search(a, -1, 3))  #값이 [-1, 3] 범위에 있는 데이터 개수 출력
