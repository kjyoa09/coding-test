from sys import stdin
from math import factorial as fac

stdin = open('in.txt')
input = stdin.readline

N = int(input())
K = int(input())

if N//2 < K:
    print(0)
else:
    a = fac(N//2)
    b = fac(K)
    c = fac(K - N//2 if K > N//2 else N//2 - K)

    print((a//b)//c*2 % 1_000_000_003 )

