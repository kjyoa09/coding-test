import sys

n,m = map(int,sys.stdin.readline().split())
arr = []
for _ in range(n):
    a = list(sys.stdin.readline())
    arr += [a[:m]]

inf = float("INF")
ch = [[inf] * m for _ in range(n)]

Q = [(0,0)]
ch[0][0] = 1

dx = [1,0,-1,0];dy = [0,1,0,-1]
while Q:
    x,y = Q.pop(0)

    for i in range(4):
        nextX,nextY = x + dx[i],y + dy[i]
        if 0<= nextX < n and 0 <= nextY < m and ch[x][y] + 1 < ch[nextX][nextY] and arr[nextX][nextY] == "1" :
            ch[nextX][nextY] = ch[x][y] + 1
            Q += [(nextX,nextY)]


print(ch[n-1][m-1])

