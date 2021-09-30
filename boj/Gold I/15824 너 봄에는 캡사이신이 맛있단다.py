from sys import stdin
stdin = open('in.txt')
input = stdin.readline
N = int(input())
arr = list(map(int,input().strip().split(' ')))
arr.sort()


MOD = 1_000_000_007
sq = [1]

for _ in range(N):
    sq.append((sq[-1]*2)%MOD)
ans = 0
for i in range(N-1,-1,-1):
    ans += ((sq[i] - sq[N-i-1]) * arr[i])%MOD
print(ans%MOD)
