import sys

T = int(sys.stdin.readline())

def bfs(arr,ch):
    cnt = 0
    while arr:
        x,y = arr.pop(0)
        if ch[x][y] == 0:
            continue
        else:
            ch[x][y] = 0
            cnt += 1
            Q = [(x,y)]
            while Q:
                x,y = Q.pop(0)
                for i in range(4):
                    nextX,nextY = x+dx[i],y+dy[i]
                    if 0<= nextX < m and 0<= nextY <n and ch[nextX][nextY] == -1:
                        ch[nextX][nextY] = 0
                        Q += [(nextX,nextY)]

          
    return cnt


for _ in range(T):
    m,n,k = map(int,sys.stdin.readline().split())

    ch = [[0] * n for _ in range(m)]

    dx = [1,0,-1,0]; dy = [0,1,0,-1]
    arr = []
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        arr += [(x,y)]
        ch[x][y] = -1


    print(bfs(arr,ch))

