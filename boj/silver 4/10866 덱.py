import sys
from collections import deque

n = int(sys.stdin.readline())

dp = deque([])
for i in range(n):
    tmp = sys.stdin.readline().strip().split()
    
    if len(tmp) == 1:
        tmp = tmp[0]
        if tmp == "front":
            if len(dp) == 0:
                print(-1)
            else:
                print(dp[0])

        elif tmp == "back":
            if len(dp) == 0:
                print(-1)
            else:
                print(dp[-1])

        elif tmp == "pop_front":
            if len(dp) == 0:
                print(-1)
            else:
                print(dp.popleft())
        elif tmp == "pop_back":
            if len(dp) == 0:
                print(-1)
            else:
                print(dp.pop())

        elif tmp == "size":
            print(len(dp))
        
        elif tmp == "empty":
            if len(dp) == 0:
                print(1)
            else:
                print(0)
    else:
        a,b = tmp
        if a == "push_front" :
            dp.appendleft(b)
        else:
            dp.append(b)
    
