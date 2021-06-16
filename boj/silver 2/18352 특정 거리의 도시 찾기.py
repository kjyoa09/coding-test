import sys,heapq as hq
sys.stdin = open("in.txt")
N,M,K,X = map(int,sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((1,e))

visit = [True] * (N+1)
distance = [float("INF")] * (N+1)
distance[X] = 0
que = [(0,X)]
while que:
    c,s = hq.heappop(que)
    if visit[s]:
        visit[s] = False
        for cost,end in dic[s]:
            if distance[end] > cost + c:
                distance[end] = cost + c
                hq.heappush(que,(cost+c,end))
ans = [idx for idx,v in enumerate(distance) if v == K]
if len(ans) == 0:
    print(-1)
else:
    for i in ans:
        print(i)