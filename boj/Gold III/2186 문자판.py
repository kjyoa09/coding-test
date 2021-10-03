from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

N,M,K = map(int,input().strip().split(' '))
maps = [list(input().strip()) for _ in range(N)]
wanted = list(input().strip())

L = len(wanted)
ch = [[[0]*M for _ in range(N)] for _ in range(L)]
for r in range(N):
    for c in range(M):
        if maps[r][c] == wanted[0]:
            ch[0][r][c] = 1

for l in range(1,L):
    for r in range(N):
        for c in range(M):
            if maps[r][c] == wanted[l]:
                for k in range(1,K+1):
                    if 0<=r-k<N:
                        ch[l][r][c] += ch[l-1][r-k][c]
                    if 0<=r+k<N:
                        ch[l][r][c] += ch[l-1][r+k][c]
                    if 0<=c-k<M:
                        ch[l][r][c] += ch[l-1][r][c-k]
                    if 0<=c+k<M:
                        ch[l][r][c] += ch[l-1][r][c+k]

print(sum(sum([x for x in ch[-1]],[])))