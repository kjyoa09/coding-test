# 왜.. 이게 더 느리지...

# from sys import stdin
# from collections import defaultdict,deque
# stdin = open('in.txt','r')
# input = stdin.readline

# N,M,K = map(int,input().strip().split(' '))
# maps = [[5] * N for _ in range(N)]
# tree = defaultdict(deque)
# A = [list(map(int,input().strip().split(' '))) for _ in range(N)]

# for _ in range(M):
#     a,b,c = map(int,input().strip().split(' '))
#     tree[(a-1,b-1)].append(c)

# dx,dy = [-1,-1,-1,0,0,1,1,1],[-1,0,1,-1,1,-1,0,1]

# for _ in range(K):
#     ba = defaultdict(lambda : 0)
#     for (r,c) in tree.keys():
#         que = deque([])
#         dead,TF = 0,False
#         while tree[(r,c)]:                
#             tmp = tree[(r,c)].popleft()
#             if maps[r][c] >= tmp:
#                 maps[r][c] -= tmp
#                 que.append(tmp + 1)
#                 TF = True
#                 if (tmp+1)%5 == 0:
#                     ba[(r,c)] += 1
#             else:
#                 dead += tmp//2
#         if TF:
#             tree[(r,c)] = que
#         maps[r][c] += dead

#     for (r,c),tmp in ba.items():
#         tmp = [1]*tmp
#         for idx in range(8):
#             pr,pc = r+dx[idx],c+dy[idx]
#             if 0<=pr<N and 0<=pc<N:
#                 tree[(pr,pc)].extendleft(tmp)
#     for r in range(N):
#         for c in range(N):
#             maps[r][c] += A[r][c]

# print(sum(len(x) for x in tree.values()))


import sys
sys.stdin = open('in.txt','r')
input = sys.stdin.readline
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

n, m, k = map(int, input().split())
plus_a = [list(map(int, input().split())) for _ in range(n)]
a = [[5]*n for _ in range(n)]
tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for year in range(k):

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                tree[i][j].sort()
                temp_tree, dead_tree = [], 0
                for age in tree[i][j]:
                    if age <= a[i][j]:
                        a[i][j] -= age
                        age += 1
                        temp_tree.append(age)
                    else:
                        dead_tree += age // 2
                a[i][j] += dead_tree
                tree[i][j] = temp_tree

    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                for age in tree[i][j]:
                    if age % 5 == 0:
                        for dir in range(8):
                            ni = i + dx[dir]
                            nj = j + dy[dir]
                            if 0 <= ni < n and 0 <= nj < n:
                                tree[ni][nj].append(1)
            a[i][j] += plus_a[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree[i][j])
print(ans)
