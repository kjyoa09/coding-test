class ftn:
    def __init__(self,arr):
        self.arr = arr
        self.tree = [0] * (1048577 * 2)
        self.Mod = 1_000_000_007
    def maketree(self,st,en,idx):
        if st == en:
            self.tree[idx] = self.arr[st]
        else:
            mid = (st+en)//2
            self.maketree(st,mid,idx*2)
            self.maketree(mid+1,en,idx*2+1)
            self.tree[idx] = (self.tree[idx*2] * self.tree[idx*2+1]) % self.Mod
    
    def change(self,st,en,idx,num,ix):
        self.tree[idx] *= num
        self.tree[idx] %= self.Mod
        if st == en:
            return
        mid = (st+en)//2
        if st <= ix <= mid:
            self.change(st,mid,idx*2,num,ix)
        else:
            self.change(mid+1,en,idx*2+1,num,ix)
    
    def find(self,st,en,idx,lb,rb):
        if (lb > en) or (rb < st):
            return 1
        
        if (lb <= st) and (en <= rb):
            return self.tree[idx]

        mid = (st+en)//2
        return (self.find(st,mid,2*idx,lb,rb) * self.find(mid+1,en,2*idx+1,lb,rb)) % self.Mod

from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

n,m,k = map(int,input().strip().split(' '))

arr = []
for _ in range(n):
    arr.append(int(input()))

sol = ftn(arr)
sol.maketree(0,n-1,1)
print(sol.tree)
for _ in range(m+k):
    a,b,c = map(int,input().strip().split(' '))
    if a == 1:
        sol.change(0,n-1,1,c/sol.arr[b-1],b-1)
        sol.arr[b-1] = c
    else:
        print(int(sol.find(0,n-1,1,b-1,c-1)%1_000_000_007))