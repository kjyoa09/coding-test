from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline

N = int(input())
maps = [[False] * N for _ in range(N)]
ch = [[False] * N for _ in range(N)]
for _ in range(int(input())):
    r,c = map(int,input().rstrip().split())
    maps[r-1][c-1] = True
dx = [0,1,0,-1];dy = [1,0,-1,0]
di = []
for _ in range(int(input())):
    r,c = input().rstrip().split()
    di.append((int(r),c))
ch[0][0] = True
body = [(0,0)]
ans = 0
d = 0
while 1:
    x,y = body[-1]
    px,py = x+dx[d],y+dy[d]
    if 0<=px<N and 0<=py<N and not ch[px][py]:
        ch[px][py] = True
        body.append((px,py))
        ans += 1 
        if maps[px][py] :
            maps[px][py] = False
        else:
            tmp_x,tmp_y = body.pop(0)
            ch[tmp_x][tmp_y] = False
    else :
        break

    if len(di) > 0 and di[0][0] == ans:
        _,direc = di.pop(0)
        if direc == "D":
            d = (d+1)%4
        else:
            if d == 0:
                d = 3
            else : d-=1
print(ans+1)