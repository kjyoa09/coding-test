from sys import stdin
import heapq as hq
from collections import deque
stdin = open("in.txt","r")
input = stdin.readline
N = int(input())
arr = []
for _ in range(N):
    h,o = map(int,input().strip().split(' '))
    arr.append((min(h,o),max(h,o)))
L = int(input())
arr.sort(key = lambda x:x[1])
que,ans = [],0
for h,o in arr:
    if o-h > L:
        continue
    else:
        if len(que) == 0:
            hq.heappush(que,(h,o))
        else:
            while que and que[0][0] < o-L:
                hq.heappop(que)
            hq.heappush(que,(h,o))
    ans = max(ans,len(que))
print(ans)