
import sys
from math import log


n = int(sys.stdin.readline())

maps = []
for num in range(n):
    maps.append(list(map(int, sys.stdin.readline().split())))


m=0;z=0;o=0
k = int(log(n,3))

def dfs(a,b,c,d):
    global m,z,o

    tmp = []
    for i in range(a,b):
        
        for j in range(c,d):
            if maps[i][j] == -1:
                tmp += [10]
            else:
                tmp += [maps[i][j]]
        
    if sum(tmp) == 0:
        z += 1
    elif sum(tmp) == len(tmp):
        o += 1
    elif sum(tmp) == len(tmp) * 10:
        m += 1
    else:
        dfs(a, (2 * a + b) // 3, c, (2 * c + d) // 3)
        dfs(a, (2 * a + b) // 3, (2 * c + d) // 3, (c + 2 * d) // 3)
        dfs(a, (2 * a + b) // 3, (c + 2 * d) // 3, d)
        dfs((2 * a + b) // 3, (a + 2 * b) // 3, c, (2 * c + d) // 3)
        dfs((2 * a + b) // 3, (a + 2 * b) // 3, (2 * c + d) // 3, (c + 2 * d) // 3)
        dfs((2 * a + b) // 3, (a + 2 * b) // 3, (c + 2 * d) // 3, d)
        dfs((a + 2 * b) // 3, b, c, (2 * c + d) // 3)
        dfs((a + 2 * b) // 3, b, (2 * c + d) // 3, (c + 2 * d) // 3)
        dfs((a + 2 * b) // 3, b, (c + 2 * d) // 3, d)



dfs(0,n,0,n)

print(m)
print(z)
print(o)
