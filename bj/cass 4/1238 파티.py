# 다익스트라
import sys,heapq as hq

sys.stdin = open("in.txt","r")

N,M,X = map(int,sys.stdin.readline().rstrip().split())

dic = {i:[] for i in range(1,N+1)}

for _ in range(M):
    s,e,v = map(int,sys.stdin.readline().rstrip().split())
    dic[s].append((v,e))

inf = float("INF")

def find(start):
    que = [(0,start)]
    check = [True] * (N+1);visit = [inf] * (N + 1)
    visit[start] = 0; check[start] = True
    while que:
        cost,start = hq.heappop(que)
        if check[start]:
            check[start] = False
            for c,s in dic[start]:
                if visit[s] > c + cost:
                    visit[s] = c + cost
                    hq.heappush(que,(c+cost,s))
    return visit
ans = find(X)
for i in range(1,N+1):
    ans[i] += find(i)[X]
print(max(ans[1:]))
