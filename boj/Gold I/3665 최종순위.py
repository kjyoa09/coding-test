from sys import stdin
from collections import deque

stdin = open('in.txt','r')
input = stdin.readline


for _ in range(int(input())):
    N = int(input())
    
    A = list(map(int,input().split(' ')))
    maps,dg = [[] for _ in range(N+1)],[0]*(N+1)

    for i in range(N):
        for ii in range(i+1,N):
            maps[A[i]].append(A[ii])
            dg[A[ii]] += 1
    
    for _ in range(int(input())):
        a,b = map(int,input().split(' '))

        if b in maps[a]:
            del maps[a][maps[a].index(b)]
            maps[b].append(a)
            dg[a]+=1
            dg[b]-=1
        else:
            del maps[b][maps[b].index(a)]
            maps[a].append(b)
            dg[a]-=1
            dg[b]+=1
    que = deque(sorted([(v,idx) for idx,v in enumerate(dg)]))
    ans = []
    while que:
        v,idx = que.popleft()
        if idx == 0:
            continue
        else:
            if dg[idx] == 0:
                ans.append(idx)
                for i in maps[idx]:
                    dg[i] -=1
    if len(ans) == N:
        print(*ans)
    else:
        print('IMPOSSIBLE')

