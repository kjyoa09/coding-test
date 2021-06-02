import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

n = int(sys.stdin.readline())

maps = [list(sys.stdin.readline().strip()) for _ in range(n)]
tmp = [x[:] for x in maps]

dx = [0,1,0,-1]; dy = [1,0,-1,0]
def dfs(x,y):
    for i in range(4):
        px,py = x + dx[i], y + dy[i]
        if (0 <= px < n) and (0 <= py < n) and check[px][py] and maps[px][py] == maps[x][y]:
            check[px][py] = False
            dfs(px,py)

ans = [0,0]
for idx in range(2):
    check = [[True] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] :
                check[i][j] = False
                dfs(i,j)
                ans[idx] +=1


            if tmp[i][j] == "R":
                tmp[i][j] = "G"
                
    maps = tmp
for i in ans:
    print(i, end = " ")

