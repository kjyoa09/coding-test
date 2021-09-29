from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
stdin = open("in.txt","r")
input = stdin.readline

N = int(input())
arr = [0]+list(map(int,input().strip().split(' ')))

maps = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().strip().split(' '))
    maps[a].append(b)
    maps[b].append(a)

tree = [[] for _ in range(N+1)]

def makeTree(now,pre):
    for ch in maps[now]:
        if ch != pre:
            tree[now].append(ch)
            makeTree(ch,now)
makeTree(1,-1)

ans = [[0,0] for _ in range(N+1)] # 0: 지금 now 선택, 1 : 선택 X
road = [[[],[]]for _ in range(N+1)]
def dfs(now):
    ans[now][0] = arr[now]
    road[now][0].append(now) 
    for ch in tree[now]:
        dfs(ch)
        ans[now][1] += max(ans[ch])
        if ans[ch][0] > ans[ch][1]:
            road[now][1] += road[ch][0]
        else:
            road[now][1] += road[ch][1]
        ans[now][0] += ans[ch][1]
        road[now][0] += road[ch][1]
dfs(1)
idx = 1 if ans[1][1] > ans[1][0] else 0
print(ans[1][idx])
print(*sorted(road[1][idx]))