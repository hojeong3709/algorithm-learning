'''
최소비용으로 포장 다시하기
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	candy = list(map(int,readl().split()))
	return N, candy


sol = -1
# 입력받는 부분
N, candy = Input_Data()

# 여기서부터 작성
def solve():

    total = 0
    # print(N, candy)
    for _ in range(N-1):
        candy.sort()
        if len(candy) > 2:
            cost = candy.pop(0) + candy.pop(0)
            total += cost
            candy.append(cost)
        else:
            total += sum(candy)        

    return total

sol = solve()

# 출력하는 부분
print(sol)