'''
Dijkstra + Topology sort
'''

from collections import deque

class ftn:
    def __init__(self,n,path,order):
        self.N = n
        self.dg = [0] * n
        self.road = [[] for _ in range(n)]
        self.v = [[] for _ in range(n)]
        
        for s,e in path:
            self.road[s].append(e)
            self.road[e].append(s)
        
        for s,e in order:
            self.v[s].append(e)
            self.dg[e] += 1
        
        self.visited = [False] * n

    def dijk(self):
        que = deque([0])

        while que:
            q = que.popleft()
            if not self.visited[q]:
                self.visited[q] = True
                for e in self.v[q]:
                    self.dg[e] -= 1
                    if not self.dg[e] and any(self.visited[x] for x in self.road[e]):
                        que.append(e)

                for e in self.road[q]:
                    if not self.visited[e] and not self.dg[e]:
                        que.append(e)

                    
def solution(n, path, order):
    sol = ftn(n,path,order)
    if sol.dg[0]:
        return False
    sol.dijk()
    return all(sol.visited)