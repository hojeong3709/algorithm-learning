'''
이진탐색

예산
국가의 역할 중 하나는 여러 지방의 예산요청을 심사하여 국가의 예산을 분배하는 것이다. 국가예산의 총액은 미리 정해져 있어서 모든 예산요청을 배정해 주기는 어려울 수도 있다. 그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정한다.
 
(1) 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
(2) 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는 모두 상한액을 배정한다. 상한액 이하의 예산요청에 대해서는 요청한 금액을 그대로 배정한다.
 
예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150이라고 하자. 이 경우, 상한액을 127로 잡으면, 위의 요청들에 대해서 각각 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.
 
여러 지방의 예산요청과 국가예산의 총액이 주어졌을 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성하시오.

입력
4
120 110 140 150
485

출력
127
'''

import sys

def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    needs = list(map(int, readl().split()))
    M = int(readl())
    return N, needs, M

sol = -1

# 입력받는 부분
N, needs, M = input_data()

# 여기서부터 작성
# print(N, needs, M)

def solve():
    start = 0
    end = max(needs)

    while start <= end:
        middle = (start + end) // 2
        if check_budget(middle):
            sol = middle
            start = middle + 1
        else:
            end = middle - 1
    return sol

def check_budget(value):
    total = 0
    for budget_need in needs:
        if value < budget_need:
            total += value
        else:
            total += budget_need

    if total <= M:
        return True
    else:
        return False

sol = solve()
# 출력하는 부분
print(sol)