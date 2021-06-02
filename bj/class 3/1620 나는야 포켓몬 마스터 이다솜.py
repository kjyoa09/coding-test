import sys
from collections import defaultdict

dic1 = defaultdict(int)
dic2 = defaultdict(str)

n,m = map(int,sys.stdin.readline().strip().split())


for i in range(n):
    tmp = sys.stdin.readline().strip()
    dic1[tmp] = i+1
    dic2[i+1] = tmp

for i in range(m):
    tmp = sys.stdin.readline().strip()
    if tmp.isdecimal():
        print(dic2[int(tmp)])
    else:
        print(dic1[tmp])
