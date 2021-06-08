import sys
from collections import deque

def bfs(S,arr):
    dx = [1,0,-1,0,1,-1,-1,1]
    dy = [0,1,0,-1,1,-1,1,-1]
    while S:
        x,y = S.pop()
        for i in range(8):
            nextX,nextY = x + dx[i],y + dy[i]
            if 0 <= nextX < h and 0 <= nextY < w and  arr[nextX][nextY]== 1:
                arr[nextX][nextY] = 0
                S += [(nextX,nextY)]


while 1:

    w,h = map(int,sys.stdin.readline().split())
    
    if w == h == 0:
        break
    arr = deque([])
    maps = []
    for _ in range(h):
        tmp = list(map(int,sys.stdin.readline().split()))
        arr += [(_,idx) for idx,x in enumerate(tmp) if x == 1]
        maps += [tmp]
    cnt = 0
    while arr:
        x,y = arr.pop()
        if maps[x][y] == 0:
            continue
        else:
            maps[x][y] = 0
            bfs(deque([(x,y)]),maps)
            cnt += 1
    print(cnt)
