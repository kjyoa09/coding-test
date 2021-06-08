# PyPy 통과... 시간단축할 방법...
import sys

sys.stdin = open("in.txt","r")
N = int(sys.stdin.readline())

Diag_L = [True] * (N*2)
Diag_R = [True] * (N*2)
C = [True] * N

ans = 0
def dfs(r,Diag_L,Diag_R,C):
    global ans
    if r == N:
        ans +=1    
    else:
        for i in range(N):
            if C[i] and Diag_L[r-i+N] and Diag_R[i+r]:
                C[i] = False;Diag_L[r-i+N] = False;Diag_R[i+r] = False
                dfs(r+1,Diag_L,Diag_R,C)
                C[i] = True;Diag_L[r-i+N] = True;Diag_R[i+r] = True

dfs(0,Diag_L,Diag_R,C)
print(ans)