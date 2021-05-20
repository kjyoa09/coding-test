# 어디서 틀렸을까...

import sys
from math import log


sys.stdin = open("in.txt")

n = int(sys.stdin.readline())

maps = []
for num in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))


m=0;z=0;o=0
k = int(log(n,3))

def dfs(a,b,c,d,k):
    global m,z,o
    print(a,b,c,d,k)
    tmp = []
    for i in range(a,b):     
        for j in range(c,d):
            if maps[i][j] == -1:
                tmp += [n]
            else:
                tmp += [maps[i][j]]
    
    if sum(tmp) == 0:
        z += 1
    elif sum(tmp) == len(tmp):
        o += 1
    elif sum(tmp) == len(tmp) * n:
        m += 1
    else:
        tmp = 3**(k-1)
        dfs(a,      a+tmp  ,c,c+tmp,k-1)
        dfs(a+tmp,  a+2*tmp,c,c+tmp,k-1)
        dfs(a+2*tmp,a+3*tmp,c,c+tmp,k-1)
        
        dfs(a      ,a+tmp,  c+tmp,c+2*tmp,k-1)
        dfs(a+tmp  ,a+2*tmp,c+tmp,c+2*tmp,k-1)
        dfs(a+2*tmp,a+3*tmp,c+tmp,c+2*tmp,k-1)

        dfs(a      ,a+tmp,  c+2*tmp,c+3*tmp,k-1)
        dfs(a+tmp  ,a+2*tmp,c+2*tmp,c+3*tmp,k-1)
        dfs(a+2*tmp,a+3*tmp,c+2*tmp,c+3*tmp,k-1)



dfs(0,n,0,n,k)

print(m)
print(z)
print(o)
