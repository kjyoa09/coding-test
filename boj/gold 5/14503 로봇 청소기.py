from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N,M = map(int,input().rstrip().split())
r,c,d = map(int,input().rstrip().split())
maps = [list(map(int,input().rstrip().split())) for _ in range(N)]
ch = []
for i in maps:
    ch += [[True if x == 0 else False for x in i]]

ro = {0:[-1,0],1:[0,1],2:[1,0],3:[0,-1]}
def turn(d):
    if d-1 <0:
        return 3
    else:
        return d-1
ans = 0
while 1:
    if maps[r][c] == 0 and ch[r][c]:
        ans +=1
        ch[r][c] = False

    for _ in range(4):
        d = turn(d)
        pr,pc = r+ro[d][0],c+ro[d][1]
        if 0<= pr < N and 0<= pc < M and ch[pr][pc] and maps[pr][pc] == 0:
            r,c = pr,pc
            break
    else:
        tmp = abs(d+2)%4
        pr,pc = r+ro[tmp][0],c+ro[tmp][1]
        if 0<= pr < N and 0<= pc < M and maps[pr][pc] == 0:
            r,c = pr,pc
        else:
            break
print(ans)
