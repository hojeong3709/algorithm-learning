'''
기출 - 도로건설
그래프 2차원
'''

import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_cost = [[0] + list(map(int, readl()[:-1])) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_cost


sol = -2
# 입력받는 부분
N, map_cost = input_data()

# 여기서부터 작성
# print(N)
# for _ in map_cost:
#     print(_)

def solve():
    
    q = deque()
    visit = [[0] + ([987654321] * N) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    # path = [0] * (N+1)
    
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    sr = 1
    sc = 1
    er = N
    ec = N

    start = (sr, sc)
    q.append(start)
    visit[sr][sc] = 0
    
    while len(q):
        sr, sc = q.popleft()

        # if sr == er and sc == ec:
        #     return

        for dr, dc in move:
            nr = sr + dr
            nc = sc + dc
            # 새로갈곳의 비용 = 현재까지 누적치 + 새로운곳 비용
            nvalue = visit[sr][sc] + map_cost[nr][nc]
            
            # 범위안에 있는지 확인
            if not (1 <= nr <= N):
                continue
            if not (1 <= nc <= N):
                continue

            if visit[nr][nc] <= nvalue:
                continue

            visit[nr][nc] = nvalue
            update = (nr, nc)
            q.append(update)

        # for _ in visit:
        #     print(_)
        # print("\n")

    return visit[N][N]

sol = solve()


# 출력하는 부분
print(sol)