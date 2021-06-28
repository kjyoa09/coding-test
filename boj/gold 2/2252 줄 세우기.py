from collections import deque
from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N,M = map(int,input().rstrip().split())
dg = [float("INF")]+[0]*(N)
v = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().rstrip().split())
    dg[b] +=1
    v[a].append(b)
que = deque([])
ans = []
for i in range(1,N+1):
    if dg[i] == 0:
        que.append(i)
        ans.append(str(i))
while que:
    tmp = que.popleft()
    for i in v[tmp]:
        dg[i] -= 1
        if dg[i] == 0:
            que.append(i)
            ans.append(str(i))
print(" ".join(ans))