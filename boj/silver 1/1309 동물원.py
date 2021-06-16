N = int(input())
dp = [1,1,1] 
for i in range(N-1):
    dp = [sum(dp)%9901,(dp[0] + dp[1])%9901,(dp[0] + dp[2])%9901]
print(sum(dp)%9901)