from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
N,M,x,y,K = map(int,input().strip().split(' '))
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]
sq,D = [0] * 6,{1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}

for c in map(int,input().strip().split(' ')):
    if 0<=x+D[c][0]<N and 0<=y+D[c][1]<M:
        x+=D[c][0]
        y+=D[c][1]
        if c == 1:
            sq = [sq[3],sq[1],sq[0],sq[5],sq[4],sq[2]]
        elif c == 2:
            sq = [sq[2],sq[1],sq[5],sq[0],sq[4],sq[3]]
        elif c == 3:
            sq = [sq[4],sq[0],sq[2],sq[3],sq[5],sq[1]]
        else:
            sq = [sq[1],sq[5],sq[2],sq[3],sq[0],sq[4]]

        print(sq[0])     
        if maps[x][y]:
            sq[-1] = maps[x][y]
            maps[x][y] = 0
        else:
            maps[x][y] = sq[-1]
    