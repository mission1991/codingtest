'''
버전은 다음처럼 "." 으로 구분된 문자열이다.
두 개의 버전을 부등호로 비교할 수 있는 프로그램을 작성하시오.

예시
0.0.2 > 0.0.1
1.2.99 > 1.3.0
1.1 = 1.1
2.0 < 2.1
'''

CASES = [['0.0.2', '0.0.1'],
         ['1.2.99', '1.3.0'],
         ['1.1', '1.1'],
         ['2.0', '2.1']]

from itertools import zip_longest


def compare(left, right):
    left_vars = map(int, left.split('.'))
    right_vars = map(int, right.split('.'))
    for a, b in zip_longest(left_vars, right_vars, fillvalue = 0):
        if a > b:
            return '>'
        elif a < b:
            return '<'
    return '='


for i in CASES:
    print(i[0], compare(*i), i[1])
