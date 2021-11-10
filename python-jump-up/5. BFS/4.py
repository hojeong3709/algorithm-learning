'''
BFS
9/1 
좀더 생각해보고 코드 수정필요

SLIKAR
사악한 황제 KAKTUS는 그의 마법 술통을 이용해 마법의 숲에 홍수가 생기도록 만들었다.
화가는 홍수로부터 안전한 비버의 굴로 도망가려고 한다.
마법의 숲 지도는 R행과 C열로 구성되어있다.
비어있는 곳은 '.', 홍수지역은 '*', 바위지역은 'X', 비버의 굴은 'D', 그리고 화가의 위치는 'S'로 표현된다.
매 분마다 화가는 그와 인접한 4개의 지역(상하좌우 위치)로 이동이 가능하다. 홍수지역 또한 매 분마다 그와 인접한 4개지역으로 뻗어나간다.
화가는 바위가 있는 구역과 홍수지역으로 이동하지 못하며, 홍수지역은 바위나 비버의 굴 위치로는 뻗어나갈 수 없다.
 
마법의 숲 지도가 주어졌을 때, 화가가 비버의 굴로 도망칠 수 있는 가장 짧은 시간은 구하여 출력하라.
 
참고 : 화가는 홍수지역과 홍수가 먼저 확산된 곳, 그리고 화가가 도착할 시간에 홍수도 확산할 칸으로 이동할 수 없다.


첫째 줄에 테스트 케이스의 갯수 T가 주어진다.
둘째 줄부터 T개의 테스트케이스 세트가 주어진다.
테스트 케이스의 첫째 줄에는 지도의 사이즈인 R,C 가 주어진다. (1<=R,C<=50)
테스트 케이스의 둘째 줄부터 R개의 줄에 마법의 숲 지도가 주어진다.
('D','S'는 하나씩만 주어진다, 지도에는 문제에서 설명한 문자만 주어진다. )

입력
1
10 11
D..........
...........
...........
...........
...........
...........
........S..
...........
...........
...........

출력
14

'''

import sys
from collections import deque

def input_data():
    R, C = map(int,readl().split())
    map_forest = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
    return R,C,map_forest

readl = sys.stdin.readline
# T는 Test Case
# T = int(readl())
# for _ in range(T):
#     # 입력받는 부분
#     R, C, map_forest = input_data()
#     # 여기서부터 작성

def solve():
    
    # 입력받는 부분
    R, C, map_forest = input_data()

    # print(R, C)
    # for _ in map_forest:
    #     print(_)

    move_possible_route = deque()
    flood_position = deque()

    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    chk = [[0] * (C+2) for _ in range(R+2)]
    
    time = 0
    sr = 0
    sc = 0
    er = 0
    ec = 0
    for r_idx, row in enumerate(map_forest):
        for c_idx, col in enumerate(row):
            if col == '*':
                w = 0
                move_possible_route.append((w, sr, sc, time))
            elif col == 'S':
                w = 1
                sr = r_idx
                sc = c_idx
                chk[sr][sc] = 1
                move_possible_route.append((w, sr, sc, time))
            elif col == 'D':
                er = r_idx
                ec = c_idx
   
    # print(move_possible_route)
    # print(er, ec)
    # print(flood_position)

    while len(move_possible_route):
        w, sr, sc, t = move_possible_route.popleft()
        
        if w == 1:
            if sr == er and sc == ec:
                return t

            for dr, dc in move:
                nr = sr + dr
                nc = sc + dc

                # 외곽체크
                if not(1 <= nr <= C):
                    continue
                if not(1 <= nc <= R):
                    continue

                # 방문체크
                if chk[nr][nc] == 1:
                    continue

                # 장애물체크
                if map_forest[nr][nc] == 'X' or map_forest[nr][nc] == '*':
                    continue
                           
                route_update = (w, nr, nc, t+1)
                move_possible_route.append(route_update)
                chk[nr][nc] = 1

   
    # for _ in map_forest:
    #     print(_)

    return -1

T = int(readl())
for _ in range(T):
    sol = solve()
    # 출력
    print(sol)