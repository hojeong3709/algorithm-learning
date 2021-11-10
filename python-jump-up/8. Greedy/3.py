'''
냉장고

N개의 화학 물질 C1, C2, …, Cn이 있다. 이들 각각은 보관되어야 할 온도가 각기 다른데, 각 Ci마다 최저보관온도 xi와 최고보관온도 yi가 정해져 있다. 
즉 Ci는 온도 xi이상, yi이하의 온도에서 보관되어야만 안전하다.
이 화학 물질들을 모두 보관하기 위해서는 여러 대의 냉장고가 필요한데 가능하면 적은 수의 냉장고를 사용하고 싶다. 이를 해결하는 프로그램을 작성하시오.

입력
첫 줄에 화학물질의 수 N이 입력된다. N의 범위는 1이상 100이하이다.
두 번째 줄부터 N+1줄까지 최저보관온도와 최고보관온도가 입력된다.
보관온도는 -270° ~ 10,000°이며, 각 냉장고는 임의의 정해진 온도를 일정하게 유지할 수 있고, 냉장고는 아주 크다고 가정한다.

출력
첫 줄에 최소로 필요한 냉장고의 대수를 출력한다.

입력
4
-15 5
-10 36
10 73
27 44

출력
2
'''

import sys 

def input_data(): 
    readl = sys.stdin.readline 
    N = int(readl()) 
    chems = [list(map(int,readl().split())) for _ in range(N)] 
    return N, chems 

# 입력받는 부분 
N, chems = input_data() 

# 여기서부터 작성 
#  1 <= N <= 100
# print(N)
# print(chems)

chems = sorted(chems, key=lambda x: x[1])

icebox_end = chems[0][1]
sol = 1

for s, e in chems:
    if s > icebox_end:
        icebox_end = e
        sol += 1

# 출력하는 부분 

print(sol) 