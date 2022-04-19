

l = [1, 2, 3, 4, 5]
l.append(6)
l.remove(1)
l.insert(2, "Hey")
value = l.pop()
print(value, l)


from collections import deque
q = deque()
q.append(1)
q.append(2)
q.popleft()
print(q)


