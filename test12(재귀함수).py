''' 팩토리얼 '''

#  반복적으로 구현한 팩토리얼
def fac_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


#  재귀적으로 구현한 팩토리얼
def fac_recursive(n):
    if n <= 1:
        return 1
    return n * fac_recursive(n - 1)


print(fac_iterative(5))
print(fac_recursive(5))

''' 유클리드 호제법 (최대공약수) '''

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))