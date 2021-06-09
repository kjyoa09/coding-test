from sys import stdin
import heapq as hq
stdin = open("in.txt","r")
N = int(stdin.readline())
po = [list(map(float,stdin.readline().rstrip().split())) for _ in range(N)]
dic = []
for i in range(N-1):
    for j in range(i+1,N):
        v = ((po[i][0]-po[j][0])**2+(po[i][1]-po[j][1])**2)**(1/2)
        hq.heappush(dic,(v,i,j))

arr = list(range(N))
def find(idx):
    if arr[idx]!=idx:
        arr[idx] = find(arr[idx])        
    return arr[idx]
def union(s,e):
    ro1 = find(s);ro2 = find(e)
    arr[ro1] = ro2
ans = 0
for _ in range(N-1):
    while 1:
        v,s,e = hq.heappop(dic)
        if find(s) != find(e):
            break
    union(s,e)
    ans +=v
    find(s);find(e)
print(ans)