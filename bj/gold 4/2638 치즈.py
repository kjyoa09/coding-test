from collections import deque
from sys import stdin
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())
maps = [list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]
inf = float("INF")
dx = [0,1,0,-1];dy = [1,0,-1,0]
def BFS(maps):
    check = [[inf] * M for _ in range(N)]
    ch = []
    for c in range(M):
        for r in range(N):
            if maps[r][c] == 1:#치즈
                ch.append((r,c))
                check[r][c] = 1
            else:#공기
                if check[r][c] == inf :# not visit
                    flag = False
                    visit = [(r,c)]
                    que = deque([(r,c)])
                    while que:
                        x,y = que.popleft()
                        for i in range(4):
                            px = x + dx[i];py = y + dy[i]
                            if 0<= px < N and 0<= py < M and maps[px][py] == 0 and check[px][py] == inf:
                                check[px][py] = 0
                                visit.append((px,py))
                                que.append((px,py))
                                if px == 0 or px == N-1 or py == 0 or py == M-1:
                                    flag = True
                    if flag == False: # 치즈 속 공기
                        for x,y in visit:
                            check[x][y] = -1

    return ch,check

ans = 0
while 1:
    ch,maps = BFS(maps)
    if len(ch) == 0:
        break
    else:        
        ans += 1
        check = [[0] * M for _ in range(N)]
        for r,c in ch:
            cnt = 0
            for i in range(4):
                px = r + dx[i];py = c + dy[i]
                if 0<= px < N and 0<= py < M and maps[px][py] == 0:
                    cnt +=1
                if cnt == 2:
                    break
            else:
                check[r][c] = 1
    maps = check    
print(ans)
