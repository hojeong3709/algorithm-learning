'''
stack linked list
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    A = [list(map(int, readl().split())) for _ in range(N)]
    return N, A

def Solve():
    global A, S
    for element in A:
        # N == 0, Stack Pop
        if element[0] == 0:
            if S:
                print(S.pop())
            else:
                print("E")
        
        # N == 1, Stack Push
        if element[0] == 1:
            S.append(element[1])
     

        # N == 2, Number of Data in Stack
        if element[0] == 2:
            print(len(S));
    

N, A = Input_Data()
S = list()

Solve();