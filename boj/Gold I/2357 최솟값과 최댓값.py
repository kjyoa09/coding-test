class ftn:
    def __init__(self,arr):
        self.arr = arr
        self.Max = [0]*(len(arr)*4)
        self.Min = [0]*(len(arr)*4)

    def make(self,idx,st,en):
        if st == en:
            self.Max[idx] = self.arr[st]
            self.Min[idx] = self.arr[en]
        else:
            mid = (st+en)//2
            self.make(idx*2,st,mid)
            self.make(idx*2+1,mid+1,en)
            self.Max[idx] = max(self.Max[idx*2],self.Max[idx*2+1])
            self.Min[idx] = min(self.Min[idx*2],self.Min[idx*2+1])

    def find(self,st,en,idx,lb,rb,TF):
        if (lb > en) or (rb<st):
            return -1 if TF else 1_000_000_001
        
        if (lb <= st) and (en <= rb):
            return self.Max[idx] if TF else self.Min[idx]\
        
        mid = (st+en)//2
        return max(self.find(st,mid,idx*2,lb,rb,TF),self.find(mid+1,en,idx*2+1,lb,rb,TF)) if TF else min(self.find(st,mid,idx*2,lb,rb,TF),self.find(mid+1,en,idx*2+1,lb,rb,TF))


from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

n,m = map(int,input().strip().split(' '))
arr = []
for _ in range(n):
    arr.append(int(input()))

sol = ftn(arr)
sol.make(1,0,n-1)

for _ in range(m):
    a,b = map(int,input().strip().split(' '))
    print(*[sol.find(0,n-1,1,a-1,b-1,False),sol.find(0,n-1,1,a-1,b-1,True)])