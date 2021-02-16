'''
N개의 원소로 구성된 A, B 두 배열을 입력 받는다. 배열의 원소는 모두 자연수입니다.
최대 K번 바꿔치기 연산을 수행하여 A, B의 원소를 바꾸어 A의 모든 원소 합이 최댓값이 나오도록 만들어라.
'''
# N => 몇 개의 원소
# K => 바꿀 수 있는 횟수

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # 작은 수 부터
b.sort(reverse=True)  # 큰 수 부터

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))