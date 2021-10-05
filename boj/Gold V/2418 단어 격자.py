from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

h,w,l = map(int,input().strip().split(' '))
maps = [list(input().strip()) for _ in range(h)]
ch = [[[0] * w for _ in range(h)] for _ in range(l)]
D = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
want = list(input().strip())



for ll in range(l):
    for r in range(h):
        for c in range(w):
            if ll == 0:
                if maps[r][c] == want[ll]:
                    ch[ll][r][c] = 1
            else:
                for dx,dy in D:
                    if 0<=r + dx <h and 0<=c + dy <w and maps[r][c] == want[ll]:
                        ch[ll][r][c] += ch[ll-1][r+dx][c+dy]


print(sum(sum([x for x in ch[-1]],[])))