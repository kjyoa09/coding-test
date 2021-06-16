import sys
import heapq as hq
from collections import defaultdict


v,e = map(int,sys.stdin.readline().split())
s = int(sys.stdin.readline())

inf = float("INF")


dic = defaultdict(list)
for _ in range(e):
    a,b,cost = map(int,sys.stdin.readline().split())
    dic[a].append((cost,b))

Q = [(0, s)]
visited = [True] * (v+1)
dp = [float('inf')] * (v+1)
dp[s] = 0
while Q:
    co, des =  hq.heappop(Q)

    if visited[des]:
        visited[des] = False
        for cost, destination in dic[des]:
            
            dp[destination] = min(cost + dp[des], dp[destination])
            hq.heappush(Q, (dp[destination], destination))


for i in dp[1:]:
    if i == inf:
        print("INF")
    else:
        print(i)
