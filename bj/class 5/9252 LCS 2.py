# 9251 LCS 연관 문제
# Backtracking : 같은 쪽으로 이동 > 없으면 ans 적고 대각으로 이동 
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("in.txt","r")
S = [sys.stdin.readline().rstrip(),sys.stdin.readline().rstrip()]
S.sort(key=lambda x:len(x))
Sh,Lo = S[0],S[1]
maps = [[0]*(len(Sh)+1) for _ in range(len(Lo)+1)]

ans = ""
for r in range(1,len(Lo) +1):
    for c in range(1,len(Sh) + 1):
        if Sh[c-1] == Lo[r-1]:
            maps[r][c] = maps[r-1][c-1] + 1
        else:
            maps[r][c] = max(maps[r-1][c],maps[r][c-1])

print(maps[-1][-1])
ans = ""
def dfs(x,y):
    global ans
    if x==0 or y == 0:
        return
    else:
        if maps[x][y-1] == maps[x][y]:
            x,y = x,y-1
        elif maps[x-1][y] == maps[x][y]:
            x,y = x-1,y
        else:
            x,y = x-1,y-1
            ans = Lo[x] + ans
        dfs(x,y)
dfs(len(Lo),len(Sh))
print(ans)