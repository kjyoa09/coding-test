from sys import stdin
from collections import deque
stdin = open('in.txt','r')
input = stdin.readline

def bfs(n):
    que = deque([1])
    par = [0] * (n+1)
    par[1] = (-1,-1)
    while que:
        remain = que.popleft()
        if remain == 0:
            break
        
        if par[(remain*(10%n))%n] == 0:
            que.append((remain*(10%n))%n)
            par[(remain*(10%n))%n] = (remain,'0')
        
        if par[(remain*(10%n)+1)%n] == 0:
            que.append((remain*(10%n)+1)%n)
            par[((remain*(10%n)+1)%n)] = (remain,'1')
    else:
        return 'BRAK'
    remain,ans = par[0]
    while par[remain] != (-1,-1):
        remain,tmp = par[remain]
        ans += tmp
    ans += '1'
    return ans[::-1]

for _ in range(int(input())):
    print(bfs(int(input())))
