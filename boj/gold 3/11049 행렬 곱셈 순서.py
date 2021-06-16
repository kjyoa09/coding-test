# 모든 경우의 수를 고려
# ABCD > A BCD, AB CD, ABC D
from sys import stdin
stdin = open("in.txt","r")
N = int(stdin.readline())
arr = []
for _ in range(N):
    a,b = map(int,stdin.readline().rstrip().split())
    arr.append((a,b))
dp = [[0] * N for _ in range(N)]
for i in range(1, N):
    for j in range(N-i):
        row = j ;col = j+i 
        dp[row][col] = dp[row][0] + dp[row+1][col] + arr[row][0] * arr[row+1][0] * arr[col][1]
        for k in range(i): 
            dp[row][col] = min(dp[row][col], dp[row][k+col-i] + dp[1+k+row][col] + arr[row][0] * arr[col][1] * arr[row+k+1][0])
    for i in dp:
        print(i)
print(dp[0][-1])
