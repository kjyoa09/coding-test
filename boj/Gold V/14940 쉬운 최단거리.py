from sys import stdin
from collections import deque
stdin = open("in.txt","r")
input = stdin.readline
N,M = map(int,input().rstrip().split())
maps = [list(map(int,input().rstrip().split())) for _ in range(N)]
for r in range(N):
    for c in range(M):
        if maps[r][c] == 2:
            start = (r,c)
            break

ch = [[-1] * M for _ in range(N)]
ch[start[0]][start[1]] = 0
dx = [1,0,-1,0];dy = [0,1,0,-1]
que = deque([start])
while que:
    x,y = que.popleft()
    for i in range(4):
        px,py = x+dx[i],y+dy[i]
        if 0<=px<N and 0<=py<M:
            if maps[px][py] != 0:
                if ch[px][py] == -1 or ch[px][py] > ch[x][y] + 1:
                    ch[px][py] = ch[x][y] + 1
                    que.append((px,py))
for r in range(N):
    print(" ".join([str(0) if x == 0 else str(y) for x,y in zip(maps[r],ch[r])]))