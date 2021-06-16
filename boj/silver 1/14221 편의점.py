##pypy
##python3 시간초과..
import sys,heapq as hq
sys.stdin = open("in.txt","r")
n,m = map(int,sys.stdin.readline().rstrip().split())
dic = [[] for _ in range(n+1)]
for _ in range(m):
    s,e,c = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((c,e))
    dic[e].append((c,s))
dic = [sorted(x,key=lambda x:x[0]) for x in dic]
p,q = map(int,sys.stdin.readline().rstrip().split())
home = list(map(int,sys.stdin.readline().rstrip().split()))
conv = list(map(int,sys.stdin.readline().rstrip().split()))

def dijk(s):
    visit = [True] * (n+1)
    dist = [float("INF")] * (n+1)
    dist[s] = 0
    que = [(0,s)]
    flag = False
    while que:
        c,s = hq.heappop(que)
        if visit[s]:
            visit[s] = False        
            for cost,end in dic[s]:
                if dist[end] > cost + c:
                    dist[end] = cost + c
                    hq.heappush(que,(cost + c, end))
    # return dist
                    if e in conv:
                        return cost + c
                        

ans = 0
min_dist = float("INF")
for h in home:
    tmp = dijk(h)
    if tmp != None and tmp < min_dist:
        ans = h
        min_dist = tmp
print(ans)    