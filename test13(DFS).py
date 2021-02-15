''' Depth First Search
N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
이때 얼음 틀의 모양으로 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
0이 붙어있으면 하나의 아이스크림
예시 4 * 5 얼음 틀에서 아이스크림이 총 3개 생성됩니다.
00110
00011
11111
00000
'''
# 보류


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 9

dfs(graph, 1, visited)