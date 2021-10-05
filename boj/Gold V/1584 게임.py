from sys import stdin
import heapq as hq

stdin = open("in.txt","r")
input = stdin.readline

maps = [[0] * 501 for _ in range(501)]
ch = [[True] * 501 for _ in range(501)]
for _ in  range(int(input())):
    x1,y1,x2,y2 = map(int,input().strip().split(' '))
    for r in range(min(x1,x2),max(x1,x2)+1):
        for c in range(min(y1,y2),max(y1,y2)+1):
            maps[r][c] = 1

for _ in  range(int(input())):
    x1,y1,x2,y2 = map(int,input().strip().split(' '))
    for r in range(min(x1,x2),max(x1,x2)+1):
        for c in range(min(y1,y2),max(y1,y2)+1):
            maps[r][c] = -1

que = [(0,0,0)]
D = [(0,1),(1,0),(0,-1),(-1,0)]
ch[0][0] = False
while que:
    cnt,nx,ny = hq.heappop(que)
    if nx==ny==500:
        print(cnt)
        break
    
    for dx,dy in D:
        px,py = nx + dx,ny + dy
        if 0<=px<501 and 0<=py<501 and maps[px][py] != -1 and ch[px][py]:
            ch[px][py] = False
            hq.heappush(que,(cnt+maps[px][py],px,py))
else:
    print(-1)