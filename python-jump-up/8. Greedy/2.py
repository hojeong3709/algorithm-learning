'''
영화관람

영화 보는걸 좋아하는 철수는 하루 종일 영화만 보려고 한다.
극장에 알아보니 N개의 영화가 상영될 예정이다.
한 영화를 보는 중에 다른 영화를 볼 수는 없으며 영화가 완전히 끝난 후에 다른 영화를 볼 수 있다.
한 영화의 종료 시간과 다음에 보고자 하는 영화의 시작 시간이 같다면 관람할 수 없다.
N개의 영화의 시작시간과 종료시간이 주어질 때 철수가 관람할 수 있는 최대 영화의 수를 구하라.

입력
첫 줄에 영화의 수 N이 입력된다. (3<=N<=100,000)
둘째 줄부터 N개의 줄에 영화 시작시간과 종료시간이 공백으로 구분되어 입력된다.
(1<=시간<=100,000,000) 종료시간이 시작시간보다 크다.

출력
관람할 수 있는 최대 영화의 수를 출력하라.

입력
5
1 3
2 5
8 10
4 7
6 9

출력
3
'''

import sys

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int,readl().split())) for _ in range(N)]
    return N, info

sol = -1

#입력받는 부분
N, info = Input_Data()

# 정렬
info = sorted(info, key=lambda x: (x[1], x[1] - x[0]) )

# print(info)

#여기서부터 작성
sol = 1

# 이중루프 순차탐색 ㄴㄴ

movie_end_time = info[0][1]

for s, e in info:
    if s > movie_end_time:
        movie_end_time = e
        sol += 1

# 출력하는 부분
print(sol)

'''
N = int(input())
data = []
for _ in range(0, N):
    s, e = map(int,input().split())
    data.append((s, e))
     
data.sort(key = (lambda x: x[1]))
sol = 1
end = data[0][1]
for s, e in data:
    if s > end:
        end = e
        sol += 1
         
print(sol) 
'''