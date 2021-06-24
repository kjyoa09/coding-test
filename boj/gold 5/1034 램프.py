from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N,M = map(int,input().rstrip().split())
maps = [list(map(int,list(input().rstrip())))for _ in range(N)]
K = int(input())
ans = 0
for nn in range(N):
    zero = sum(1 for x in maps[nn] if x == 0)
    if zero <= K and zero%2 == K%2:
        tmp = 0
        for r in range(N):
            if maps[nn] == maps[r]:
                tmp +=1
        if ans < tmp:
            ans = tmp
print(ans)