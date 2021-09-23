# 진짜 하나하나 구현함..
# 숏코딩은 어디까지 줄이려나;
from sys import stdin
from collections import deque
stdin = open('in.txt','r')
input = stdin.readline

R,C = map(int,input().strip().split(' '))
dic,st = {},{}
maps = [list(input().strip()) for _ in range(R)]
ch,dx,dy = [[True] * C for _ in range(R)],[0,1,0,-1],[1,0,-1,0]

for r in range(R):
    for c in range(C):
        dic[(r,c)] = maps[r][c]
        if maps[r][c] == 'M' or maps[r][c] == 'Z':
            st[maps[r][c]] = (r,c)
que = deque([])

for idx in range(4):
    px,py = st['M'][0]+dx[idx],st['M'][1]+dy[idx]
    if 0<=px<R and 0<=py<C and dic[(px,py)] != '.':
        que.append((px,py))
        break
if len(que) == 0:
    for idx in range(4):
        px,py = st['Z'][0]+dx[idx],st['Z'][1]+dy[idx]
        if 0<=px<R and 0<=py<C and dic[(px,py)] != '.':
            que.append((px,py))
            break
if len(que) == 0:
    if st['M'][0] == st['Z'][0]:
        print(*[st['M'][0],min(st['Z'][1],st['M'][1])+1,'-'])
    else:
        print(*[min(st['Z'][0],st['M'][0])+1,st['M'][1],'|'])

else:
    find = False
    while que:
        x,y = que.popleft()
        ch[x][y] = False
        if dic[(x,y)] == 'M' or dic[(x,y)] == 'Z':
            for idx in range(4):
                px,py = x+dx[idx],y+dy[idx]
                if 0<=px<R and 0<=py<C and dic[(px,py)] != '.':
                    que.append((px,py))
        else:
            if dic[(x,y)] == '+':
                for idx in range(4):
                    px,py = x+dx[idx],y+dy[idx]
                    if 0<=px<R and 0<=py<C and dic[(px,py)] != '.' and ch[px][py]:
                        que.append((px,py))
                    if 0<=px<R and 0<=py<C and dic[(px,py)] == '.':
                        coord = (px,py)
                        find = True
            elif dic[(x,y)] == '-':
                (px,py) = (x,y-1) if 0<=y-1<C and ch[x][y-1] else (x,y+1)
            elif dic[(x,y)] == '|':
                (px,py) = (x-1,y) if 0<=x-1<R and ch[x-1][y] else (x+1,y)

            elif dic[(x,y)] == '1':
                (px,py) = (x+1,y) if 0<=x+1<R and ch[x+1][y] else (x,y+1)
            elif dic[(x,y)] == '2':
                (px,py) = (x-1,y) if 0<=x-1<R and ch[x-1][y] else (x,y+1)
            elif dic[(x,y)] == '3':
                (px,py) = (x-1,y) if 0<=x-1<R and ch[x-1][y] else (x,y-1)
            elif dic[(x,y)] == '4':
                (px,py) = (x+1,y) if 0<=x+1<R and ch[x+1][y] else (x,y-1)
        
            if dic[(px,py)] == '.':
                coord = (px,py)
                find = True
            else : 
                que.append((px,py))
        if find:
            break
    ans = []
    for idx in range(4):
        px,py = coord[0]+dx[idx],coord[1]+dy[idx]
        if 0<=px<R and 0<=py<C :
            if idx==0 and dic[(px,py)] in ['-','3','4','+']:
                ans.append(0)
            if idx==1 and dic[(px,py)] in ['|','2','3','+']:
                ans.append(1)
            if idx==2 and dic[(px,py)] in ['-','1','2','+']:
                ans.append(2)
            if idx==3 and dic[(px,py)] in ['|','1','4','+']:
                ans.append(3)
    if len(ans) == 4:
        print(*[coord[0]+1,coord[1]+1,'+'])
    if ans == [0,1] :
        print(*[coord[0]+1,coord[1]+1,'1'])
    if ans == [0,2] :
        print(*[coord[0]+1,coord[1]+1,'-'])
    if ans == [0,3] :
        print(*[coord[0]+1,coord[1]+1,'2'])
    if ans == [1,2] :
        print(*[coord[0]+1,coord[1]+1,'4'])
    if ans == [1,3] :
        print(*[coord[0]+1,coord[1]+1,'|'])
    if ans == [2,3] :
        print(*[coord[0]+1,coord[1]+1,'3'])
