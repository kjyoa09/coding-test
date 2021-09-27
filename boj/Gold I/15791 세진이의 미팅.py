from sys import stdin
stdin = open('in.txt','r')

MOD = 1_000_000_007

def fac(n):
    re = 1
    for i in range(2,n+1):
        re = (re*i)%MOD
    return re

def pow(A,p):
    if p == 0:
        return 1
    elif p%2:
        return (A * (pow(A,p//2)**2)) % MOD    
    else:
        return (pow(A,p//2)**2) % MOD

N,K = map(int,stdin.readline().split(' '))

print(((fac(N)%MOD) * pow(fac(K)%MOD,MOD - 2)* pow(fac(N-K)%MOD,MOD - 2)) % MOD)
