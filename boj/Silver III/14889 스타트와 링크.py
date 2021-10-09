from sys import stdin
from itertools import combinations
stdin = open('in.txt','r')
input = stdin.readline

N = int(input())
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]
tot = sum(sum([x for x in maps],[]))
dic = {}
ans = float('inf')
def dfs(now,cnt,arr,score):
    
    global ans
    if cnt == N//2:
        if tuple(arr) not in dic:
            tmp,v,TF = 0,[],[False] * N
            for idx,tf in enumerate(arr):
                if not tf:
                    TF[idx] = True
                    v.append(idx)
            for x in v:
                for j in v:
                    tmp += maps[x][j]
            
            if ans > abs(tmp-score):
                ans =  abs(tmp-score)
            
            dic[tuple(arr)] = 1
            dic[tuple(TF)] = 1
        return

    else:
        for idx in range(now,N):
            arr[idx] = True
            if cnt == 0:                
                dfs(idx+1,cnt+1,arr,score)
            else:
                tmp = 0
                for a,b in enumerate(arr):
                    if b == True:
                        tmp += maps[a][idx]
                        tmp += maps[idx][a]
                dfs(idx+1,cnt+1,arr,score+tmp)             
            arr[idx] = False                    
                
dfs(0,0,[False]*N,0)
print(ans)
