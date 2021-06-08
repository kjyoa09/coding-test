import sys
sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())
dx = list(range(1,N));dy = list(range(1,M))
maps = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

def dfs(dx,dy,coord):
    x,y = coord
    if not (0<=x+dx<N and 0<=y+dy<M):
        return maps[x][y]
    else:
        return dfs(dx,dy,(x+dx,y+dy)) + maps[x][y]


print(dfs(0,1,(0,0)))
arr = []
for i in range(N):
    for j in range(M):
        for dx in range(N):
            for dy in range(M):
                if dx == dy == 0:
                    continue
                else:
                    tmp = dfs(dx,dy,(i,j))
                    print(tmp)
                    if len(tmp) > 1:
                        arr += [tmp,tmp[::-1]]
print(arr)
ans = -1
for i in arr:
    for j in range(2,len(i)+1):
        tmp = int(i[:j])
        if tmp**(1/2)%1 == 0 and ans < tmp:
            ans = tmp
print(ans)
zip