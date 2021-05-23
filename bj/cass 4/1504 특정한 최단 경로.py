# 다익스트라
# 플로이드 와샬 시간초과
import sys
import heapq as hq
from collections import defaultdict

sys.stdin = open("in.txt","r")

N,E = map(int,sys.stdin.readline().rstrip().split())

inf = float("INF")

dic = defaultdict(list)
maps = [[inf] * N for _ in range(N)]

for _ in range(E):
    s,e,r = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((r,e))
    dic[e].append((r,s))

v1,v2 = map(int,sys.stdin.readline().rstrip().split())

def fi(start):
    visit = [inf] * (N+1)
    que = [[0,start]]
    visit[start] = 0
    while que:
        tmp = hq.heappop(que)
        for v,e in dic[tmp[1]]:
            if visit[e] > tmp[0] + v:
                 visit[e] = tmp[0] + v
                 hq.heappush(que,[visit[e],e])
    return visit

ans1,ans2=fi(1)[v1] + fi(v1)[v2] + fi(v2)[N],fi(1)[v2] + fi(v2)[v1] + fi(v1)[N] 
if ans1 == inf and ans2 == inf:
    print(-1)
else:
    print(min(ans1,ans2))