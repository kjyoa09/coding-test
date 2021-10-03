from sys import stdin
from collections import deque

input = stdin.readline

maps = [deque(list(input().strip())) for _ in range(4)]


for _ in range(int(input())):
    a,b = map(int,input().strip().split(' '))
    a-=1
    que = deque([])
    if a+1 < 4 and maps[a][2] != maps[a+1][6] :
        que.append((a+1,1,-1*b))
    if a-1 >= 0 and maps[a][6] != maps[a-1][2] :
        que.append((a-1,-1,-1*b))
    maps[a].rotate(b)
    while que:
        now,r,b = que.popleft()
        if r == 1:
            if now+1 < 4 and maps[now][2] != maps[now+1][6]:
                que.append((now+1,1,-1*b))
        else:
            if now-1 >= 0 and maps[now][6] != maps[now-1][2]:
                que.append((now-1,-1,-1*b))
        maps[now].rotate(b)

print(sum(2**i if maps[i][0] == '1' else 0 for i in range(4)))