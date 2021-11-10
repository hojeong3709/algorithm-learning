'''
BFS
기출 - 자율 주행 알고리즘 개발 템플릿
'''
import sys
from collections import deque
def input_data():
    readl = sys.stdin.readline
    R,  C = map(int,  readl().split())
    map_park = [['X']+list(readl()[:-1])+['X'] if 1<=r<=R else ['X']*(C+2) for r in range(R+2)]
    return R,  C,  map_park
sol = -1
# 입력받는 부분
R,  C,  map_park = input_data()
# 여기서부터 입력

# print(R)
# print(C)
# for _ in map_park:
#     print(_)

def solve():

    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    q = deque()
    chk = [[0] * (C+2) for _ in range(R+2)]
    # for _ in chk:
    #     print(_)

    sr = 1
    sc = 1
    er = R
    ec = C
    start = (sr, sc, 0)

    q.append(start)
    chk[sr][sc] = 1

    while len(q):
        sr, sc, d = q.popleft()
        if sr == er and sc == ec:
            return d

        for dr, dc in move:
            nr = sr + dr
            nc = sc + dc

            if not(1 <= nr <= R):
                continue

            if not(1 <= nc <= C):
                continue

            if chk[nr][nc] == 1:
                continue

            if map_park[nr][nc] == 'X':
                continue

            update = (nr, nc, d+1)
            q.append(update)
            chk[nr][nc] = 1
            # print(q)
            # for _ in chk:
            #     print(_)       

    return -1      

sol = solve()

# 출력하는 부분
print(sol)