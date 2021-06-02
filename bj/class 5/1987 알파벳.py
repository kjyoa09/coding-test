# 시간초과가 애매하다..
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def backtrack(x, y, visitedAlpha, cnt):
    global ans
    if cnt > ans:
        ans = cnt
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in visitedAlpha:
                visitedAlpha += board[nx][ny]
                backtrack(nx, ny, visitedAlpha, cnt+1)
                visitedAlpha = visitedAlpha[:-1]
                

R, C = map(int, input().rstrip().split())
board = []
for i in range(R):
    string = input().rstrip()
    board.append(list(string))


visitedAlpha = ""
visitedAlpha += board[0][0]
ans = 1

backtrack(0, 0, visitedAlpha, 1)

print(ans)