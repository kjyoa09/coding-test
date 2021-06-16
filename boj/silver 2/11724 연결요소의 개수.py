import sys
from collections import defaultdict,deque


dic = defaultdict(deque)
n,m = map(int,sys.stdin.readline().split())

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    dic[a] += [b]
    dic[b] += [a]

T = deque(list(range(1,n+1)))
ch = [-1] * (n+1)

cnt = 0
while T:
    tmp = T.pop()
    if ch[tmp] == 0:
        continue
    else:
        ch[tmp] = 0
        cnt += 1
        Q = dic[tmp]
        while Q:
            x = Q.pop()
            if ch[x] == -1:
                Q += dic[x]
                ch[x] = 0
print(cnt)

