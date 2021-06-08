# 크루스칼 알고리즘 : N개의 도시를 최소한의 간선(N-1)로 연결.
# 간선이 N-2이면 2개의 그룹
from sys import stdin
import heapq as hq
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())

arr = list(range(N+1))
def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx]) 
    return arr[idx]
def union(u,v):
    root1 = find(u)
    root2 = find(v)
    arr[max(root1,root2)] = min(root1,root2)

total = 0
dic = []
for _ in range(M):
    s,e,v = map(int,stdin.readline().rstrip().split())
    total += v
    hq.heappush(dic,(v,s,e))
ans = 0
for _ in range(N-2):
    while 1:
        v,s,e = hq.heappop(dic)
        if find(arr[s]) != find(arr[e]):
            break
    union(e,s)
    find(e);find(s)    
    ans += v
print(ans)
