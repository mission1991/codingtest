'''
1차원의 점들이 주어졌을 때, 그 중 가장 거리가 짧은 것의 쌍을 출력하는 함수를 작성하시오.
(단 점들의 배열은 모두 정렬되어있다고 가정한다.)

Ex => S = [1, 3, 4, 8, 13, 17, 20]
Ans => (3, 4)가 될 것이다.
'''


def spair(S):
    dict = {}
    for x, y in zip(S[:-1], S[1:]):
        print(x, y)
        if not dict.get(y-x):
            dict[y-x] = [(x, y)]
        else:
            dict[y-x] = dict[y-x] + [(x, y)]
    print(dict)
    return dict[min(dict.keys())]




S = [1, 3, 4, 8, 13, 17, 20, 21]
print(spair(S))