# https://ko.wikipedia.org/wiki/%ED%8E%98%EB%A5%B4%EB%A7%88%EC%9D%98_%EC%86%8C%EC%A0%95%EB%A6%AC
# 페르마의 소정리
# print(((fac(N)//fac(K))// fac(N-K)) % MOD) 이렇게 하면 안되네;;
# 수학 어렵네;

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
