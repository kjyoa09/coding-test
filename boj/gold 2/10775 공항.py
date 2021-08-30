# UNION FIND
# 첫번째 공항 사용시 TF False로 변환
stdin = open("in.txt")
input = stdin.readline

G = int(input())
P = int(input())


class ftn:
    def __init__(self,G):
        self.arr = list(range(G))
    
    def find(self,idx):
        if self.arr[idx] != idx:
            self.arr[idx] = self.find(self.arr[idx])
        return self.arr[idx]

    def union(self,idx1,idx2): # idx2 > idx1
        self.arr[idx2] = idx1 

sol = ftn(G)
cnt = 0
TF = True
for _ in range(P):
    g = int(input()) - 1
    idx2 = sol.find(g)
    if idx2 == 0:
        if TF :
            TF = False
            cnt += 1
        else:
            break
    else:
        idx1 = sol.find(idx2 - 1)
        sol.union(idx1,idx2)    
        cnt += 1
print(cnt)
