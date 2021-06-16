import sys
sys.setrecursionlimit(10**5)
m,n = map(int,sys.stdin.readline().split()) 
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
visit = [[0] * n for _ in range(m)]
ch = [[-1] * n for _ in range(m)]
def dfs(x,y):   
    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    
    if x == m-1 and y == n-1:
        return 1
    if (ch[x][y] != -1): return visit[x][y]
    for i in range(4):
        nextX = x + dx[i]
        nextY = y + dy[i]
        if 0 <= nextX < m and 0 <= nextY < n:
            if arr[nextX][nextY] < arr[x][y]:
                visit[x][y] += dfs(nextX,nextY)
                ch[x][y] = 0
    return visit[x][y]
dfs(0,0)
print(visit[0][0])

