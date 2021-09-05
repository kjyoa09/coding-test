# 처음 시작 하는 자리 0으로 초기화
# BFS 탐색 : 먹이 찾으면 찾은 거리보다 먼 경우 제외
import sys
from collections import deque
sys.stdin = open("in.txt","r")

n = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            start = (i,j,0)
            maps[i][j] = 0
            break
dx = [1,0,-1,0]
dy = [0,1,0,-1]
inf = float("INF")

def find(start,maps,size):
    inf_cnt = inf
    que = deque([start])
    check = [[True] * n for _ in range(n)]
    check[start[0]][start[1]] = False
    pray = []
    while que:
        x,y,cnt = que.popleft()

        for i in range(4):
            px,py = x + dx[i],y + dy[i]
            if 0<= px < n and 0<= py < n and check[px][py] and maps[px][py] <= size and cnt + 1 <= inf_cnt:
                check[px][py] = False
                que.append((px,py,cnt + 1))
                if maps[px][py] < size and maps[px][py] != 0:
                    pray.append((px,py,cnt + 1))
                    inf_cnt = cnt + 1
    return pray

num = 0
size = 2
ans = 0
while 1:
    pray = find(start,maps,size)
    if len(pray) == 0:
        print(ans)
        break
    else:
        pray.sort(key = lambda x : (x[2],x[0],x[1]))
        x,y,move = pray.pop(0)
        ans += move
        maps[x][y] = 0
        num += 1        
        start = (x,y,0)    
    if num == size :
        size += 1
        num = 0
