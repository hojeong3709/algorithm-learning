'''
calculator with stack
'''
import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	str_exp = readl().split()
	nums = list(map(int,str_exp[0::2]))
	op = str_exp[1::2]
	return N, nums, op

sol = -1
# 입력받는 부분
N, nums, op = Input_Data()

# 여기서부터 작성
# print(N)
# print(nums)
# print(op)

def solve():
    stack = []

    for i, num in enumerate(nums):
        if i == 0:
            stack.append(num)
        else:
            if op:
                o = op.pop(0)

            if o == "+":
                value = num
                stack.append(value)
            elif o == "-":
                value = -num
                stack.append(value)
            elif o == "*":
                if stack:
                    value1 = stack.pop()
                    value2 = num
                    stack.append(value1 * value2)
            elif o == "/":
                if stack:
                    value1 = stack.pop()
                    value2 = num
                    stack.append(int(value1 / value2))

        # print(stack)
    
    return sum(stack)

sol = solve()

# 출력하는 부분
print(sol)


# def solve():
#     stack = []
#     stack.append(nums[0])
#     # solve1    
#     # for i in range (N-1):
#     #     if op[i] == '+':
#     #         stack.append(nums[i+1])
#     #     elif op[i] == '-':
#     #         stack.append(-nums[i+1])
#     #     elif op[i] == '*':
#     #         stack.append(stack.pop() * nums[i+1])
#     #     elif op[i] == '/':
#     #         stack.append(int(stack.pop() / nums[i+1]))

#     # sovle2
#     # for o, n in zip(op, nums[1:]):
#     #     if o == '+':
#     #         stack.append(n)
#     #     elif o == '-':
#     #         stack.append(-n)
#     #     elif o == '*':
#     #         stack.append(stack.pop() * n)
#     #     elif o == '/':
#     #         stack.append(int(stack.pop() / n))
   
#     return sum(stack)

# sol = solve()

# # 출력하는 부분
# print(sol)