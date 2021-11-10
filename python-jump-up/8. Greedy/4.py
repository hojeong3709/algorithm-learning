'''
농장탈출

소들은 농부 존의 농장을 탈출하는 대담한 계획을 세웠다. 
그들은 작은 고무 보트를 구했고 한 밤중에 농장 경계에 흐르는 강을 보트를 타고 건너려는 계획이다. 
그 계획은 완벽해 보였다. 
작은 고무 보트가 소들의 무게를 견디지 못한다는 사실을 알기 전까지는…
N마리의 소(1≤N≤20)들의 무게는 각각 W_1, …, W_N이다. 보트가 침몰하지 않을 만큼 가벼운 소들을 선별해야 한다. 
불행하게도, 소들은 산수를 못하기로 유명하다.
10진법을 사용하는 소들은 소들의 무게를 더하다가 자리올림이 발생하는 경우 그 소는 보트를 사용하기에는 너무 무거운 소라고 판단한다. 
자리올림이 발생하지 않고 더할 수 있는 무게가 보트를 사용할 수 있는 가벼운 무게이다.
 당신이 할 일은 소들을 도와서 보트를 탈 수 있는 소들의 최대 수를 구하는 것이다. 
 즉, 소들의 무게들을 모두 더했을 때 자리올림이 발생하지 않게 하는 소들의 최대 수를 구하는 것이다.

입력
5
522
6
84
7311
19

출력
3

522 + 6 + 7311 = 7839, 세 마리 소의 무게를 더할 때 어떤 자리에서도 자리올림이 발생하지 않는다.
    522
      6
+ 7311
---------
  7839
'''
import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight

sol = -1
# 입력받는 부분
N, weight = input_data()

# 여기서부터 작성

# 출력하는 부분
print(sol)

'''
정답
import sys
  
  
def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight
  
  
def Check_Carry(A,B):
    while A and B:
        if A%10 + B%10 >= 10: return True
        A //= 10
        B //= 10
    return False
  
def DFS(s,sum_weight, cnt) : # 어떤소를 배에 태울것인가?
    global sol
    if cnt + (N-s) <= sol:
        return
  
    if sol < cnt:
        sol = cnt
  
    for n in range(s,N):
        # n번소를 태우는 시도!
        if not Check_Carry(sum_weight, weight[n]):
            DFS(n+1, sum_weight+weight[n], cnt+1)
  
"""
def DFS(n,sum_weight,cnt): # n 소 -> 태울것인가? (자리올림이 발생하지 않을때!) 말것인가? (언제든지!)
    global sol
    if cnt + (N-n) <= sol:
        return
  
    if n>=N:
        if sol < cnt:
            sol = cnt
        return
  
    # 태우기!
    if not Check_Carry(sum_weight, weight[n]): 
        DFS(n+1, sum_weight + weight[n], cnt+1)
  
    # 안태우기!
    DFS(n+1, sum_weight, cnt)
"""
  
sol = -1
# 입력받는 부분
N, weight = input_data()
  
# 여기서부터 작성
# DFS(n,sum_weight,cnt)
DFS(0, 0, 0)
  
# 출력하는 부분
print(sol)
'''