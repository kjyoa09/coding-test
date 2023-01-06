# https://www.acmicpc.net/problem/17503

import sys
from heapq import *

sys.stdin = open('in.txt')
input = sys.stdin.readline
# print(n,m,k)

n,m,k = map(int,input().rstrip().split())

arr = []
for i in range(k):
    v,c = map(int,input().rstrip().split())
    arr.append((c,v))

def ftn(arr):
    heapify(arr) # 도수 오름차순으로 heapq 생성

    res = []
    ans = 0

    while arr:
        c,v = heappop(arr)
        heappush(res,(v,c))
        ans += v
        
        if ans >= m and len(res) == n:
            return c
            
        if len(res) == n:
            v,c = heappop(res)
            ans -= v 

    return -1
    
print(ftn(arr))