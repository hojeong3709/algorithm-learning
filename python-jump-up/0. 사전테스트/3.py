import sys


def input_data():

    readl = sys.stdin.readline

    N = int(readl())

    num = [float(readl()) for _ in range(N)]

    return N, num


sol = 0.0

# 입력받는 부분

N, num = input_data()


# 여기서부터 작성

def solve():
    # print(N, num)
    
    '''
    누적곱, 수정필요
    '''
    max = 0;
    for i in range(N-1):
        value = num[i] * num[i+1]
        if max < value:
            max = value
    
    return max

sol = solve()

# 출력하는 부분 

print(f"{sol:.3f}") 