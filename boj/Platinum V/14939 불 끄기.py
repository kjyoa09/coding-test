from os import rename
from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

maps = [[True if x == '#' else False for x in list(input().strip())] for _ in range(10)]

class ftn:
    def __init__(self,maps):
        self.maps = maps
        self.ans = -1
  
    def fun(self,TF):
        arrs = [x[:] for x in maps]
        tmp = 0
        self.cnt[TF] =1
        for r in range(10):
            for c in range(10):
                if r == 0:
                    if TF[c] == '1':

                        tmp += 1
                        arrs[r][c] = False if arrs[r][c] else True
                        arrs[r+1][c] = False if arrs[r+1][c] else True  
                        if c > 0 :
                            arrs[r][c-1] = False if arrs[r][c-1] else True
                        if c < 9 :
                            arrs[r][c+1] = False if arrs[r][c+1] else True 
                else:
                    if not arrs[r-1][c]:
                        tmp +=1
                        arrs[r-1][c] = False if arrs[r-1][c] else True 
                        arrs[r][c] = False if arrs[r][c] else True   
                        if c > 0 :
                            arrs[r][c-1] = False if arrs[r][c-1] else True
                        if c < 9 :
                            arrs[r][c+1] = False if arrs[r][c+1] else True
                        if r < 9:
                            arrs[r+1][c] = False if arrs[r+1][c] else True
        if all(arrs[-1]):

            if self.ans == -1:
                self.ans = tmp

            elif self.ans > tmp:
                self.ans = tmp
        

sol = ftn(maps)

for i in range(2**10):
    sol.fun(bin(i)[2:].rjust(10,'0'))

print(sol.ans)