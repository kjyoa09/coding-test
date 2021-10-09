from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

n,m,h = map(int,input().strip().split(' '))
board = [[False] * n for _ in range(h)]
for _ in range(m):
    a,b = map(int,input().strip().split(' '))
    board[a-1][b-1] = True

ans = 4

def down():
    for idx in range(n):
        k = idx
        for hh in range(h):
            if board[hh][k]:
                k += 1
            elif k>0 and board[hh][k-1]:
                k -= 1
        if k != idx :
            return False
    else:
        return True

def dfs(nh,nn,cnt):
    global ans
    if down():
        if cnt < ans:
            ans = cnt
        return
    
    if cnt == 3 or cnt > ans:
        return
    
    else:
        for hh in range(nh,h):
            for nnn in range(nn,n-1):
                if not board[hh][nnn] and (nnn == 0 or not board[hh][nnn-1]) and (nnn == n-1 or not board[hh][nnn +1]):
                    board[hh][nnn] = True
                    dfs(hh,nnn,cnt + 1)
                    board[hh][nnn] = False
            nn = 0

dfs(0,0,0)
print(ans if ans < 4 else -1)