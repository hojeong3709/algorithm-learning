'''
더하기
덧셈을 못하는 철수를 공부시키기 위해 자연수들을 주고, 그 중에 몇 개의 수를 골라서 그 합이 K가 될 수 있는지 알아보라고 시켰다. 
철수 어머니가 자연수들을 무작위로 선택해서 본인도 가능한지 아닌지 모르고 있다. 어머니가 채점을 할 수 있게 주어진 문제의 답을 찾아주자.

첫 번째 줄에 테스트 케이스 개수 T(1≤T≤10)가 주어진다.
두 번째 줄부터 아래 내용이 T개 만큼 주어진다.
첫 줄에 자연수 개수 N(5 <= N <= 20)과 K(1 <= K <= 2,000,000)가 공백으로 구분되어 입력된다.
다음 줄에 N개의 자연수 di(1 <= di <= 100,000)가 공백으로 구분되어 입력된다.

2
5 19
1 2 4 7 10
5 25
1 2 4 7 10

'''

import sys

T = int(input())

print(T)

def dfs(n, s):
    
    # 구하고자 하는값인 K와 누적합 s와 값이 같은 경우
    if s == K:
        return True

    # 깊이가 N이상인 경우, 즉 선택이 N개 이상인 경우 탐색 불필요
    if n >= N:
        return False

    # 구하고자 하는값인 K보다 누적합 s가 큰경우, 더이상 탐색 불필요
    if s > K:
        return False

    # 선택
    if dfs(n+1, s + d[n]):
        return True

    # 미선택
    if dfs(n+1, s):
        return True

def dfs1(n, s):

    # 구하고자 하는값인 K와 누적합 s와 값이 같은 경우
    if s == K:
        return True

    # 깊이가 N이상인 경우, 즉 선택이 N개 이상인 경우 탐색 불필요
    if n >= N:
        return False

    # 구하고자 하는값인 K보다 누적합 s가 큰경우, 더이상 탐색 불필요
    if s > K:
        return False

    for i in range(n, N):
        if dfs1(i+1, s + d[i]):
            return True

    return False


for i in range(T) :
    N, K = map(int, input().split())
    d = list(map(int, input().split()))

    # print(N)
    # print(K)
    # print(d)

    # 여기서부터 작성
    sol = dfs1(1, 0)
    if sol:
        print("Yes")
    else:
        print("No")

'''
T = int(input())
 
def dfs(n, s): #n: 선택할 index, s:선택한 수 의 합계
    if s>K: return False
    if s == K: return True
    if n >= N: return False
 
    #선택
    if dfs(n+1, s+d[n]): return True
    #선택 안함
    if dfs(n+1, s): return True
    return False
 
def dfs1(n, s):
    if s>K: return False
    if s == K: return True
    if n >= N: return False
 
    for i in range(n, N):
        if dfs1(i+1, s+d[i]): return True
 
    return False
 
def solve():
    ans = dfs1(0,0)
    return ans
 
for i in range(T) :
    N, K = map(int, input().split())
    d = list(map(int, input().split()))
 
    sol = solve()
    if sol: print('YES')
    else: print('NO')
'''