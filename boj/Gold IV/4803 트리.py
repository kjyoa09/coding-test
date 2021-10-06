from sys import stdin
from collections import Counter
stdin = open('in.txt','r')
input = stdin.readline

class ftn:
    def __init__(self,n):
        self.n = n
        self.maps = [[] for _ in range(n+1)]
        self.tree = [[] for _ in range(n+1)]
        self.node = list(range(n+1))

        self.TF = True
        self.visited = [False] * (n+1)
    
    def insert(self,a,b):
        self.maps[a].append(b)
        self.maps[b].append(a)

    def mk(self,pre,now):
        if self.visited[now]:
            self.TF = False
            return
        else:
            self.visited[now] = True

        for ch in self.maps[now]:
            if pre != ch:
                self.node[ch] = self.node[now]
                self.tree[now].append(ch)
                self.mk(now,ch)
cnt = 1
while 1:       
    n,m = map(int,input().strip().split(' '))
    if n == m == 0:
        break
    else:
        sol = ftn(n)
        for _ in range(m):
            a,b = map(int,input().strip().split(' '))
            sol.insert(a,b)
        ans = 0

        for n in range(1,n+1):
            if sol.node[n] == n:
                sol.mk(0,n)
                ans += sol.TF
                sol.TF = True
        
        if ans == 0:
            print(f'Case {cnt}: No trees.')
        else:
            if ans == 1:
                print(f'Case {cnt}: There is one tree.')
            else:
                print(f'Case {cnt}: A forest of {ans} trees.')
        cnt += 1