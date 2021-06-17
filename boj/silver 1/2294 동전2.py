from sys import stdin
stdin = open("in.txt","r")
N,K = map(int,stdin.readline().rstrip().split())
maps = [0] * (K+1)
for _ in range(N):
    n = int(stdin.readline())
    if n > K:
        continue
    maps[n] = 1
    for tmp in range(n,K+1):
        if maps[tmp-n] != 0 :
            if maps[tmp] == 0 or maps[tmp-n]+1 < maps[tmp]:
                maps[tmp] = maps[tmp-n]+1
if maps[-1] == 0:
    print(-1)
else:
    print(maps[-1])