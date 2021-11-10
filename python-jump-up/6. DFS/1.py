'''
주사위 던지기

주사위를 던진 횟수 N과 출력형식 M을 입력 받아서 M의 값에 따라 각각 아래와 같이 출력하는 프로그램을 작성하시오.
M = 1 : 주사위를 N번 던져서 나올 수 있는 모든 경우
M = 2 : 주사위를 N번 던져서 중복이 되는 경우를 제외하고 나올 수 있는 모든 경우
M = 3 : 주사위를 N번 던져서 모두 다른 수가 나올 수 있는 모든 경우
* 중복의 예
1 1 2 와 중복 : 1 2 1, 2 1 1
1 2 3 과 중복 : 1 3 2, 2 1 3, 2 3 1, 3 1 2
'''
import sys

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int,readl().split())
    return N, M

# 입력받는 부분
N, M = Input_Data()

# depth
ans = [0] * (N+1)
# dice 1 ~ 6
sel = [0] * 7

# 여기서부터 작성
def dfs1(depth):
    global ans
    if depth > N:
        print(*ans[1:N+1])
        return

    for i in range(1, 7):
        ans[depth] = i
        dfs1(depth + 1)

    return -1

def dfs2(depth, status):
    
    global ans
    if depth > N:
        print(*ans[1:N+1])
        return

    for i in range(status, 7):
        ans[depth] = i
        dfs2(depth+1, i)


def dfs3(depth):

    global ans
    global sel
    if depth > N:
        print(*ans[1:N+1])
        return

    for i in range(1, 7):
        if sel[i] == 1:
            continue
        ans[depth] = i
        sel[i] = 1
        dfs3(depth+1)
        sel[i] = 0
           

if M == 1:
    dfs1(1)
if M == 2:
    dfs2(1, 1)
# 순열, 순서중요
if M == 3:
    dfs3(1)