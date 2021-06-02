import sys

n = int(sys.stdin.readline())
ans = [1,1,1]
for i in range(100):
    ans += [ans[-3] + ans[-2]]


for _ in range(n):
    tmp = int(sys.stdin.readline())
    print(ans[tmp-1])
