from sys import stdin
stdin = open("in.txt","r")
N,K = map(int,stdin.readline().rstrip().split())
maps = [1] + [0] * (K)
for _ in range(N):
    n = int(stdin.readline())
    for tmp in range(n,K+1):
        maps[tmp] +=maps[tmp-n]
print(maps[-1])