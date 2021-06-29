from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N,M = map(int,input().rstrip().split())
maps = [list(input().rstrip()) for _ in range(N)]
direct = {"D":(1,0),"L":(0,-1),"R":(0,1),"U":(-1,0)}
check = [["a"]*M for _ in range(N)]

ans = 0

def dfs(r,c):
    global ans
    px,py = r + direct[maps[r][c]][0],c + direct[maps[r][c]][1]
    if check[px][py].isdigit():
        check[r][c] = check[px][py]
        return check[px][py]
    elif check[px][py] == "b" :
        ans += 1
        check[r][c] = str(ans)
        return str(ans)
    else:
        check[r][c] = "b"
        check[r][c] = dfs(px,py)
        return check[r][c]

for r in range(N):
    for c in range(M):
        if check[r][c] == "a":
            dfs(r,c)
print(ans)