# 세그먼트 트리
class ftn:
    def __init__(self,N,li):
        self.arr = [0] * (4*N)
        self.li = li

    def make_tree(self,st,en,idx):
        if st==en:
            self.arr[idx] = self.li[st]
        else:
            mid = (st+en)//2
            self.make_tree(st,mid,2*idx)
            self.make_tree(mid+1,en,2*idx+1)
            self.arr[idx] = self.arr[idx*2] + self.arr[idx*2+1]
    
    def change(self,st,en,idx,v,ix):
        self.arr[idx] += v
        if st == en:
            return
        mid = (st+en)//2
        if st<=ix<=mid:
            self.change(st,mid,2*idx,v,ix)
        else:
            self.change(mid+1,en,2*idx+1,v,ix)

    def sum(self,st,en,idx,lb,rb):
        if (lb > en) or (rb<st):
            return 0
        
        if (lb <= st) and (en <= rb):
            return self.arr[idx]
        
        mid = (st+en)//2
        return self.sum(st,mid,idx*2,lb,rb) + self.sum(mid+1,en,idx*2+1,lb,rb)
          

from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

N,M,K = map(int,input().split(' '))
arr = []
for _ in range(N):
    arr.append(int(input()))
sol = ftn(N,arr)
sol.make_tree(0,N-1,1)


for _ in range(M+K):
    a,b,c = map(int,input().split(' '))
    if a == 1:
        diff = c-arr[b-1]
        arr[b-1] = c
        sol.change(0,N-1,1,diff,b-1)
    else:
        print(sol.sum(0,N-1,1,b-1,c-1))
