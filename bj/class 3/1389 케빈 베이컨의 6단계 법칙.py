import sys; 
n,m = map(int,sys.stdin.readline().strip().split())
inf = float("INF")
maps = [[inf] * n for _ in range(n)]

for _ in range(m):
    s,e = map(int,sys.stdin.readline().strip().split())
    maps[s-1][e-1] = 1
    maps[e-1][s-1] = 1

for k in range(n):
    maps[k][k] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]

ans = [sum(x) for x in maps]

print(ans.index(min(ans))+1)
