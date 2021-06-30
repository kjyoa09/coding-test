from sys import stdin
from collections import deque
stdin = open("in.txt")
input = stdin.readline

N,M = map(int,input().rstrip().split())
dg = [float("INF")]+[0]*(N)
v = [[] for _ in range(N+1)]
for _ in range(M):
    tmp = list(map(int,input().rstrip().split()))
    if tmp[0] == 1:
        continue
    else:
        for i in range(2,tmp[0]+1):
            v[tmp[i-1]].append(tmp[i])
            dg[tmp[i]] += 1
que = deque([])
for i in range(N+1):
    if dg[i] == 0:
        que.append(i)
ans = []
while que:
    tmp = que.popleft()
    ans.append(tmp)
    for i in v[tmp]:
        dg[i] -= 1
        if dg[i] == 0:
            que.append(i)
if len(ans) == N:
    for i in ans:
        print(i)
else :
    print(0)
