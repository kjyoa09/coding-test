# https://woodforest.tistory.com/159
# 카탈란 수 공식으로 풀 수 있음

class ftn:
    def __init__(self,n):
        self.ans = 0
        self.n = 2*n
    
    def find(self,n,cnt):
        if cnt == self.n:
            if n == 0:
                self.ans += 1
        elif n - (self.n - cnt) == 0:
            self.ans += 1
        else:
            if n >= 1 :
                self.find(n-1,cnt + 1)
            self.find(n+1,cnt + 1)
            
def solution(n):
    sol = ftn(n)
    sol.find(0,0)
    return sol.ans