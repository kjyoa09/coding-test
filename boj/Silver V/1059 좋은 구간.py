from sys import stdin
import heapq as hq
stdin = open('in.txt','r')
input = stdin.readline

L = int(input())
S = list(map(int,input().strip().split(' ')))
n = int(input())

if n in S:
    print(0)
else:
    hq.heapify(S)
    tmp = 0
    while S[0]<n:
        tmp = hq.heappop(S)
    print((n-tmp) * (S[0]-n) - 1)