'''
list, python style
-> stack, queue
'''

N = int(input())
a = list(map(float, input().split()))

print(N, a)

# stack = list()

# for x in a:
#     if x:
#         if len(stack) < 4:
#             stack.append(x)
#         else:
#             print(-1, end=' ')
#     else:
#         if stack:
#             print(stack.pop(), end=' ')
#         else:
#             print(-1, end=' ')