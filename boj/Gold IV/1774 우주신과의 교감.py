# Union Find
# M에서 불필요한 간선이 있을 경우 조심
# 그런데 왜 틀렸습니다. 가 아니라 Index에러지;;
from sys import stdin
import heapq as hq
from math import sqrt
stdin = open('in.txt','r')
input = stdin.readline

N,M = map(int,input().strip().split(' '))
arr = list(range(N))

def dis(coord1,coord2):
    x1,y1 = coord1
    x2,y2 = coord2
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx])
    return arr[idx]

def union(idx1,idx2):
    if idx1 > idx2:
        arr[idx1] = idx2
    else:
        arr[idx2] = idx1

dic = {}

for n in range(N):
    dic[n] = tuple(map(int,input().strip().split(' ')))

que = []
for n in range(N):
    for nn in range(n+1,N):
        hq.heappush(que,(dis(dic[n],dic[nn]),n,nn))

for _ in range(M):
    a,b = map(int,input().strip().split(' '))
    hq.heappush(que,(0,a-1,b-1))

N-=1
ans = 0
while N:
    tmp,idx1,idx2 = hq.heappop(que)
    if find(idx1) != find(idx2):
        union(find(idx1),find(idx2))
        N -= 1
        ans += tmp

print(f'{ans:.2f}')