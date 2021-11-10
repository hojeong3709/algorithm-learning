'''
모범생 - 단순정렬응용
'''

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	score = map(int,readl().split())
	info = list(enumerate(score, 1))
	return N, info

# 입력받는 부분
N, info = Input_Data()

def solve():
    # print(N, info)
    
    info.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    sol = [id for id, _ in info]
    if len(sol) > 3:
        print(*sol[:3])
    else:
        print(*sol)
    

# 여기서부터 작성
sol = solve()

# 출력하는 부분
# print(*sol)