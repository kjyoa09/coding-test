import sys
import heapq as hq
sys.stdin = open("in.txt","r")
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
dic = {i:[] for i in range(1,n+1)}
for _ in range(m):
    s,e,v = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((v,e))
s,e = map(int,sys.stdin.readline().rstrip().split())
inf = float("INF")
que = [(0,s,[s])]
visit = [inf] * (n+1)
visit[s] = 0 
path = []

while que:
    v,s,r = hq.heappop(que)    
    for cost,end in dic[s]:
        if visit[end] > cost + v:
            visit[end] = cost + v
            hq.heappush(que,(cost + v,end,r + [end]))
            if end == e:
                path = r + [end] 
print(visit[e])
print(len(path))
print(" ".join(map(str,path))) 