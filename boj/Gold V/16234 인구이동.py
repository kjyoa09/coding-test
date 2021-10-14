from sys import stdin
from collections import deque
stdin = open('in.txt')
input = stdin.readline

N,L,R = map(int,input().strip().split(' '))
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]
cnt = 0
dx,dy = [1,0,-1,0],[0,1,0,-1]

def bfs(st,ch):
    que = deque([st])
    visited = [st]
    count,tot = 0,0    
    while que:
        r,c = que.popleft()
        tot += maps[r][c]
        count += 1
        for idx in range(4):
            pr,pc = r+dx[idx],c+dy[idx]
            if 0<=pr<N and 0<=pc<N and not ch[pr][pc] and L<=abs(maps[r][c] - maps[pr][pc]) <= R:
                visited.append((pr,pc))
                que.append((pr,pc))
                ch[pr][pc] = True
    return count,tot,visited,ch

while 1:
    dic,ch = {},[[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not ch[r][c]:
                ch[r][c] = True
                count,tot,visited,ch = bfs((r,c),ch)
                if count != 1:
                    dic[len(dic)] = (visited,tot,count)
    if len(dic) == 0:
        print(cnt)
        break
    else:
        for visited,tot,count in dic.values():
            val = tot//count
            for xx,yy in visited:
                maps[xx][yy] = val
        cnt += 1       

    # for x in maps:
    #     print(x)
    # print()    