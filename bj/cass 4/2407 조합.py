import sys

sys.stdin = open("in.txt")

n,m = map(int,sys.stdin.readline().rstrip().split())


fac = [1]

for i in range(2,n+1):
    fac += [fac[-1]*i]


print(fac[n-1]//fac[m-1]//fac[n-m-1])