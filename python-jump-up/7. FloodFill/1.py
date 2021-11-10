'''
FloodFill
단지 번호 붙이기

<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집들의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 
대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

입력
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

출력
3
7
8
9
'''
import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_apt = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
    return N, map_apt


# 입력받는 부분
N, map_apt = Input_Data()

chk = [[0]*(N+2) for r in range(N+2)]
move =[(1, 0), (-1, 0), (0, -1), (0, 1)]
sol_list = []
# 여기서부터 작성

# print(N)
# for _ in map_apt:
#     print(_)

def fill(r, c):
    if map_apt[r][c] == 0:
        return
    # map을 한번만 쓰기때문에 chk 배열없이 map에 업데이트 하면서 계산가능
    map_apt[r][c] = 0
    sol_list[-1] += 1
    for dr, dc in move:
        nr = r + dr
        nc = c + dc
        fill(nr, nc)

def solve():

    for r in range(N+1):
        for c in range(N+1):
            if map_apt[r][c] == 1:
                sol_list.append(0)
                fill(r, c)
    return -1

# 출력하는 부분
solve()
# print(sol_list)
print(len(sol_list), *sorted(sol_list), sep='\n')