import sys,heapq as hq
sys.stdin = open("in.txt","r")
a,b = map(int,sys.stdin.readline().rstrip().split())
N,M = map(int,sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((1,e))
    dic[e].append((1,s))
visit = [True] * (N+1)
dist = [float("INF")] * (N+1)
dist[a] = 0
que = [(0,a)]
while que:
    c,s = hq.heappop(que)
    if visit[s]:
        visit[s] = False
        for cost,end in dic[s]:
            if dist[end] > cost + c:
                dist[end] = cost + c
                hq.heappush(que,(cost+c,end))
    if visit[b] == False:
        break

if visit[b]:
    print(-1)
else:
    print(dist[b])
