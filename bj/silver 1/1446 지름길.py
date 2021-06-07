import sys,heapq as hq
sys.stdin = open("in.txt")
N,D = map(int,sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(D+1)]
for _ in range(N):
    s,e,c = map(int,sys.stdin.readline().rstrip().split())
    if e > D:
        continue
    else:
        dic[s].append((c,e))
que = [(0,0)]
vist = [True] * (D+1)
dist = [0] + [float("INF")] * D
while que:
    c,s = hq.heappop(que)
    if vist[s]:
        vist[s] = False
        for cost,end in dic[s]:
            if dist[end] > cost + c:
                dist[end] = cost + c
                hq.heappush(que,(cost + c, end))
        if s<D and dist[s+1] > c + 1:
            dist[s+1] = c + 1
            hq.heappush(que,(c +1,s+1))
print(dist[-1])
