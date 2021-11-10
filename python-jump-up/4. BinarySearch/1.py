'''
이진탐색
오름차순의 순서대로 정렬되어 있는 N개의 데이터에서 특정한 숫자가 몇 번째 위치에 있는지를 알아내는 프로그램을 작성하시오.
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	data = [0] + list(map(int,readl().split()))
	T = int(readl())
	num = list(map(int,readl().split()))
	return N, data, T, num


# 입력받는 부분
N, data, T, num = Input_Data()

# print(N, data, T, num)

def bsearch(start, end, search_num):
    middle = (start + end) // 2
    while start <= end:
        if data[middle] == search_num:
            return middle
        elif data[middle] < search_num:
            start = middle + 1
        else:
            end = middle -1
        
        middle = (start + end) // 2
    return 0

# 여기서부터 작성
def solve():
  
    result = []

    for search_num in num:
        start = 0
        end = N-1
        result.append(bsearch(start, end, search_num))
        
    # print(result)
    return result

sol = solve()

print(*sol)