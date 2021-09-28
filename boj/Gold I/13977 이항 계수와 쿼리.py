from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
MOD = 1_000_000_007
fac = [1,1]
for i in range(2,4000000+1):
    fac.append((fac[-1]*i)%MOD)
def pow(A,p):
    if p == 0:
        return 1
    elif p%2:
        return (A * (pow(A,p//2)**2)) % MOD    
    else:
        return (pow(A,p//2)**2) % MOD


for _ in range(int(input())):
    N,K = map(int,input().strip().split(' '))
    print(((fac[N]%MOD) * pow(fac[K]%MOD,MOD-2)*pow(fac[N-K]%MOD,MOD - 2)) % MOD)
