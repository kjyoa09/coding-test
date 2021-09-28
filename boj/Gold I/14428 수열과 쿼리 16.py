class ftn:
    def __init__(self,arr):
        self.mins = [0]*(len(arr)*4)
        self.idxs = [0]*(len(arr)*4)
        self.arr = arr
    
    def mk(self,s,e,idx):
        if s == e:
            self.mins[idx] = self.arr[s]
            self.idxs[idx] = s
        else:
            mid = (s+e)//2
            self.mk(s,mid,2*idx)
            self.mk(mid+1,e,2*idx+1)
            if self.mins[2*idx] > self.mins[2*idx+1]:
                self.mins[idx] = self.mins[2*idx+1]
                self.idxs[idx] = self.idxs[2*idx+1]
            else:
                self.mins[idx] = self.mins[2*idx]
                self.idxs[idx] = self.idxs[2*idx]
    
    def find(self,s,e,idx,lb,rb):
        if (s>rb) or (e<lb):
            return float('inf'),-1
        
        if (lb<=s) and (e<=rb):
            return self.mins[idx],idx
        
        else:
            mid = mid = (s+e)//2
            l,lidx = self.find(s,mid,2*idx,lb,rb)
            r,ridx = self.find(mid+1,e,2*idx+1,lb,rb)
            if l > r :
                return r,ridx
            else:
                return l,lidx

    def change(self,s,e,idx,chidx):
        if s == e:
            self.mins[idx] = self.arr[s]
        else:
            mid = mid = (s+e)//2
            if s<=chidx<=mid:
                self.change(s,mid,2*idx,chidx)
            else:
                self.change(mid+1,e,2*idx+1,chidx)

            if self.mins[2*idx] > self.mins[2*idx+1]:
                self.mins[idx] = self.mins[2*idx+1]
                self.idxs[idx] = self.idxs[2*idx+1]
            else:
                self.mins[idx] = self.mins[2*idx]
                self.idxs[idx] = self.idxs[2*idx]

from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
N = int(input())
sol = ftn(list(map(int,input().strip().split(' '))))
sol.mk(0,N-1,1)


for _ in range(int(input())):
    a,b,c = map(int,input().strip().split(' '))
    if a == 1:
        sol.arr[b-1] = c
        sol.change(0,N-1,1,b-1)
    else:
        _,v = sol.find(0,N-1,1,b-1,c-1)
        print(sol.idxs[v]+1)