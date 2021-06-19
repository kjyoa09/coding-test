dp = [0,1,3]
for i in range(30):
    dp += [dp[-1] + dp[-2] * 2]
ans = dp[:]
for i in range(3,len(dp)):
    if i%2 == 1:
        ans[i] = (dp[i] + dp[i//2])//2
    else:
        ans[i] = (dp[i] + dp[i//2] + 2 * dp[(i-2)//2])//2
print(ans[4])