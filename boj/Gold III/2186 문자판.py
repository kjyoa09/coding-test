from sys import stdin
from collections import defaultdict
stdin = open('in.txt','r')
input = stdin.readline

N,M,K = map(int,input().strip().split(' '))
maps = [list(input().strip()) for _ in range(N)]
dic = defaultdict(list)

for r in range(N):
    for c in range(M):
        dic[maps[r][c]].append((r,c))

wanted = input().strip()
