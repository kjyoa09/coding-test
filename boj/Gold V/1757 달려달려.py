from sys import stdin
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())
maps = [[-1] * (M+1) for _ in range(N+1)]
for i in range(N):
    tmp = int(stdin.readline())
    if i == 0 :
        maps[i][1] = tmp
    else:
        for l in range(1,M+1):
            if l == 1:
                if maps[i][0] != -1:
                    maps[i][l] = maps[i][0] + tmp
                else:
                    maps[i][l] = tmp
            else:
                if maps[i-1][l-1] != -1:
                    maps[i][l] = maps[i-1][l-1] + tmp

    for idx in range(M+1):
        if maps[i][idx] != -1 and 0<= i + idx + 1 < N+1:
            if maps[i + idx + 1][0] < maps[i][idx]:
                maps[i + idx + 1][0] = maps[i][idx]
print(maps[-1][0])
