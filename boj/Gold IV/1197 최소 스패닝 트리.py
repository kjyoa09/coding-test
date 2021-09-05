# find(s) != find(e)일 때까지 while돌려줘야함[중요]
# 문제 자체는 1647 도시 분할 계획이랑 비슷
from sys import stdin
import heapq as hq
stdin = open("in.txt","r")
V,E = map(int,stdin.readline().rstrip().split())
dic = []
for _ in range(E):
    s,e,v = map(int,stdin.readline().rstrip().split())
    hq.heappush(dic,(v,s,e))

arr = list(range(V+1))

def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx])
    return arr[idx]
def union(s,e):
    ro1 = find(s);ro2 = find(e)
    arr[ro1] = ro2
ans = 0
for _ in range(V-1):
    while 1:
        v,s,e = hq.heappop(dic)
        if find(arr[s]) != find(arr[e]):
            break
    union(s,e)
    find(e);find(s) 
    ans +=v
print(ans)