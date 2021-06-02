import sys
from collections import defaultdict

dic = defaultdict(int)
n,m = map(int,sys.stdin.readline().strip().split())
for i in range(n):
    tmp = sys.stdin.readline().strip()
    dic[tmp] = 1
for i in range(m):
    tmp = sys.stdin.readline().strip()
    if tmp in dic:
        dic[tmp]+=1
dic = [(k,v) for k,v in dic.items() if v == 2]

dic.sort(key = lambda x:x[0])

print(len(dic))
for i in dic:
    print(i[0])

