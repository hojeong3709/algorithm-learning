'''
거스름돈

여러분은 한국의 자동판매기용 프로그램의 개발을 의뢰 받았다.
이번에 개발할 프로그램은 자동판매기에서 이용자에게 거스름돈을 남겨줄 때, 거스름돈에 사용될 동전의 수를 가정 적게 하는 것이다.
입력으로 거슬러 줘야 할 돈의 액수가 들어온다.
여러분은 그 돈의 액수를 거슬러 주는 여러 가지 방법들 중 가장 적은 동전은 몇 개 인지 구하는 프로그램을 작성해야 된다.
단, 대한민국에서 사용하는 동전의 종류는 500, 100, 50, 10의 4가지 종류가 있으며, 동전의 수는 무한하다.

입력
첫 번째 줄에 거슬러줘야 할 돈의 액수가 입력된다. (최대 액수는 10000원)

출력
가장 적게 지불할 동전의 수를 출력한다.

'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    change = int(readl())
    return change

sol = -1
# 입력받는 부분
change = Input_Data()

# 여기서부터 작성
def solve():
    global change

    coins = [500, 100, 50, 10]

    total_cnt = 0
    for coin in coins:
        if change > 0:
            cnt = change // coin
            change = change - coin * cnt
            total_cnt += cnt

    return total_cnt

sol = solve()

# 출력하는 부분
print(sol)