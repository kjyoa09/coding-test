# 노드 별 Dijk >> 갈 수 있는 곳 파악
# 합이 가장 큰 값
import sys, heapq as hq
sys.stdin = open("in.txt","r")

N,M,R = map(int,sys.stdin.readline().rstrip().split())

item = {i:v for i,v in zip(range(1,N+1),list(map(int,sys.stdin.readline().rstrip().split())))}

maps = [[] for _ in range(N+1)]
for _ in range(R):
    s,e,v = map(int,sys.stdin.readline().rstrip().split())
    maps[s].append((v,e))
    maps[e].append((v,s))

inf = float("INF")
def dijk(start):
    que = [(0,start)]
    visit = [True] * (N+1)
    
    COST = [inf] * (N+1)
    COST[start] = 0     
    
    while que:
        c,s = hq.heappop(que)
        if visit[s]:
            visit[s] = False
            for cost,e in maps[s]:
                if cost + c < COST[e]:
                    hq.heappush(que,(cost + c, e))
                    COST[e] = cost + c
    return COST
ans = -1
for i in range(1,N+1):
    tmp = sum([item[idx] for idx,x in enumerate(dijk(i)) if x <= M])
    if ans < tmp:
        ans = tmp
print(ans)