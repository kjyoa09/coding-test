## pypy 로는 통과(python 3은 시간 초과)

import sys
sys.stdin = open("in.txt","r")
R,C,T = map(int,sys.stdin.readline().rstrip().split())
maps = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(R)]

clean = [(i,0) for i in range(R) if maps[i][0] == -1]

dx = [1,0,-1,0];dy = [0,1,0,-1]
def dust():
    ch = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if maps[r][c] > 0 :
                n = 0;v = maps[r][c]
                for i in range(4):
                    if 0 <= r + dx[i] <R and 0<=c + dy[i]<C and maps[r + dx[i]][c + dy[i]] != -1:
                        n+=1
                        ch[r + dx[i]][c + dy[i]] += v//5
                ch[r][c] += v - (v//5) * n
    return ch

def rotate():
    x1,y1 = clean[0];x2,y2 = clean[1]
    ch = [i[:] for i in maps]
    for i in range(1,C): # R R
        ch[x1][i] = maps[x1][i-1]
        ch[x2][i] = maps[x2][i-1]
    for i in range(x1-1,-1,-1): # U
        ch[i][C-1] = maps[i+1][C-1]
    for i in range(C-2,-1,-1): # L
        ch[0][i] = maps[0][i+1]
    for i in range(1,x1): # D
        ch[i][0] = maps[i-1][0]

    for i in range(x2+1,R): #D
        ch[i][C-1] = maps[i-1][C-1]
    for i in range(C-2,-1,-1): #L
        ch[R-1][i] = maps[R-1][i+1]
    for i in range(R-2,x2,-1): #U
        ch[i][0] = maps[i+1][0]
    ch[x1][y1] = -1
    ch[x2][y2] = -1
    return ch

for _ in range(T):
    maps = dust()
    maps = rotate()

print(sum([y for x in maps for y in x])+ 2)