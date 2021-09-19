from sys import stdin
import heapq as hq
stdin = open('in.txt','r')
input = stdin.readline
input()
A = list(map(int,input().strip().split(' ')))
A = [-x for x in A]
B = list(map(int,input().strip().split(' ')))
hq.heapify(A)
hq.heapify(B)

ans = 0
while A:
    ans -= hq.heappop(A) * hq.heappop(B)
print(ans)