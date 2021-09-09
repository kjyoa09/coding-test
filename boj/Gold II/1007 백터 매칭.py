from itertools import combinations

class ftn:
    def __init__(self):
        self.dic = {}
        self.ans = float('inf')

    def insert(self,x,y,idx):
        self.dic[idx] = (x,y)    
    
    def dist(a,b):
        return sum((x+y)**2 for x,y in zip(a,b))**(1/2)


from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline



for _ in range(int(input())):
    N = int(input())
    sol = ftn()

    for idx in range(N):
        x,y = map(int,input().split(' '))
        sol.insert(x,y,idx)
    
    for 
    print(list(combinations(sol.dic.keys(),2)))