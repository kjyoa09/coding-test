from sys import stdin
from math import floor
input = stdin.readline

n,k,q = map(int,input().strip().split(' '))


def ftn(a,b):
    re = 0
    while a != b:
        while a>b:
            a = int(floor((a-1)/k))
            re +=1
        while a<b:
            b = int(floor((b-1)/k))
            re += 1
    return re

for _ in range(q):
    a,b = map(int,input().strip().split(' '))
    if k == 1:
        print(abs(b-a))
    else:
        print(ftn(a-1,b-1))
