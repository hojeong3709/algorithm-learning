'''
BFS
그래프 1차원
지하철 - 재방문필요

입력
5 5
0 2 2 5 9
2 0 3 4 8
2 3 0 7 6
5 4 7 0 5
9 5 6 5 0

출력
8
1 3 5 
'''

import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    matrix = [[0] * (N+1) if n == 0 else [0]+list(map(int,readl().split())) for n in range(N+1)]
    return N, M, matrix


#입력받는 부분
N, M, matrix = Input_Data()

# print(N)
# print(M)
# for _ in matrix:
#     print(_)

path = [0] * (N+1)


def trace(m):
    if m == 0:
        return
    trace(path[m])
    print(m, end=' ')

def solve():
    global path
    q = deque()
    visit = [987654321] * (N+1)
    # init
    q.append(1)
    visit[1] = 0
    path[1] = 0

    while len(q):
        s = q.popleft()
        # 모든 연결점 탐색( matrix )
        for e in range(1, N+1):
            if matrix[s][e] == 0:
                continue
            # e까지가는 새로운 비용
            ntime = visit[s] + matrix[s][e]
            if visit[e] <= ntime:
                continue
            visit[e] = ntime
            path[e] = s
            q.append(e)
    return visit[M]

sol = solve()
print(sol)
trace(M)

# 출력
# 최소시간과 최단경로 출력