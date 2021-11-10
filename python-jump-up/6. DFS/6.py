'''
벽장문의 이동

n개의 같은 크기의 벽장들이 일렬로 붙어져 있고 벽장의 문은 n-2개만이 있다. 
한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면) 그 벽장 앞으로 움직일 수 있다.
 
그림은 7개의 벽장의 예이다. 그림에서 2번 벽장과 5번 벽장이 열려있고, 나머지 벽장은 닫혀 있다. 
벽장 문은 좌우 어느 쪽이든 그 이웃 벽장이 열려 있다면 그 쪽으로 한 칸씩 이동할 수 있다. 
그림에서 주어진 상태에서는 1번 벽장을 닫고 있는 벽장문을 오른쪽으로 한 칸 이동함으로써 1번 벽장을 사용할 수 있다. 
이때 2번 벽장은 닫혀져 사용할 수 없다. 역시 5번 벽장이 열려 있으므로 4번 벽장 또는 6번 벽장 앞의 벽장문을 5번 벽장 앞으로 이동시킬 수 있다.
 
풀어야 할 문제는 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서를 찾는 것이다. 
이때 벽장문의 이동횟수를 최소로 하여야 한다. 입력은 다음과 같이 주어지며, 열려있는 벽장의 개수는 항상 2개이다.
 
예를 들어 사용할 벽장 순서가 3 1 6 5이면, 3번 앞의 문을 2번으로 옮겨서 3번 벽장을 사용하고(문 이동회수=1), 
다음에 1번과 2번 앞에 있는 문을 오른쪽으로 하나씩 옮겨서(문 이동회수=2) 1번 벽장을 사용하며, 
6번 앞에 있는 문을 왼쪽으로 옮겨서 6번 벽장을 사용하고(문 이동회수=1), 다시 그 문을 오른쪽으로 옮겨서 5번 벽장을 사용한다(문 이동회수=1), 
따라서 문이 이동한 회수의 합은 5이다.

또한 같은 벽장을 여러 번 사용할 수도 있다.

입력
7
2 5
4
3
1
6
5

출력
5
'''
import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq


sol = -1

#입력받는 부분
N, A, B, S, seq = input_data()

# 여기서부터 작성
# print("-"*10)
# print(N, A, B, S)
# print(seq)

# N : 벽장길이
# A : 벽장A
# B : 벽장B
# S : 사용할 벽장개수

# N = 7
# A = 2
# B = 5
# S = 4
# seq = [3, 1, 6, 5]

g_td = 999999999

def dfs(n, a_pos, b_pos, td):
    
    global g_td

    # N회이상 움직일경우 탐색종료
    if n >= S:
        if td < g_td:
            g_td = td  
        return
    
    # 최소값이상이므로 탐색중지
    if td >= g_td:
        return

    # 벽장A를 움직일 경우
    dfs(n+1, seq[n], b_pos, td + abs(a_pos - seq[n]))
    
    # 벽장B를 움직일 경우
    dfs(n+1, a_pos, seq[n], td + abs(b_pos - seq[n]))   


def solve():

    # dfs(N회, 벽장A상태(위치), 벽장B상태(위치), 총이동거리합)
    dfs(0, A, B, 0)
    sol = g_td
    return sol
    
sol = solve()


# 출력하는 부분
print(sol)

'''
import sys
 
 
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    A, B = map(int, readl().split())
    S = int(readl())
    seq = [int(readl()) for _ in range(S)]
    return N, A, B, S, seq
 
 
def solve(n, o1, o2, cnt_move):
    global sol
    if n >= S:
        sol = cnt_move
        return
 
# DFS 방식 중 진입전에 확인하고 조건에 맞으면 진입

    if sol > cnt_move + abs(o1-seq[n]):
        solve(n+1, seq[n], o2, cnt_move + abs(o1-seq[n]))
     
    if sol > cnt_move + abs(o2-seq[n]):
        solve(n+1, o1, seq[n], cnt_move + abs(o2-seq[n]))
 
 
sol = -1
 
#입력받는 부분
N, A, B, S, seq = input_data()
 
# 여기서부터 작성
sol = 100000000
solve(0, A, B, 0)
 
# 출력하는 부분
print(sol)

'''