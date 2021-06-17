import sys
sys.stdin = open("in.txt")
a,b = map(int,input().split())
fac = [1]
for i in range(1,a+1):
    fac += [fac[-1]*i]
tmp = fac[a]//fac[b]//fac[a-b]
print(tmp %10007)