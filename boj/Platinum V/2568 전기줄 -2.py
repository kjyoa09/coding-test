# LIS(bisect)
# 이어진 값이 주어져서 확인해야함
from sys import stdin
from bisect import bisect_left
stdin = open('in.txt','r')
input = stdin.readline

N = int(input())

arr = []

dic = {}
for _ in range(N):
    x,y = map(int,input().split(' '))
    arr.append((x,y))

arr.sort(key = lambda x:x[0])

re,bi,la = [],[],0
dix = {}
for idx in range(N):
    x,y = arr[idx]
    dix[y] = idx
    if not re:
        re.append(y)
        bi.append(idx-1)        
    else:
        tmp = bisect_left(re,y)
        if tmp == len(re):
            bi.append(dix[re[-1]])
            re.append(y)
            la = idx
        else:
            bi.append(dix[re[tmp-1]])
            re[tmp] = y

used = []
for _ in range(len(re)):
    used.append(arr[la][0])
    la = bi[la]

print(N - len(used))
for x,y in arr:
    if x not in used:
        print(x)