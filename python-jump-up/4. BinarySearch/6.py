'''
어민
한 작은 나라에서는 대부분의 시민들이 어부이며, 그 나라의 모든 마을은 직선 해변을 따라 건설된 직선 도로에 위치해 있다.
마을의 어부들은 엄청난 양의 물고기를 잡았으나 예전처럼 물고기를 좋아하지 않아서 이웃 나라의 가난하고 배고픈 아이들을 입양하기로 결정했다.
하나의 긴 직선 도로가 해변을 따라 모든 마을을 연결한다. 따라서 각 도시(첫 번째와 마지막 도시는 제외)는 두 이웃 마을에 직접 연결된다. 1년에 한 명의 어린이가 1톤의 물고기를 먹는다. 어떤 마을에서 잡힌 물고기의 양은 그 마을에서 먹거나 다른 마을로 옮길 수 있다.
도로를 이용해서 옮겨야 하는데 이용에 따른 세금이 부과된다. 1km당 1톤의 물고기를 세금으로 내야 한다.
각 마을마다 동등한 수의 가난한 아이들이 입양되기를 원한다. 각 마을에 수용될 수 있는 아이들의 최대 수를 결정하는 프로그램을 작성하시오. 모든 물고기가 잡히고 저렴하게 운반된 물고기를 먹을 수 있다는 조건이다.

첫 번째 줄에는 마을 수 N(1≤N≤100,000, 정수)이 입력된다
두 번째 줄부터 N줄에 걸쳐 마을 정보가 입력된다. 마을 정보는 두 개의 정수A, B이며 공백으로 구분되어 입력된다. A는 도시의 위치이며 B는 잡힌 물고기 양이다. (1≤A≤1,000,000,000, 단위는 km) (0≤B≤1,000,000,000, 단위는 톤)
마을 정보는 도로 위치에 따라 오름차순으로 정렬되어 입력된다.
'''
import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = -1

# 입력받는 부분
N, info = input_data()
M = 1000000000

# 여기서부터 작성
# print(N, info)

def solve():
    start = 1
    end = M
    result = -1

    while start <= end:

        middle = (start + end) // 2
        if check_child_num(middle):
            result = middle
            start = middle + 1
        else:
            end = middle -1

    return result

def check_child_num(child_num):

    fish_transfer = 0
    for i in range(N-1):
        town_fish_amount = info[i][1] + fish_transfer - child_num
        town_distance_tax = info[i+1][0] - info[i][0]
        fish_transfer = town_fish_amount - town_distance_tax
        
        if town_fish_amount >= 0 and fish_transfer < 0:
            fish_transfer = 0
        # print("fish_transfer : {}".format(fish_transfer))
    
    last_town_fish_amount = info[N-1][1] + fish_transfer - child_num
    if last_town_fish_amount >= 0:
        return True
    else:
        return False 

# def check_child_num(kid):
#     extra = 0
#     for i in range(N-1):
#         remain = info[i][1] + extra - kid
#         extra = remain - (info[i+1][0] - info[i][0])
#         if ((remain >= 0) and  (extra<0)): extra=0
#     return info[N-1][1] + extra >= kid

sol = solve()

# 출력하는 부분
print(sol)