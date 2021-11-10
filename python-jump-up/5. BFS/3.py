'''
BFS
토마토
'''

import sys
from collections import deque
from typing import Mapping

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int,readl().split())
    map_box = [[0]*(C+2) if (r==0 or r==R+1) else [0]+list(map(int,readl().split()))+[0] for r in range(R+2)]
    return C,R,map_box

sol = -2

# 입력받는 부분
C,R,map_box = Input_Data()

# 작성하는 부분

# print(C)
# print(R)
# for _ in map_box:
#     print(_)

def solve():

    ripe_tomatos = deque()
    for r, r_box in enumerate(map_box):
        for c, tomato in enumerate(r_box):
            if tomato == 1:
                ripe_tomatos.append((r, c, 0))

    # print(ripe_tomatos)
    visit = [[0] * (C+2) for _ in range(R+2)]
    # for _ in visit:
    #     print(_)

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    time = 0

    while len(ripe_tomatos):
        sr, sc, t = ripe_tomatos.popleft()
        visit[sr][sc] = 1
        time = t

        # if sr == er and sc == ec:
        #     return t

        for dr, dc in move:
            nr = sr + dr
            nc = sc + dc

            if not(1 <= nr <= R):
                continue
            if not(1 <= nc <= C):
                continue

            if visit[nr][nc] == 1:
                continue

            if map_box[nr][nc] == -1:
                continue

            update = (nr, nc, t+1)
            ripe_tomatos.append(update)
            visit[nr][nc] = 1

        # print(ripe_tomatos)

    return time


sol = solve()

# 출력하는 부분
print(sol)