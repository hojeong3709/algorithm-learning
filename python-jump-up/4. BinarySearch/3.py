'''
도약
이진탐색 트리 응용

수정필요
'''

import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
# print(N, pos)

def bsearch_lower(data, start, end, search_num):
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

def bsearch_upper(data, start, end, search_num):
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

def solve():

    pos.sort()
    # print(N, pos)

    result = []
    for i in range(N-2):
        for j in range(i+1, N-1):
            first_jump = pos[j] - pos[i]
            second_jump_start = pos[j] + first_jump
            second_jump_end = pos[j] + 2 * first_jump
            # sequential search(해결완료)
            # for k in range(j+1, N):
            #     if second_jump_start <= pos[k] <= second_jump_end:
            #         result.append((pos[i], pos[j], pos[k]))

            print(pos[i], pos[j], second_jump_start, "(+{})".format(first_jump), second_jump_end, "(+{})".format(2 * first_jump))

            # binary search
            # jump start 이상값 중 가장 작은 값
            # jump end 이하값 중 가장 큰값
            # 음... 아직도 잘모르겠다.
            lower = bsearch_lower(pos, j + 1, N - 1, second_jump_start)
            upper = bsearch_upper(pos, j + 1, N - 1, second_jump_end)
            if lower != -1:
                result.append((pos[i], pos[j], pos[lower]))
            if upper != -1:
                result.append((pos[i], pos[j], pos[upper]))
            
            # if lower!=-1 and pos[lower] <= second_jump_end:
            #     upper = bsearch_upper(pos, lower, N - 1, second_jump_end)
            #     result += upper - lower + 1

    # print(result)

    return result

sol = solve()

# 출력하는 부분
print(sol)