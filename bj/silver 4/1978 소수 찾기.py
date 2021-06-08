import sys
ch = [False] * 2 + [True] * 999

for i in range(2,1001):
    if ch[i]:
        for n in range(i+i,1001,i):
            ch[n] = False

_ = input()
arr = list(map(int,sys.stdin.readline().split()))
ans = 0
for i in arr:
    if ch[i]:
        ans += 1
print(ans)
