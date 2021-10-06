from sys import stdin
import heapq as hq
stdin = open('in.txt','r')
input = stdin.readline

N,M = map(int,input().strip().split(' '))
maps = [list(input().strip()) for _ in range(N)]
ch = [[[False] * M for _ in range(N)] for _ in range(2**8)]
end = {}
for r in range(N):
    for c in range(M):
        end[(r,c)] = False
        if maps[r][c] == '0':
            que = [(0,r,c,0)]
        elif maps[r][c] == '1':
            end[(r,c)] = True
D = [(1,0),(0,1),(-1,0),(0,-1)]
ch[0][que[0][1]][que[0][2]] = 0
while que:
    cnt,r,c,key = hq.heappop(que)
    if end[(r,c)]:
        print(cnt)
        break
    else:
        for dx,dy in D:
            px,py = r+dx,c+dy
            if 0<=px<N and 0<=py<M and maps[px][py] != '#':
                if maps[px][py] in ['.','0','1'] and (not ch[key][px][py] or ch[key][px][py] > cnt + 1):
                    ch[key][px][py] = cnt + 1
                    hq.heappush(que,(cnt+1,px,py,key))
                elif 97<=ord(maps[px][py])<=102:
                    tmp_key = 1<<(ord(maps[px][py])-96)
                    tmp_key = (tmp_key|key) if key & tmp_key == 0 else key
                    if not ch[tmp_key][px][py] or ch[tmp_key][px][py] > cnt + 1:
                        ch[tmp_key][px][py] = cnt + 1
                        hq.heappush(que,(cnt+1,px,py,tmp_key))
                elif 65<=ord(maps[px][py])<=70:
                    tmp = 1<<(ord(maps[px][py])-64)
                    if tmp & key != 0 and (not ch[key][px][py] or ch[key][px][py] > cnt + 1):
                        ch[key][px][py] = cnt + 1         
                        hq.heappush(que,(cnt+1,px,py,key))        
else:
    print(-1)