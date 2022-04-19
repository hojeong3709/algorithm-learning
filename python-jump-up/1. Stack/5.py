'''
건물옥상정원
N 확인 후 순방향, 역방향 탐색시 시간오버
역발상 필요, i 번째 건물이 볼 수 있는 건물 -> i 번째 건물을 볼 수 있는 건물
-> stack 사용
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_h = [int(readl()) for _ in range(N)]
    return N, list_h

N, building_heights = Input_Data()

# print(N)
# print(building_heights)

def solve():
    
    stack = []
    sum = 0
        
    for current_building_height in building_heights:
        # print("current_building_height : {}".format(current_building_height))
        # print(stack)
        while stack and stack[-1] <= current_building_height:
            stack.pop()
            # print(stack)        
        sum += len(stack)
        # print(sum)
        stack.append(current_building_height)

    return sum

sol = solve()
print(sol)