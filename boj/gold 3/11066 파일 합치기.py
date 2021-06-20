from sys import stdin
stdin = open("in.txt","r")
T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    arr = list(map(int,stdin.readline().rstrip().split()))
    maps = [[float("INF")] * N for _ in range(N)]
    ch = [[sum(arr[:i+1]) for i in range(N)]]
    for i in range(N):
        maps[i][i] = arr[i]
        if i > 0:
            ch += [[x-arr[i-1] for x in ch[-1]]]


    for i in range(1,N): #Length
        for S in range(N-i): # 시작점
            for tmp in range(S,S+i):
                a = 0
                if S != tmp:
                    a += maps[S][tmp]
                if tmp +1 != S+i:
                    a += maps[tmp+1][S+i]
                if maps[S][S+i] > a:
                    maps[S][S+i] = a
            maps[S][S+i] += ch[S][S+i]
    print(maps[0][-1])