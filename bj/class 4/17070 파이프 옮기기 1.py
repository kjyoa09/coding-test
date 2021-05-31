# BFS >> 시간초과 :pypy로도...
# pipe 모양 별로 map >> dp >> python3으로도 통과... DP 좋네..
import sys

sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]

ch_h = [[0] * N for _ in range(N)]
ch_v = [[0] * N for _ in range(N)]
ch_d = [[0] * N for _ in range(N)]


ch_h[0][1] = 1

for r in range(0,N):
    for c in range(2,N):
        if maps[r][c] != 1:
            ch_h[r][c] += ch_h[r][c-1]
            ch_h[r][c] += ch_d[r][c-1]
            if r > 0 :
                ch_v[r][c] += ch_v[r-1][c]
                ch_v[r][c] += ch_d[r-1][c]
                if maps[r][c-1] ==0 and maps[r-1][c] == 0: 
                    ch_d[r][c] += ch_h[r-1][c-1]
                    ch_d[r][c] += ch_d[r-1][c-1]
                    ch_d[r][c] += ch_v[r-1][c-1]

print(ch_d[N-1][N-1]+ch_h[N-1][N-1]+ch_v[N-1][N-1])
'''
# 시간초과
import sys
from collections import deque
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
que = deque([((0,0),(0,1),[((0,0),(0,1))])])
ans = 0
while que:
    (x1,y1),(x2,y2),path = que.popleft()

    if x2==y2==N-1:
        ans +=1
        print(path)
    else:
        if x1==x2 and y2-y1 == 1:#hori
            if 0<= y2+1 < N and maps[x2][y2+1] == 0: # right
                que.append(((x2,y2),(x2,y2+1),path + [((x2,y2),(x2,y2+1))]))

                if 0<= x2+1 < N and maps[x2+1][y2+1] == 0 and maps[x2+1][y2] == 0: #diag
                    que.append(((x2,y2),(x2+1,y2+1),path + [((x2,y2),(x2+1,y2+1))]))

        elif y1==y2 and x2-x1 == 1:#vertical
            if 0<=x2+1<N and maps[x2+1][y2] == 0: #down
                que.append(((x2,y2),(x2+1,y2),path + [((x2,y2),(x2+1,y2))]))
                if 0 <= y2 +1 < N and maps[x2+1][y2+1] == 0 and maps[x2][y2+1] == 0:#diag
                    que.append(((x2,y2),(x2+1,y2+1),path + [((x2,y2),(x2+1,y2+1))]))
        else: #diag
            cnt = 0
            if 0 <= y2 + 1 < N and maps[x2][y2+1] == 0:
                que.append(((x2,y2),(x2,y2+1),path + [((x2,y2),(x2,y2+1))]))
                cnt += 1
            if 0 <= x2 + 1 <N and maps[x2+1][y2] == 0:
                que.append(((x2,y2),(x2+1,y2),path + [((x2,y2),(x2+1,y2))]))
                cnt += 1
            if cnt == 2 and maps[x2+1][y2 +1] == 0:
                que.append(((x2,y2),(x2+1,y2+1),path + [((x2,y2),(x2+1,y2+1))]))
print(ans)
'''
