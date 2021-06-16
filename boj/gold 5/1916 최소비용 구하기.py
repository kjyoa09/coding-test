import sys

import heapq as hq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
m = int(input())


inf = float("INF")

dic = defaultdict(list)
for _ in range(m):
    a,b,c = map(int,input().split())
    dic[a].append((c,b))

s,e = map(int,input().split())

visit = [True] * (n+1)
dp = [inf] * (n+1)
dp[s] = 0
Q = [(0,s)]

while Q:
    cost,dest = hq.heappop(Q)

    if visit[dest]:
        visit[dest] = False

        for co,de in dic[dest]:
            if dp[de] > cost + co:
                dp[de] = cost + co

            hq.heappush(Q,(cost+co,de))
        
print(dp[e])
