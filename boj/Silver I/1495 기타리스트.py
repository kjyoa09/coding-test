# 0~M 까지 배열 만들어서 메모리 초과 방지
from sys import stdin
stdin = open("in.txt","r")
N,S,M = map(int,stdin.readline().rstrip().split())
arr = list(map(int,stdin.readline().rstrip().split()))
tmp = [-1]*(M+1)
tmp[S] = S
for a in arr:
    re = [-1]*(M+1)
    for t in tmp :
        if t != -1:
            if t-a >=0:
                re[t-a] = t-a
            if t+a <= M:
                re[t+a] = t+a
    tmp = re
for t in tmp[::-1]:
    if t!=-1:
        print(t)
        break
else:
    print(-1)