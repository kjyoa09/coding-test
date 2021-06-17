from sys import stdin
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())
maps = [list(map(int,stdin.readline().rstrip().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        tmp = [0]
        if 0<=c-1<M :
            tmp += [check[r][c-1]]
        if 0<=r-1<N :
            tmp += [check[r-1][c]]
        if 0<=c-1<M and 0<=r-1<N:
            tmp += [check[r-1][c-1]]
        check[r][c] = max(tmp) + maps[r][c]
print(check[-1][-1])