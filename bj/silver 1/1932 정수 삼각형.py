import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr += [list(map(int,input().split()))]
now = arr.pop()
while arr:
    tmp = arr.pop()
    p = []
    for i in range(len(tmp)):
        p += [max(tmp[i] + now[i],tmp[i] + now[i + 1])]
    now = p
print(now[0])
