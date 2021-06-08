import sys
from collections import deque

n = int(sys.stdin.readline())

Con = ["D","S","L","R"]

def cmd(K):
    a = K//1000
    b = (K%1000)//100
    c = (K%100)//10
    d = K%10
    return [K*2 % 10000,K-1 if K != 0 else 9999 ,b*1000 + c * 100 + d * 10 + a,d * 1000 + a * 100 + b * 10 + c]

def pp(li):
    if li[0] == "":
        return ""
    else:
        return pp(check[li[1]])+li[0]
    
for i in range(n):
    tmp,target = map(int,sys.stdin.readline().rstrip().split())
    check = [False] * 10001
    check[tmp] = ["",tmp]
    Q = deque([tmp])
    while 1:
        K = Q.popleft()
        post = cmd(K)
        
        for co,po in zip(Con,post):            
            if check[po] == False:
                check[po] = [co,K]
                Q.append(po)
        if check[target]:
            print(pp(check[target]))
            break
