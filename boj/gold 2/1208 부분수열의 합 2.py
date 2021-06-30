from sys import stdin
from collections import deque
stdin = open("in.txt")
input = stdin.readline

N,S = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
maps = [[0 for _ in range(2000001)] for _ in range(N+1)]
maps[0][1000000] = 1
que = deque([1000000])
for i in range(1,N+1):
    tmp_que = deque([])
    while que:
        tmp = que.pop()
        tmp_que.append(tmp)
        tmp_que.append(tmp+arr[i-1])
        maps[i][tmp] += maps[i-1][tmp]
        maps[i][tmp] += maps[i-1][tmp+arr[i-1]]
    que = tmp_que
print(maps[N][S+1000000])