# 10 20 999 15
# 이런 수열이 주어지면 10 15 999 가 Return 되는데 
# 길이여서 통과됨...
# 수정해야함 
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