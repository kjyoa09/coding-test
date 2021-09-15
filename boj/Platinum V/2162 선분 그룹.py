from sys import stdin
from collections import deque
stdin = open('in.txt','r')
input = stdin.readline

class ftn:
    def __init__(self,arr):
        self.arr= arr

    def ccw(self,x1,y1,x2,y2,x3,y3):
        tmp= (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
        if tmp> 0:
            return 1
        elif tmp < 0:
            return -1
        else:
            return 0

    def connect(self,coord1,coord2):
        x1,y1,x2,y2 = coord1
        x3,y3,x4,y4 = coord2
        answer=0
        didanswer=False

        if self.ccw(x1,y1,x2,y2,x3,y3) * self.ccw(x1,y1,x2,y2,x4,y4)==0 and self.ccw(x3,y3,x4,y4,x1,y1) * self.ccw(x3,y3,x4,y4,x2,y2)==0:
            didanswer=True
            if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
                answer=1
        if self.ccw(x1,y1,x2,y2,x3,y3) * self.ccw(x1,y1,x2,y2,x4,y4)<=0 and self.ccw(x3,y3,x4,y4,x1,y1) * self.ccw(x3,y3,x4,y4,x2,y2)<=0:
            if not didanswer:
                answer=1
        return answer

N = int(input())
sol = ftn([tuple(map(int,input().split(' '))) for _ in range(N)])
maps = [[] for _ in range(N)]

for i in range(N):
    for j in range(i):
        if sol.connect(sol.arr[i],sol.arr[j]):
            maps[i].append(j)
            maps[j].append(i)

group_cnt = 0
ans = -1
visited = [False] * N

for i in range(N):
    if not visited[i]:
        que = deque([i])
        cnt = 0
        while que:
            tmp = que.popleft()
            if not visited[tmp]:
                visited[tmp] = True
                cnt +=1 
                for v in maps[tmp]:
                    if not visited[v]:
                        que.append(v)
        group_cnt += 1
        if cnt > ans:
            ans = cnt

print(group_cnt)
print(ans)