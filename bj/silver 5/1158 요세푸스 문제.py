import sys
from collections import deque
n,k = map(int,sys.stdin.readline().strip().split())
dq = deque(list(range(1,n+1)))
cnt = 0
print("<",end = "")
while len(dq) != 1:
    cnt += 1
    tmp = dq.popleft()
    if cnt == k:
        print(tmp,", ",sep ="",end = "")
        cnt = 0
    else:
        dq.append(tmp)
print(dq.pop(),">",sep ="")
