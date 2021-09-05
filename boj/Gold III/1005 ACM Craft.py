# 위상정렬
# iv 에 앞에 건물 지어야 하는 번호 저장
# ans 에 각 건물 건설 완료 시간 저장 
from sys import stdin
from collections import deque
stdin = open("in.txt")
input = stdin.readline
T = int(input())
for _ in range(T):
    N,K = map(int,input().rstrip().split())
    cost = [0] + list(map(int,input().rstrip().split()))
    ans = [0] * (N+1)
    v = [[] for _ in range(N+1)]
    iv = [[] for _ in range(N+1)]
    dg = [0] * (N+1)
    for _ in range(K):
        a,b = map(int,input().rstrip().split())
        v[a].append(b)
        iv[b].append(a)
        dg[b] += 1
    que = deque([])
    for i in range(1,N+1):
        if dg[i] == 0:
            que.append(i)
            ans[i] = cost[i]
    while que:
        tmp = que.pop()
        for i in v[tmp]:
            dg[i] -= 1
            if dg[i] == 0:
                ans[i] = max([ans[v] for v in iv[i]]) + cost[i]
                que.append(i)
    print(ans[int(input())])