'''
기출 - 기부금
'''
import sys

def input_data():
    readl = sys.stdin.readline
    N,  M = map(int,  readl().split())
    insentive = list(map(int,  readl().split()))
    return N,  M,  insentive
sol = -1

# 입력받는 부분
N,  M,  insentive = input_data()

# 여기서부터 작성
def solve():

    # N ==> 직원수
    # M ==> 기부금 목표금액
    # insentive ==> 성과급

    start = 0
    end = max(insentive)

    while start <= end:
        middle = (start + end) // 2
        if check_donation_goal(middle):
            sol = middle
            start = middle + 1
        else:
            end = middle -1
    return sol

def check_donation_goal(donation_goal):
    donation_total = 0
    for ins in insentive:
        donation = ins - donation_goal
        if donation >= 0:
            donation_total += donation    
    
    if donation_total >= M:
        return True
    else:
        return False

sol = solve()

# 출력하는 부분
print(sol)