from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
stdin = open("in.txt","r")
input = stdin.readline

N = int(input())
maps = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,input().strip().split(' '))
    maps[a].append(b)
    maps[b].append(a)

tree = [[] for _ in range(N+1)]
def MT(now,pre):
    for ch in maps[now]:
        if ch != pre:
            tree[now].append(ch)
            MT(ch,now)
MT(1,0)
ans = [[0,0] for _ in range(N+1)]# 0 : 현재 Node >> early 1 : Noob

def dfs(now):
    ans[now][0] = 1
    for ch in tree[now]:
        dfs(ch)
        ans[now][1] += ans[ch][0]
        ans[now][0] += min(ans[ch])
dfs(1)
print(min(ans[1]))