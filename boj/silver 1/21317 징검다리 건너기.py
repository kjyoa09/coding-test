# 예외처리
# 특이한 CASE : ex) N == 1 >> 0 N<=3 : 매우 큰 점프 할 수 없음 

from sys import stdin
stdin = open("in.txt","r")
N = int(stdin.readline())
if N == 1:
    print(0)
else:
    maps = [()]
    for _ in range(N-1):
        s,b = map(int,stdin.readline().rstrip().split())
        maps.append((s,b))
    K = int(stdin.readline())
    dp = [[0,0]] * (N + 1)
    dp[2] = [maps[1][0],0]
    for num in range(3,N+1):
        tmp = [0,0]
        tmp[0] = min(dp[num-1][0]+maps[num-1][0],dp[num-2][0]+maps[num-2][1])
        if num == 4:
            tmp[1] = K
        elif num == 5:
            tmp[1] = min(dp[num-3][0]+K,dp[num-1][1] + maps[num-1][0])
        elif num >= 6:
            tmp[1] = min(dp[num-3][0]+K,dp[num-1][1] + maps[num-1][0],dp[num-2][1] + maps[num-2][1])
        dp[num] = tmp
    if N <= 3:
        print(dp[-1][0])
    else:
        print(min(dp[-1]))