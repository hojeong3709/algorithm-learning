'''
queue
'''

import sys
from collections import deque
 
 
def Input_Data():
  readl = sys.stdin.readline
  N = int(readl())
  list_cmd = [list(map(int,readl().split())) for _ in range(N)]
  return N, list_cmd
 
N, list_cmd = Input_Data()


def solve():
    # print(N)
    # print(list_cmd)

    queue = deque()

    for cmd in list_cmd:
        if cmd[0] == 0: #pop
            if queue:
                print(queue.pop())                
            else:
                print("E")
        elif cmd[0] == 1: #push
            queue.appendleft(cmd[1])
        elif cmd[0] == 2: #data
            print(len(queue))

solve()
