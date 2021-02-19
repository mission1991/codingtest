'''
메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
일반적으로 탑다운과 바텀업 방식이 있습니다.
'''
# 일반적인 재귀로 피보나치 수열을 풀기엔 시간 복잡도가 너무 크다.
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)



# 메모이제이션 활용 (탑다운)
d = [0] * 100  # 메모이제이션 하기 위해 리스트 초기화

def fivo(a):
    if a == 1 or a == 2:
        return 1
    if d[a] != 0:
        return d[a]
    d[a] = fivo(a - 1) + fivo(a - 2)
    return d[a]
print(fivo(99))

# 바텀업
d = [0] * 100  # 리스트 초기화
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])