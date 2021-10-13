from sys import stdin
from collections import defaultdict
stdin = open('in.txt','r')
input = stdin.readline

N,M,K = map(int,input().strip().split(' '))

maps = defaultdict(list)
A = [list(map(int,input().strip().split(' '))) for _ in range(N)]

for _ in range(M):
    a,b,c = map(int,input().strip().split(' '))
    maps[(a-1,b-1)].append(c)
print(4000*4000)
