from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
N = int(input())
maps = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().strip().split(' '))
    maps[a].append(b)
    maps[b].append(a)

visited,SNS = [False] * (N+1),[[0] * (N+1) for _ in range(2)]

def dfs(now):
    global visited,SNS
    visited[now] = True

    for ch in maps[now]:
        if not visited[ch]:
            dfs(now,ch)


SNS[1][2] = 1

visited