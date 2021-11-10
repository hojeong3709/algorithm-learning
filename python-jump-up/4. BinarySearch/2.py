'''
숫자카운팅 - 이진탐색 응용
배열에 오름차순으로 N개의 숫자가 저장되어 있다.
M개의 탐색할 숫자가 주어질 때, 각 숫자가 배열에 몇 개씩 저장되어 있는지 출력하는 프로그램을 작성하시오.
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	data = list(map(int,readl().split()))
	T = int(readl())
	num = list(map(int,readl().split()))
	return N, data, T, num


# 입력받는 부분
N, data, T, num = Input_Data()

# 여기서부터 작성

def bsearch_lower(start, end, search_num):
    sol = -1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == search_num:
            sol = middle
            end = middle - 1
        elif data[middle] > search_num:
            end = middle - 1
        else:
            start = middle + 1
    return sol

def bsearch_upper(start, end, search_num):
    sol = -1
    while start <= end:
        middle = (start + end) // 2
        if data[middle] == search_num:
            sol = middle
            start = middle + 1
        elif data[middle] > search_num:
            end = middle - 1
        else:
            start = middle + 1
    return sol

# 여기서부터 작성
def solve():
  
    result = []
    for search_num in num:
        start = 0
        end = N-1
        lo = bsearch_lower(start, end, search_num)
        if lo == -1:
            result.append(0)
        else:
            result.append(bsearch_upper(start, end, search_num) - lo + 1)

    return result

sol = solve()

print(*sol)