# Dp로 안되네;;
import sys
sys.stdin = open("in.txt","r")
maps = [[0] * 501 for _ in range(501)]
N = int(sys.stdin.readline())
for _ in  range(N):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    for r in range(min(x1,x2),max(x1,x2)+1):
        for c in range(min(y1,y2),max(y1,y2)+1):
            maps[r][c] = 1
N = int(sys.stdin.readline())
for _ in  range(N):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().rstrip().split())
    for r in range(min(x1,x2),max(x1,x2)+1):
        for c in range(min(y1,y2),max(y1,y2)+1):
            maps[r][c] = float("INF")
maps[0][0] = 0
ans = [[0] * 501 for _ in range(501)]
for r in range(500,):
    for c in range(501):
        if r == 0 and c == 0:
            ans[r][c] = 0
        elif r == 0:
            ans[r][c] = ans[r][c-1] + maps[r][c]
        elif c == 0:
            ans[r][c] = ans[r-1][c] + maps[r][c]
        else:
            ans[r][c] = min(ans[r-1][c],ans[r][c-1]) + maps[r][c]
if ans[500][500] == float("INF"):
    print(-1)
else:
    print(ans[500][500])
