from sys import stdin
import heapq as hq

stdin = open("in.txt","r")
input = stdin.readline

n = int(input())
m = int(input())

maps = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,v = map(int,input().strip().split(' '))
    maps[s].append((v,e))
start,end = map(int,input().strip().split(' '))

cost = [float('inf')] * (n+1)
que = [(0,start,[start])]

ans = {}

while que:
    cnt,st,path = hq.heappop(que)    
    if cost[st] > cnt:
        cost[st] = cnt
        for co,en in maps[st]:
            if cost[en] > co + cnt:
                if en == end:
                    ans[cnt + co] = path + [en]
                hq.heappush(que,(co + cnt,en,path + [en]))
print(cost[end])
print(len(ans[cost[end]]))
print(' '.join(map(str,ans[cost[end]])))