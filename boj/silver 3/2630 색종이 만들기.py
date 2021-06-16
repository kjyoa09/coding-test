import sys
from collections import defaultdict


n = int(sys.stdin.readline().strip())
maps = []

for i in range(n):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    maps += [tmp]

def div(arr):
    leng = len(arr)//2

    re = [[],[],[],[]]

    for i in range(leng*2):
        if i < leng:
            re[0] += [arr[i][:leng]]
            re[1] += [arr[i][leng:]]
        else:
            re[2] += [arr[i][:leng]]
            re[3] += [arr[i][leng:]]
    return re
ans = [0,0]
def check(arr):
    global ans

    tmp = [y for x in arr for y in x]

    if len(set(tmp)) == 1:
        ans[tmp[0]] += 1
    else:
        re = div(arr)
        for i in re:
            check(i)
    
check(maps)

for i in ans:
    print(i)
