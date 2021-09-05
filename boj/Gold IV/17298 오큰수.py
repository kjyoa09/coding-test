import sys
from collections import deque


N = int(sys.stdin.readline())
arr = deque(list(map(int,sys.stdin.readline().strip().split())))

ans = ["-1"] * N

i = 0
stack = deque([(arr.popleft(),i)])

while arr:
    i += 1
    tmp = arr.popleft()
    
    if stack[-1][0] < tmp:
        while stack:
            if stack[-1][0] < tmp:
                a,idx = stack.pop()
                ans[idx] = str(tmp)
            else:
                break
    
    stack.append((tmp,i))

print(" ".join(ans))