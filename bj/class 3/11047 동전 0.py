import sys


n,k = map(int,sys.stdin.readline().split())
arr = []
for i in range(n):
    tmp = sys.stdin.readline().split()
    tmp = int(tmp[0])

    if tmp <= k:
        arr += [tmp]
    else:
        break
arr = arr[::-1]
ans = 0

for i in arr:
    a,k = divmod(k,i)
    ans += a
print(ans)
