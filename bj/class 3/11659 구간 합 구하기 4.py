import sys

input = sys.stdin.readline

n,m = map(int,input().split())

arr = list(map(int,input().split()))
li = [0]
for i in arr:
    li += [li[-1] + i]


for _ in range(m):
    s,e = map(int,input().split())
    print(li[e] - li[s-1])
