from sys import stdin
stdin = open("in.txt","r")
N,K = map(int,stdin.readline().rstrip().split())
fac = [1]
for i in range(1,N+K):
    fac += [fac[-1]*i]
print((fac[N+K-1]//(fac[K-1]*fac[N]))%1000000000)
