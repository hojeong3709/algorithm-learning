'''
건물세우기
(주)정올에서는 여러 개의 빌딩을 새로 지을 계획이다. 그래서 빌딩을 세울 장소를 선정하였다. 
그리고 각 빌딩을 각 장소에 세울 경우에 드는 비용을 추정하였다. 
예를 들어서 아래의 표를 보자
 
             1 2 3
           A 4 7 3
           B 2 6 1
           C 3 9 4
 
A, B, C 는 건물을 나타내고, 1, 2, 3은 장소를 나타낸다. 예를 들어서 건물 B를 장소 1에 세우면 비용이 2가 들고, 장소 2에 세우면 비용이 6, 장소 3에 세우면 비용이 1만큼 든다. 물론 한 장소에는 한 건물밖에 세울 수 없다. 만일 A를 장소 2에, B를 장소 3에, C를 1에 세우면 전체 비용이 7+1+3 = 11이 필요하다. 그런데 A를 3, B를 1, C를 2에 세우면 3+2+9 = 14 가 필요하다.
 
각 빌딩을 어느 장소에 세우면 비용의 합이 최소가 되는지 구하는 프로그램을 작성하시오.
'''

import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    cost = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
    return N, cost


# 입력받는 부분
N, cost = input_data()

# 여기서부터 작성
# print(N)
# for _ in cost:
#     print(_)

g_cost = 999999999
g_visit = [0] * (N+1)
sol_list = [0] * (N+1)
cur_list = [0] * (N+1)

def dfs(n, c):

    global g_cost, g_visit, sol_list

    if n > N:
        if g_cost > c:
            g_cost = c
            sol_list = cur_list.copy()
        return

    if c >= g_cost:
        return

    for i in range(1, N+1):
        if g_visit[i] == 1:
            continue
        g_visit[i] = 1
        cur_list[n] = i
        dfs(n+1, c + int(cost[n][i]))    
        g_visit[i] = 0
        
    # return -1

def solve():
    # dfs(depth, cost)
    dfs(1, 0)
    print(g_cost)
    # print(g_sel)
    print(*sol_list[1:])

solve()

