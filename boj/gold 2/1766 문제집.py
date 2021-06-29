# 위상 정렬 + heap
# list에 추가할 때 append 사용 += 별로인 듯
from sys import stdin
import heapq as hq
stdin = open("in.txt")
input = stdin.readline
N,M = map(int,input().rstrip().split())
dg = [float("INF")]+[0]*(N)
v = [[]for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().rstrip().split())
    v[a].append(b)
    dg[b] += 1
que = []
for idx,va in enumerate(dg):
    if va == 0:
        hq.heappush(que,idx)

ans = []
while que:
    tmp = hq.heappop(que)
    ans.append(str(tmp))
    for i in v[tmp]:
        dg[i] -= 1
        if dg[i] == 0:
            hq.heappush(que,i)
print(" ".join(ans))

