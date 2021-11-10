'''
디스플레이 필터
nCr 조합을 선택하는 조건, 이진트리 형태로 풀수있다. 간단하게 코드구현 가능.
'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info_filter = [list(map(int, readl().split())) for _ in range(N)]
    return N, info_filter

sol = -1
# 입력받는 부분
N, info_filter = input_data()

g_sol_diff = 9999999999
g_sol_cnt = 0

def dfs(n, plus, multiple, cnt):

    global g_sol_diff, g_sol_cnt
    
    # 종료조건
    if n == N:
        if cnt > 0:
           # 비교한 값이 작을경우와 값이 같은경우에는 카운트값이 작은경우에 업데이트
           if g_sol_diff > abs(plus - multiple) or \
              (g_sol_diff == abs(plus - multiple) and cnt < g_sol_cnt):
              g_sol_diff = abs(plus - multiple)
              g_sol_cnt = cnt
        return  

    # 업데이트 조건
    n_plus = plus + info_filter[n][1]
    n_multiple = multiple * info_filter[n][0]

    # 선택한 방향
    dfs(n+1, n_plus, n_multiple, cnt+1)

    # 선택안한 방향
    dfs(n+1, plus, multiple, cnt)        

# 여기서부터 작성
def solve():

    # nCr을 구하는데 중복불가 - binary tree 형태로 재귀
    dfs(0, 0, 1, 0)
    return g_sol_cnt
    
sol = N - solve()

# 출력하는 부분
print(sol)