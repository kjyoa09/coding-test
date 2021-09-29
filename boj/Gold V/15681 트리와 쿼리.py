from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
stdin = open("in.txt","r")
input = stdin.readline
N,R,Q = map(int,input().strip().split(' '))
maps = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().strip().split(' '))
    maps[a].append(b)
    maps[b].append(a)

dp = [[] for _ in range(N+1)]

def makeTree(now,pre):
    for ch in maps[now]:
        if ch != pre:
            dp[now].append(ch)
            makeTree(ch,now)
makeTree(R,-1)

size = [0] * (N+1)
def countSub(now):
    size[now] = 1
    for ch in dp[now]:
        countSub(ch)
        size[now] += size[ch]
countSub(R)
for _ in range(Q):
    print(size[int(input())])