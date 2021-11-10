'''
건물옥상정원
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_h = [int(readl()) for _ in range(N)]
    return N, list_h

N, list_h = Input_Data()

print(N)
print(list_h)

def solve():
    
    stack = []
    sum = 0
    


    stack.append(list_h[0])
    for i in range(N):
        current_building_height = list_h[i]
        while stack and stack[-1] <= current_building_height:
            stack.pop()
        stack.append(current_building_height)
        
    # for h in list_h:
    #     while stack and stack[-1] <= h:
    #         stack.pop()
    #     sum += len(stack)
    #     stack.append(h)

        print(stack)

    return sum

sol = solve()

print(sol)