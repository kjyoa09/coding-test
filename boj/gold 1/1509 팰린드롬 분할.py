from sys import stdin
stdin = open("in.txt")
st = list(stdin.readline().rstrip())
L = len(st) 
maps = [[0 for _ in range(L)] for _ in range(L)]
for i in range(L):
    maps[i][i] = 1
for i in range(L-1):
    if st[i] == st[i+1]:
        maps[i][i+1] = 1
for l in range(3,L+1): # 길이
    for s in range(L-l+1):
        e = s+l-1
        if maps[s+1][e-1] == 1 and st[s]==st[e]:
            maps[s][e] = 1
dp = [1] + [0] * L
for i in range(1,L):
    if maps[0][i]:
        dp[i] = 1
    else:
        dp[i] = dp[i-1]+1
        for j in range(1,i):
            if maps[j][i]:
                dp[i] = min(dp[i],dp[j-1] + 1)
print(dp[L-1])