'''
장기자랑 - 원형큐 사용
'''

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
from typing import Deque


def input_data():
    readl = sys.stdin.readline
    N, S, M = map(int, readl().split())
    return N, S, M

sol_list = []

# 입력받는 부분
N, S, M = input_data()

# 여기서부터 작성

def solve():
    # print(N, S, M)

    from collections import deque
    queue = deque(list(range(S, N+1)) + list(range(1, S)))
    # print(queue)

    for _ in range(N):
        for _ in range(M-1):
            queue.append(queue.popleft())
        sol_list.append(queue.popleft())
    return sol_list

sol_list = solve()

# 출력하는 부분
print(*sol_list)