import sys,heapq as hq
sys.stdin = open("in.txt","r")
N,K = map(int,sys.stdin.readline().rstrip().split())
gem = []
for _ in range(N):
    M,V = map(int,sys.stdin.readline().rstrip().split())
    gem += [(-V,M)]
hq.heapify(gem)
bags = []
for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)
bags.sort()
ans = 0
visit = [True] * K
num = 0
while gem:
    v,m = hq.heappop(gem)
    for i in range(K):
        if visit[i] and bags[i] >= m:
            visit[i] = False
            ans -=v
            num+=1
            break
    if num == K:
        break
print(ans)