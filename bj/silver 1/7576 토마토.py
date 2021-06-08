import sys
from collections import deque

a,b = map(int,input().split())
dx = [1,0,-1,0];dy=[0,1,0,-1]
ch = [[0] * a for _ in range(b)]
S = deque([])
cnt = 0
for r in range(b):
    tmp = sys.stdin.readline().split()
    for c in range(a):
        if tmp[c] == "1":
            S.append((r,c)) 
        elif tmp[c] == "0":
            ch[r][c] = -1
            cnt += 1
if cnt == 0:
    print(0)
else:
    day = 0
    while 1:
        nextS = deque()
        while S:
            tmp = S.popleft()

            for i in range(4):
                coord = (tmp[0] + dx[i],tmp[1] + dy[i])
                if 0 <= coord[0] < b and 0 <= coord[1] < a and ch[coord[0]][coord[1]] == -1:

                    ch[coord[0]][coord[1]] = 0
                    nextS.append(coord)
                    cnt -= 1
        day += 1
        if cnt == 0:
            print(day)
            break
        else:
            if len(nextS) == 0:
                print(-1)
                break
            else:
                S = nextS
