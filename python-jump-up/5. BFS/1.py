'''
BFS

미로탈출로봇
미로탈출 로봇 대회를 개최하였다. 대회에 사용되는 미로는 가로(X), 세로(Y) 100이하의 크기이며, 미로를 한 칸 이동하는 데는 1초가 걸린다.
로봇이 출발점에서 도착점까지 가장 빨리 이동할 경우 걸리는 시간을 구하는 프로그램을 작성하시오.

첫 줄에 미로의 크기 X, Y(1≤X, Y≤100)가 주어진다.
둘째 줄에 출발점 x, y 좌표와 도착점 x, y 좌표가 공백으로 구분하여 주어진다.
셋째 줄부터 미로의 정보가 길은 0, 벽은 1로 공백이 없이 들어온다.
주의 사항으로, 좌표는 좌측상단이 가장 작은 위치이며 이 위치의 좌표는 (1,1)이다.

8 7
1 2 7 5
11111111
00000111
10110011
10111001
10111101
10000001
11111111
'''

import sys
from collections import deque
from types import new_class

def Input_Data():
    readl = sys.stdin.readline
    C, R = map(int,readl().split())
    sc,sr,ec,er = map(int,readl().split())
    map_maze = [[1]*(C+2)if (r == 0 or r == R+1) else [1] +list(map(int,readl().strip()))+[1] for r in range(R+2)]
    return C,R,sc,sr,ec,er,map_maze

sol = -1
#입력받는 부분
C,R,sc,sr,ec,er,map_maze = Input_Data()

# print(C)
# print(R)
# print(sc)
# print(sr)
# print(ec)
# print(er)

# 여기서부터 작성
# BFS1
def solve():
    
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    chk = [[0] * (C+2) for r in range(R+2)]
    
    q = deque()
    q.append((sr, sc, 0))
    chk[sr][sc] = 1

    while len(q):
        current_r, current_c, current_d = q.popleft()
        if current_r == er and current_c == ec:
            return current_d
        for dr, dc in move:
            new_r = current_r + dr
            new_c = current_c + dc

            # 불가능한 조건 걸러내기
            # 1. list 외부
            if not(1 <= new_c <= R):
                continue
            if not(1 <= new_r <= C):
                continue

            # 2. 방문한곳
            if chk[new_r][new_c] == 1:
                continue

            # 3. 벽
            if map_maze[new_r][new_c] == 1:
                continue
            
            q.append((new_r, new_c, current_d + 1))
            chk[new_r][new_c] = 1
 
    return -1

# # BFS2
# def solve():
    
#     move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#     chk = [[0] * (C+2) for r in range(R+2)]
    
#     q = deque()
#     q.append((sr, sc, 0))

#     # check 배열 없애면? --> 지나온길을 벽으로 막는다.
#     # chk[sr][sc] = 1
#     map_maze[sr][sc] = 1

#     while len(q):
#         current_r, current_c, current_d = q.popleft()
#         if current_r == er and current_c == ec:
#             return current_d
#         for dr, dc in move:
#             new_r = current_r + dr
#             new_c = current_c + dc
#             # 불가능한 조건 걸러내기

#             # 1. list 외부 (생략)
#             # if not(1 <= new_c <= R):
#             #     continue
#             # if not(1 <= new_r <= C):
#             #     continue

#             # 2. 방문한곳(생략)
#             # if chk[new_r][new_c] == 1:
#             #     continue

#             # 3. 벽
#             if map_maze[new_r][new_c] == 1:
#                 continue
            
#             q.append((new_r, new_c, current_d + 1))
#             chk[new_r][new_c] = 1
 
#     return -1

sol = solve()

#출력하는 부분
print(sol)