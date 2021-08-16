'''
Kruskal Algorithm (Union & Find)
'''
import heapq as hq

class ftn:
    def __init__(self,land):
        self.Len = len(land)
        self.arr = list(range(self.Len * self.Len))
        
        self.que = []
        
        dx,dy = [0,1,0,-1],[1,0,-1,0]
        
        for r in range(self.Len):
            for c in range(self.Len):
                for idx in range(4):
                    px,py = r+dx[idx], c+dy[idx]
                    if 0<= px < self.Len and 0 <= py < self.Len:
                        hq.heappush(self.que,(abs(land[r][c] - land[px][py]),r*self.Len + c, px*self.Len + py))        
    
    def find(self,idx):
        if self.arr[idx] == idx:
            return idx
        self.arr[idx] = self.find(self.arr[idx])
        return self.arr[idx]
    
    def union(self,idx1,idx2):
        if idx1 < idx2:
            self.arr[idx2] = idx1
        else:
            self.arr[idx1] = idx2
    
    def ans(self,h):
        while len(self.que) and self.que[0][0] <= h:
            c,s,e = hq.heappop(self.que)
            idx1,idx2 = self.find(s),self.find(e)
            if idx1 != idx2:
                self.union(idx1,idx2)
        self.arr = [self.find(x) for x in self.arr]
        cnt = len(set(self.arr)) - 1 
        re = 0

        while cnt:
            c,s,e = hq.heappop(self.que)
            idx1,idx2 = self.find(s),self.find(e)
            if idx1 != idx2 :
                self.union(idx1,idx2)
                re += c
                cnt -= 1

        return re
        
        
def solution(land, height):
    sol = ftn(land)
    return sol.ans(height)