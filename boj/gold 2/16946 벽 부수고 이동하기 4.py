# 1 인 지점마다 BFS >> 시간 초과
# 연결된 0끼리 그룹으로 묶고 arr 에 개수 메모
# 1 인 지점마다 그룹 중복되지 않게 더하기
# 10으로 나눈 나머지(문제 잘읽기)
from sys import stdin
from collections import deque
stdin = open("in.txt")
input = stdin.readline
N,M = map(int,input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(N)]
check = [[-1 for _ in range(M)] for __ in range(N)]
arr = []
dx,dy = [1,0,-1,0],[0,1,0,-1]
def bfs(r,c,flag):
    que = deque([(r,c)])
    visit = 1
    while que:
        x,y = que.pop()
        for i in range(4):
            px,py = x+dx[i],y+dy[i]
            if 0<=px<N and 0<=py<M and maps[px][py] == "0" and check[px][py] == -1:
                visit += 1
                que.append((px,py))
                check[px][py] = flag
    arr.append(visit)
flag = -1
for r in range(N):
    for c in range(M):
        if check[r][c] == -1 and maps[r][c] == "0":
            flag += 1
            check[r][c] = flag
            bfs(r,c,flag)
for r in range(N):
    for c in range(M):
        if maps[r][c] == "1":
            tmp = []
            cnt = 1
            for i in range(4):
                px,py = r+dx[i],c+dy[i]
                if 0<=px<N and 0<=py<M and check[px][py] != -1 and check[px][py] not in tmp:
                    tmp.append(check[px][py])
                    cnt += arr[check[px][py]]
            maps[r][c] = str(cnt%10)
for i in maps:
    print("".join(i))