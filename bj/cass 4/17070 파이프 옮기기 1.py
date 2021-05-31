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