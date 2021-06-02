import sys
n = int(sys.stdin.readline())
ans = []
for i in range(n):
    a = sys.stdin.readline()
    ans += [int(a)]

ans.sort()
for i in ans:
    print(i)
