# Check map 두개 만들어서 BFS [TF : 이전에 벽을 부수면 F else : T]
# DFS는 Recursion error
import sys
from collections import deque
sys.stdin = open("in.txt","r")

N,M = map(int,sys.stdin.readline().rstrip().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
inf = float("INF")
check_T = [[inf] * M for _ in range(N)]
check_F = [[inf] * M for _ in range(N)]
dx,dy = [0,1,0,-1],[1,0,-1,0]

check_T[0][0] = 0
check_F[0][0] = 0

que = deque([(0,0,True,0)])

while que:
    x,y,TF,cnt = que.popleft()
    for i in range(4):
        px,py = x+dx[i],y+dy[i]
        if 0 <= px < N and 0 <= py < M :
            if maps[px][py] == "0":
                if TF and check_T[px][py] > cnt + 1 :
                    check_T[px][py] = cnt +1
                    que.append((px,py,True,cnt + 1))
                elif not TF and check_F[px][py] > cnt + 1 :
                    check_F[px][py] = cnt +1
                    que.append((px,py,False,cnt + 1))                       
            else:
                if TF and check_F[px][py] > cnt + 1 :
                    check_F[px][py] = cnt +1
                    que.append((px,py,False,cnt + 1))

if check_T[N-1][M-1] == check_F[N-1][M-1] == inf:
    print(-1)
else:
    print(min(check_T[N-1][M-1],check_F[N-1][M-1])+1)


'''
DFS
import sys
from collections import deque
sys.setrecursionlimit(10*10)
N,M = map(int,sys.stdin.readline().rstrip().split())

maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
ans = float("INF")
check = [[True] * M for _ in range(N)]
dx,dy = [0,1,0,-1],[1,0,-1,0]

def dfs(coord,ch,TF,cnt):
    global ans

    if coord == (N-1,M-1):
        if ans > cnt:
            ans = cnt
        return
    else:
        x,y = coord
        for i in range(4):
            px,py = x+dx[i],y+dy[i]
            if 0 <= px < N and 0 <= py < M and ch[px][py]:
                if maps[px][py] == "0":
                    ch[px][py] = False
                    dfs((px,py),ch,TF,cnt + 1)
                    ch[px][py] = True
                elif maps[px][py] == "1" and TF:
                    ch[px][py] = False
                    dfs((px,py),ch,False,cnt + 1)
                    ch[px][py] = True

dfs((0,0),check,True,0)
if ans == float("INF"):
    print(-1)
else:
    print(ans+1)
'''