from sys import stdin
from collections import deque
stdin = open('in.txt','r')
input = stdin.readline

N,M,K = map(int,input().strip().split())
maps = [list(input().strip()) for _ in range(N)]
inf = float("INF")
check = [[[inf] * M for _ in range(N)] for _ in range(K+1)]
dx,dy = [0,1,0,-1],[1,0,-1,0]

for k in range(K):
    check[k][0][0] = 0

que = deque([(0,0,0,0)])

while que:
    x,y,k,cnt = que.popleft()
    for i in range(4):
        px,py = x+dx[i],y+dy[i]
        if 0 <= px < N and 0 <= py < M :
            if maps[px][py] == "0":
                if check[k][px][py] > cnt + 1 :
                    check[k][px][py] = cnt +1
                    que.append((px,py,k,cnt + 1))
            else:
                if k+1<=K and check[k+1][px][py] > cnt + 1 :
                    check[k+1][px][py] = cnt +1
                    que.append((px,py,k+1,cnt + 1))

if all(check[k][-1][-1] == inf for k in range(K+1)) :
    print(-1)
else:
    print(min(check[k][-1][-1]for k in range(K+1))+1)