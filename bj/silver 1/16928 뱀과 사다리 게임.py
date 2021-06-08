import sys; 
from collections import defaultdict

n,m = map(int,sys.stdin.readline().strip().split())

dic = defaultdict(int)
for i in range(n+m):
    s,e = map(int,sys.stdin.readline().strip().split())
    dic[s] = e

Q = [(1,0)]
visit = [True]*2 +[False] * 99

while Q:
    v,cnt = Q.pop(0)
    post = [v + i for i in range(1,7) if v + i <= 100]
    post = [dic[x] if x in dic else x for x in post]

    for i in post:
        if not visit[i]:
            visit[i] = cnt+1
            Q += [(i,cnt + 1)]
print(visit[-1])
