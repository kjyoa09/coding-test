import sys
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

arr = []

for _ in range(n):
    tmp = list(sys.stdin.readline().strip())
    for i in range(n):
        if tmp[i] == "1":
            arr += [(_,i)]

idx = 0
dic = defaultdict(list)
dx = [1,0,-1,0];dy = [0,1,0,-1]
while arr:
    Q = [arr.pop(0)]
    dic[idx] += Q
    while Q:
        tmp = Q.pop(0)
        post = [(tmp[0] + dx[i],tmp[1] + dy[i]) for i in range(4) if (tmp[0] + dx[i],tmp[1] + dy[i]) in arr]
        Q += post
        for i in post:
            arr.remove(i)
        dic[idx] += post
    idx += 1
print(len(dic))
dic = sorted(dic.items(),key = lambda x:len(x[1]))

for i in dic:
    print(len(i[1]))
