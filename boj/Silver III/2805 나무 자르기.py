import sys


n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

lt = 0 ;rt = max(arr)

ans = -1
while lt <= rt:
    mid = (lt + rt)//2
    tmp = [x - mid for x in arr if x > mid]

    if sum(tmp) < m :
        rt = mid - 1
    else:
        lt = mid + 1
        if ans < mid:
            ans = mid
print(ans)
