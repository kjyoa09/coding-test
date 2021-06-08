from sys import stdin
stdin = open("in.txt")
N,S = map(int,stdin.readline().rstrip().split())
arr = list(map(int,stdin.readline().rstrip().split()))
ans = float("INF")
lt = 0;rt = 0
tmp = arr[0]
while lt <= rt < N:
    if tmp >= S:
        if ans > rt - lt + 1:
            ans = rt - lt + 1
        tmp -= arr[lt]
        lt+=1
    else:
        rt+=1
        if rt < N:
            tmp += arr[rt]
if ans == float("INF"):
    print(0)
else:
    print(ans)
