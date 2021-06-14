from sys import stdin
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())
A = list(map(int,stdin.readline().rstrip().split()))
C = list(map(int,stdin.readline().rstrip().split()))
Sc = sum(C)
maps = [[0] * (Sc+1) for _ in range(N)] 

for i in range(N):
    for j in range(Sc+1):
        if i == 0:
            if j >= C[i]:
                maps[i][j] = A[i]
        else:
            if j-C[i] >= 0:
                maps[i][j] = max(maps[i-1][j],maps[i-1][j-C[i]] +A[i])
            else:
                maps[i][j] = maps[i-1][j]
for idx,v in enumerate(maps[-1]):
    if v >= M:
        print(idx)
        break
