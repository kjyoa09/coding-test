from sys import stdin
import heapq as hq
stdin = open("in.txt")
input = stdin.readline
N = int(input())
arr = [list(map(int,input().rstrip().split()))+[_] for _ in range(N)]
que = []
arr.sort(key=lambda x:x[0])
for a in range(1,N):
    cost = min([abs(arr[a-1][i] - arr[a][i]) for i in range(3)])
    hq.heappush(que,(cost,arr[a][-1],arr[a-1][-1]))
arr.sort(key=lambda x:x[1])
for a in range(1,N):
    cost = min([abs(arr[a-1][i] - arr[a][i]) for i in range(3)])
    hq.heappush(que,(cost,arr[a][-1],arr[a-1][-1]))
arr.sort(key=lambda x:x[2])
for a in range(1,N):
    cost = min([abs(arr[a-1][i] - arr[a][i]) for i in range(3)])
    hq.heappush(que,(cost,arr[a][-1],arr[a-1][-1]))
check = [i for i in range(N)]
def find(idx):
    if check[idx] != idx:
        check[idx] = find(check[idx])
    return check[idx]
def union(idx1,idx2):
    ro1 = find(idx1);ro2 = find(idx2)
    check[ro2] = ro1
ans = 0
cnt = 0
while 1:
    cost,s,e = hq.heappop(que)
    if find(check[s]) != find(check[e]):
        union(s,e)
        find(s),find(e)
        ans += cost
        cnt += 1
    if cnt == N-1:
        break
print(ans)
