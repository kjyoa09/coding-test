# 비트마스킹 + dp
# 비트 연산자...는 나쁘지 않은데 오히려 dp가 더 어렵네;;
from sys import stdin
# stdin = open("in.txt")
# input = stdin.readline

# N = int(input())
# W = [list(map(int,input().split(' '))) for _ in range(N)]


# maps = [[0] * (65536) for _ in range(N)]
# inf = float('inf')

# def dfs(node,bit):

#     if 1<<node == bit: return 0 
#     maps[node][bit] = inf

#     for next in range(N):
#         if bit & 1<<next or W[node][next] == 0: continue

#         if maps[next][(1<<next)|bit] > maps[node][bit] + W[node][next]:
#             maps[next][(1<<next)|bit] = maps[node][bit] + W[node][next]
#             dfs(next,(1<<next)|bit)
# dfs(0,1)
# print(min(maps[node][-1] + W[node][0] if W[node][0] != 0 else float('inf') for node in range(N)))

stdin = open("in.txt")
input = stdin.readline
n=int(input())
dist=[[*map(int,input().split())] for i in range(n)]
dp=[[0]*65537 for i in range(17)]
inf=float('inf')
def tsp(current, visited):
    if visited==(1<<n)-1 and dist[current][0] != 0 : return dist[current][0] 
    if dp[current][visited]!=0: return dp[current][visited]
    dp[current][visited]=inf
    for next in range(n):
        if visited & (1<<next): continue
        if dist[current][next]==0: continue
        dp[current][visited]=min(dp[current][visited], tsp(next, visited | (1<<next)) + dist[current][next])
    return dp[current][visited]
print(dp[0][1])
print(int(tsp(0,1)))
