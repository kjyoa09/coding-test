import sys
from collections import deque

a,b = map(int,sys.stdin.readline().strip().split())

dq = deque(list(range(1,a+1)))

print("<",end = "")
cnt = 0 
while len(dq)!=1:

    if cnt == b-1:
        print(dq.popleft(),end = ", ")
        cnt = 0
    else:
        cnt += 1
        dq.append(dq.popleft())
print(dq.pop(),">",sep = "")
