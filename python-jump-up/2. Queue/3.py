'''
프린터 큐

입력
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

출력
1
2
5
'''

import sys
from collections import deque

def input_data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job

def solve(N, M, job):
    q = deque()
    cnt = [0] * 10

    for idx, priority in enumerate(job):
        q.append((idx, priority))
        cnt[priority] += 1

    sol = 0
    for i in range(9, 0, -1):
        for _ in range(cnt[i]):
            while True:
                idx, priority = q.popleft()
                if priority == i:
                    break
                q.append((idx, priority))
            sol += 1
            if idx == M:
                return sol
    return -1

T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    #입력받는 부분    
    N, M, job = input_data()
    # 여기서부터 작성
    ret = solve(N, M, job)
    print(ret)