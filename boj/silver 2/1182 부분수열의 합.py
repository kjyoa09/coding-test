from sys import stdin
from collections import defaultdict
stdin = open("in.txt")
input = stdin.readline

N,S = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
dic = defaultdict(int)

tmp = []
for a in arr:
    dic[a] += 1
    if len(tmp):
        for i in range(len(tmp)):
            dic[tmp[i]+a] += 1
            tmp.append(tmp[i]+a)
    tmp.append(a)
print(dic[S])