import sys
_ = int(input())
arr = list(map(int,sys.stdin.readline().split()))
li = [arr.pop(0)]
ans = -1
while arr:
    tmp = arr.pop(0)
    if li[-1] < tmp:
        li += [tmp]
        if len(arr) == 0:
            if li[-1] - li[0] > ans:
                ans = li[-1] - li[0]
    else:
        if li[-1] - li[0] > ans:
            ans = li[-1] - li[0]
        li = [tmp]
       
if ans == -1:
    print(0)
else:
    print(ans)

