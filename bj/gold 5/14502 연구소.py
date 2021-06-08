import sys
from itertools import combinations
from collections import deque

n,m = map(int,sys.stdin.readline().split())
def bfs(S,arr,comb):
    for c in comb:
        a,b = c
        arr[a][b] = 1
        
    dx = [1,0,-1,0];dy = [0,1,0,-1]
    cnt = 0
    while S:
        x,y = S.pop()
        for i in range(4):
            nextX,nextY = x + dx[i],y + dy[i]
            if 0 <= nextX < n and 0 <= nextY < m and  arr[nextX][nextY]== 0:
                arr[nextX][nextY] = 2
                cnt += 1
                S += [(nextX,nextY)]
    return cnt

maps = []
arr = []
S = []
for _ in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    maps += [tmp]
    for idx,x in enumerate(tmp):
        if x == 0:
            arr += [(_,idx)]
        elif x == 2:
            S += [(_,idx)]

Max = len(arr)
possible = list(combinations(arr,3))

ans = - 1
for poss in possible:
    Tmp_maps = []
    for i in maps:
        Tmp_maps += [i[:]]
    Tmp_s = deque(S[:])

    re = bfs(Tmp_s,Tmp_maps,poss)

    if Max - re -3  > ans:
        ans = Max - re -3

print(ans)

