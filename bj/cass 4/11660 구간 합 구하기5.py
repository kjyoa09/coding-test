# pypy로 통과...
# 면적을 구해서 구하면 python으로도 통과
import sys

sys.stdin = open("in.txt","r")
'''
N,M = map(int,sys.stdin.readline().rstrip().split())

maps = []

for _ in range(N):
    row = list(map(int,sys.stdin.readline().rstrip().split()))
    tmp = [row[0]]
    for r in row[1:]:
        tmp += [tmp[-1] + r]
    maps.append(tmp)

for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    ans = 0
    for r in range(x1,x2+1):
        if y1 > 1:
            ans += maps[r-1][y2-1] - maps[r-1][y1-2]
        else:
            ans += maps[r-1][y2-1]
    print(ans)
'''
n,m=map(int,sys.stdin.readline().rstrip().split())
n+=1
a=[0]*n
d=[0]*n
for i in range(1,n):
    a[i]=[0]+list(map(int,sys.stdin.readline().rstrip().split()))
    d[i]=[0]*n
a[0]=d[0]=[0]*n
for i in range(1,n):
    for j in range(1,n):
        d[i][j]=a[i][j]+d[i-1][j]+d[i][j-1]-d[i-1][j-1]

for t in range(m):
    q,w,e,r=map(int,sys.stdin.readline().rstrip().split())
    print(d[e][r]-d[e][w-1]-d[q-1][r]+d[q-1][w-1])