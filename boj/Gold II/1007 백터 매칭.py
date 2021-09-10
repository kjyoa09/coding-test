# https://nerogarret.tistory.com/21
from itertools import combinations

class ftn:
    def __init__(self):
        self.dic = {}
        self.ans = float('inf')

        self.T_x = 0
        self.T_y = 0

    def insert(self,x,y,idx):
        self.dic[idx] = (x,y)    
        self.T_x += x
        self.T_y += y

    def dist(self,arr):
        x,y = 0,0

        for a in arr:
            x += self.dic[a][0]
            y += self.dic[a][1]
        tmp = ((2*x - self.T_x)**2 + (2*y - self.T_y)**2)**(1/2)
        
        if self.ans > tmp:
            self.ans = tmp
        



from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

for _ in range(int(input())):
    N = int(input())
    sol = ftn()

    for idx in range(N):
        x,y = map(int,input().split(' '))
        sol.insert(x,y,idx)

    for comb in combinations(sol.dic.keys(),N//2):
        sol.dist(comb)
    print(sol.ans)
