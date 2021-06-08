import sys

k,n = map(int,input().split())
arr = []
for _ in range(k):
    arr += [int(sys.stdin.readline())]


lt = 1;rt = 2**31

ans = -1
while lt <= rt:
    mid = (lt + rt)//2

    tmp = sum([x//mid for x in arr])

    if tmp < n:
        rt = mid -1
    else:
        lt = mid + 1
        if ans < mid:
            ans = mid
print(ans)
