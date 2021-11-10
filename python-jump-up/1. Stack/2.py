'''
stack, python style
'''

N = int(input())
a = list(map(int, input().split()))



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