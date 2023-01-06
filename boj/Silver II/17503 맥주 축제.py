# https://www.acmicpc.net/problem/17503

import sys
from heapq import *

# sys.stdin = open('in.txt')
input = sys.stdin.readline
# n,m,k = map(int,sys.stdin.readline().rstrip().split())
# print(n,m,k)

n,m,k = map(int,input().rstrip().split())

arr = []
for i in range(k):
    # v,c = map(int,sys.stdin.readline().rstrip().split())
    v,c = map(int,input().rstrip().split())
    heappush(arr,(c,v)) # 도수 오름차순으로 heapq 생성

res = []
ans = 0

while arr:
    c,v = heappop(arr)
    ans += v
    
    if ans >= m:
        print(c)
        break
    
    else :
        heappush(res,(v,c)) # 만족도 오름차순으로 heappush
    
    if len(res) == n:
        v,c = heappop(res)
        ans -= v 

if len(arr) == 0 :print(-1)