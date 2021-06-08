from collections import deque

n = int(input())

dq = deque(list(range(1,n+1)))

while len(dq) != 1:
    tmp = dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
