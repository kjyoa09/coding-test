from sys import stdin
from collections import Counter
input = stdin.readline

N,M = map(int,input().strip().split(' '))
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]

dic = {}
cctv = []

for r in range(N):
    for c in range(M):
        dic[(r,c)] = maps[r][c]
        if 1<=maps[r][c]<=5:
            cctv.append((r,c,maps[r][c]))
D = [[[(1,0)],[(0,1)],[(0,-1)],[(-1,0)]],#1 
    [[(1,0),(-1,0)],[(0,1),(0,-1)]], #2
    [[(1,0),(0,1)],[(-1,0),(0,-1)],[(1,0),(0,-1)],[(-1,0),(0,1)]],
    [[(1,0),(-1,0),(0,1)],[(1,0),(-1,0),(0,-1)],
    [(1,0),(0,1),(0,-1)],[(-1,0),(0,1),(0,-1)]],
    [[(1,0),(0,1),(0,-1),(-1,0)]]]

# print(D[0])
# print(D[1])
# print(D[2])
# print(D[3])

def CH(dic,coord,D):
    (x,y),(dx,dy) = coord,D
    while 1:
        px,py = x+dx,y+dy
        if 0<=px<N and 0<=py<M and dic[(px,py)] != 6:
            if dic[(px,py)] == 0:
                dic[(px,py)] = -1
            x,y = px,py
        else:
            return dic

ans = float('inf')
def dfs(dic,cctv,idx):
    global ans
    if len(cctv) == idx:
        tmp = Counter(dic.values())[0]
        if ans > tmp:
            ans = tmp
    else:
        r,c,ix = cctv[idx]
        for m in D[ix-1]:            
            tmp_dic = dic.copy()
            for d in m:
                tmp_dic = CH(tmp_dic,(r,c),d)
            dfs(tmp_dic,cctv,idx+1)

dfs(dic,cctv,0)
print(ans)