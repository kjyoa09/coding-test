import bisect,sys
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [arr[0]]

for i in range(1,N):
    idx = bisect.bisect_left(dp,arr[i])
    if len(dp) == idx:
        dp += [arr[i]]
    else:
        dp[idx] = arr[i]
print(dp)