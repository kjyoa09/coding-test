import sys
input = sys.stdin.readline
inf = float("INF")
n = int(input())
maps = [[inf] * n for _ in range(n)]
m = int(input())
for _ in range(m):
    a,b,c = map(int,input().split())
    if maps[a-1][b-1] > c:
        maps[a-1][b-1] = c
for i in range(n):
    maps[i][i] = 0
for k in range(n):
    for i in range(n):
        for j in range(n):
            if maps[i][j] > maps[i][k] + maps[k][j]:
                maps[i][j] = maps[i][k] + maps[k][j]
for tmp in maps:
    for u in tmp:
        if u == inf:
            print(0,end = " ")
        else:
            print(u,end = " ")
    print()
