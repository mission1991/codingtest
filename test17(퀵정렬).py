'''
기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
첫 번째 데이터를 기준 데이터로 Pivot 설정합니다.
'''

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # 기준!
    tail = arr[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    # 왼쪽, 오른쪽 분할 후 각각 재귀적으로 빠르게 수행
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(arr))



