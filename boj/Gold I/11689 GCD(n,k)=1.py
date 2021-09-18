from sys import stdin
from math import sqrt

def dfs(n,st):
    for num in range(st,int(sqrt(n))+1):
        if n % num == 0:
            po = 1
            while n % (num ** (po + 1)) == 0:
                po += 1
            return [(num,po)] + dfs(n//(num**po),num+1) if n//(num**po) != 1 else [(num,po)]
    else:
        return [(n,1)]

stdin = open('in.txt','r')
n = int(stdin.readline())

if n == 1:
    print(1)
else:
    arr = dfs(n,2)
    ans = 1
    for a in arr:
        ans *= a[0]**(a[1]-1)*(a[0]-1)
    print(ans)