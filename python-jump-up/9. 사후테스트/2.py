'''
연결된 세포

당신은 M행, N열의 크기를 가진 행렬을 가지고 있고, 행렬은 1과 0의 세포로 이루어져 있다. 
여기서 수직이든 수평이든 대각선 방향이든 인접한 두 개의 세포를 연결되어 있다고 표현하는데, 세포가 1인 것들은 서로 연결되어 하나의 구역을 이룬다.
행렬에는 몇 개의 구역이 있는데, 행렬에서 크기가 가장 큰 구역을 이루는 세포 1의 개수는 얼마인가?

가장 첫 줄에는 행의 크기인 M(0<M<10)을 입력 받고, 두 번째 줄에는 열 크기인 N(0<N<10)을 입력 받는다. 
다음으로는 실제 행렬을 입력 받는데, 행렬은 숫자들로 이루어져 있다.

입력
4
4
1 1 0 0
0 1 1 0
0 0 1 0
1 0 0 0

출력
5

입력
5
4
0 0 1 1
0 0 1 0
0 1 1 0
0 1 0 0
1 1 0 0

출력
8

'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    M = int(readl())
    N = int(readl())
    map_cell = [list(map(int, readl().split())) for _ in range(M)]
    return M, N, map_cell


sol = -1
#입력 받는 부분
M, N, map_cell = Input_Data()

#여기서부터 작성
# print(M)
# print(N)
# for _ in map_cell:
#     print(_)

# 8가지 방향으로 확인
move = [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
visit = [[0] * (N) for _ in range(M)]
sol_list = []

def floodfill(r, c, v):
    
    global sol_list

    # 탐색범위확인
    if not(0 <= r <= M-1):
        return
    if not(0 <= c <= N-1):
        return

    # 탐색불가지역
    if map_cell[r][c] == 0:
        return

    # 이미방문
    if visit[r][c] >= 1:
        return

    # 장애물은 없음
    
    # 방문체크
    visit[r][c] = v
    sol_list[-1] += 1

    # 이동
    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        floodfill(nr, nc, v+1)
        
  

def solve():

    global sol_list

    for r in range(M):
        for c in range(N):
            if map_cell[r][c] == 1:
                sol_list.append(0)
                floodfill(r, c, 1)   

    return max(sol_list)

sol = solve()
#출력하는 부분
# print("="*10)
# for _ in visit:
#     print(_)

print(sol)