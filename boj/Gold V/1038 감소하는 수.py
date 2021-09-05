# 전에 추가한 배열 기억해서 맨 앞자리에 1-9들어갈 수 있으면 추가
from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N = 1023
arr = [str(i) for i in range(10)]
ans = [str(i) for i in range(10)]
tmp = [str(i) for i in range(10)]
while N >= len(ans):
    tmpp = []
    for i in arr:
        tmpp.extend([i+x for x in tmp if int(x[0]) < int(i)])
    ans += tmpp
    tmp = tmpp
    if tmp[-1] == "9876543210":
        break
if len(ans) <= N:
    print(-1)
else:
    print(ans[N])