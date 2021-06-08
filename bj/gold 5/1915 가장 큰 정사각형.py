import math,sys

a,b = map(int,input().split())

ch = [[0] * b for _ in range(a)]

maps = [list(map(int, input().strip())) for _ in range(a)]
ans = -1
for r in range(a):
    for c in range(b):
        if r == 0 or c == 0:
            ch[r][c] = maps[r][c]
        else:
            if ch[r][c-1] != 0 and ch[r-1][c] != 0 and maps[r][c] != 0:
                tmp = min(ch[r-1][c],ch[r][c-1])
                if ch[r-tmp][c-tmp] != 0:
                    ch[r][c] = tmp + 1
                else:
                    ch[r][c] = tmp
            else:
                ch[r][c] = maps[r][c]
   
        if ch[r][c] > ans:
            ans = ch[r][c]
print(ans **2)
