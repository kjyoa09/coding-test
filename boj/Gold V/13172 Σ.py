import sys
from math import gcd
sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())
mod = 1_000_000_007
def pow(x,y):
    if y==1:
        return x
    else:
        if y%2 == 1:
            return x * pow(x,y-1)%mod
        tmp = pow(x,y//2)
        return tmp*tmp%mod
ans = 0
for _ in range(N):
    n,s = map(int,sys.stdin.readline().rstrip().split())
    g = gcd(n,s)
    n //= g;s //= g
    ans += s*pow(n,mod-2)
    ans %= mod
print(ans)