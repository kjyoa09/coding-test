class ftn:
    def __init__(self,arr):
        self.arr = arr
        self.tree = [0] * (len(arr)*4)
        self.Mod = 1_000_000_007

    def maketree(self,st,en,idx):
        if st == en:
            self.tree[idx] = self.arr[st]
        else:
            mid = (st+en)//2
            self.maketree(st,mid,idx*2)
            self.maketree(mid+1,en,idx*2+1)
            self.tree[idx] = ((self.tree[idx*2]%self.Mod) * (self.tree[idx*2+1]%self.Mod)) % self.Mod
    
    def change(self,st,en,idx,ch_idx):
        if st == en:
            self.tree[idx] = self.arr[ch_idx]
        else:
            mid = (st+en)//2
            if st<=ch_idx<=mid:
                self.change(st,mid,2*idx,ch_idx)
            else:
                self.change(mid+1,en,2*idx+1,ch_idx)
            self.tree[idx] = ((self.tree[idx*2]%self.Mod) * (self.tree[idx*2+1]%self.Mod)) % self.Mod

    def find(self,st,en,idx,lb,rb):
        if (lb > en) or (rb < st):
            return 1
        if (lb <= st) and (en <= rb):
            return self.tree[idx]
        mid = (st+en)//2
        return ((self.find(st,mid,2*idx,lb,rb)% self.Mod) * (self.find(mid+1,en,2*idx+1,lb,rb)% self.Mod)) % self.Mod

from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

n,m,k = map(int,input().strip().split(' '))

arr = []
for _ in range(n):
    arr.append(int(input()))

sol = ftn(arr)
sol.maketree(0,n-1,1)
for _ in range(m+k):
    a,b,c = map(int,input().strip().split(' '))
    if a == 1:
        sol.arr[b-1] = c
        sol.change(0,n-1,1,b-1)
    else:
        print(sol.find(0,n-1,1,b-1,c-1)%1_000_000_007)