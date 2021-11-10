'''
미술관람대회

해마다 열리는 꿀꿀이 올림피아드에는 여러 종목들이 있는데, 요즘에는 꿀꿀이들의 교양을 겨루는 ‘미술관람 대회’가 인기를 끌고 있다. 
이 대회는 사회자가 빨강, 초록, 파랑으로 이루어진 N × N 픽셀의 그림을 보여주면 그 그림에 포함된 영역의 수를 빠르고 정확하게 맞추는 것이 목표이다. 
동일한 색깔이 네 방향(상, 하, 좌, 우) 중 한 곳이라도 연결되어 있으면 하나의 영역으로 간주한다.
 
예를 들어, 아래 그림은 각각 2, 1, 1개의 빨간색, 초록색, 파란색 영역이 있어 총 4개의 영역이 있다.

한편, 꿀꿀이들의 절반 정도는 선천적인 유전자 때문에 적록색맹이라서 빨간색과 초록색을 구별하지 못한다.
따라서 사회자는 일반 대회와 적록색맹용 대회를 따로 만들어서 대회를 진행하려고 한다. 사회자를 도와 영역의 수를 구하는 프로그램을 작성하여라.

입력
첫 번째 줄에는 그림의 크기 N이 주어진다. (1 ≤ N ≤ 100)
두 번째 줄부터 N개의 줄에는 각 픽셀의 색깔이 'R'(빨강), 'G'(초록), 'B'(파랑) 중 하나로 주어진다.

5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

출력
일반 꿀꿀이와 적록색맹 꿀꿀이가 보는 영역의 수를 출력한다.
4 3

'''

import sys
from collections import deque
sys.setrecursionlimit(10000)

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_nor_pig


sol_nor_pig, sol_rg_pig = -1, -1
# 입력받는 부분
N, map_nor_pig = input_data()

# 여기서부터 작성
chk = [[0] * (N+2) for _ in range(N+2)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
g_cnt = 0

def fill(r, c, nmap):

    global g_cnt

    # 범위밖
    if nmap[r][c] == 0:
        return
    
    # 이미 방문한곳 ==> map update
    if chk[r][c] == 1:
        return
    
    chk[r][c] = 1

    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        if nmap[r][c] == nmap[nr][nc]:
            fill(nr, nc, nmap)
            g_cnt += 1
            
def solve(nmap):

    for r in (1, N+1):
        for c in (1, N+1):
            fill(r, c, nmap)
    return g_cnt

# 출력하는 부분
map_rg_pig = [[ 'R' if map_nor_pig[r][c] == 'G' else map_nor_pig[r][c] for c in range(N+2)] for r in range(N+2)]

sol_nor_pig = solve(map_nor_pig)
sol_rg_pig = solve(map_rg_pig)


# print(N)
# for _ in map_nor_pig:
#     print(_)

print(sol_nor_pig, sol_rg_pig)



# 솔루션

# import sys
# from collections import deque
  
# sys.setrecursionlimit(10000)
# def input_data():
#     readl = sys.stdin.readline
#     N = int(readl())
#     map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
#     return N, map_nor_pig
  
# def Flood_Fill(sr,sc,map_art):
#     q = deque()
#     q.append((sr,sc,map_art[sr][sc]))
#     map_art[sr][sc] = 0
#     while len(q)>0:
#         r,c,color = q.popleft()
#         for dr, dc in d:
#             nr, nc = r+dr, c +dc
#             if map_art[nr][nc] == color:
#                 q.append((nr,nc,map_art[nr][nc]))
#                 map_art[nr][nc] = 0
 
# def Fill(r,c,map_art):
     
#     color = map_art[r][c]
#     map_art[r][c] = 0
#     for dr, dc in d:
#         nr, nc = r+dr, c +dc
#         if map_art[nr][nc] == color:          
#             Fill(nr,nc,map_art)
  
# def Solve(map_art):
#     cnt_area = 0
#     for r in range(1,N+1):
#         for c in range(1,N+1):
#             print(r, c)
#             if map_art[r][c] != 0:
#                 # Flood_Fill(r,c,map_art)
#                 Fill(r,c,map_art)
#                 cnt_area += 1
#     return cnt_area
  
# sol_nor_pig, sol_rg_pig = -1, -1
# # 입력받는 부분
# N, map_nor_pig = input_data()
  
# # 여기서부터 작성
# d = [(1,0), (-1,0), (0,1),(0,-1)]
# map_rg_pig = [[ 'R' if map_nor_pig[r][c] == 'G' else map_nor_pig[r][c] for c in range(N+2)] for r in range(N+2)]
# sol_nor_pig , sol_rg_pig = Solve(map_nor_pig), Solve(map_rg_pig)
  
# print(sol_nor_pig, sol_rg_pig)

