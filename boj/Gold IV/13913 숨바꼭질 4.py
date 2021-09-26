from sys import stdin
from collections import deque
stdin = open('in.txt','r')
input = stdin.readline

N,K = map(int,input().strip().split(' '))

if K <= N:
    print(N-K)
    print(*list(range(N,K-1,-1)))
else:
    arr = [float('inf')] * (100001)
    que = deque([(K,0,[K])])
    while que:
        now,cnt,path = que.popleft()
        arr[now] = cnt
        if now == N:
            print(cnt)
            print(*path)
            break
        else:
            if 0<=now+1<100000 and arr[now+1] > cnt+1:
                que.append((now+1,cnt+1,[now+1]+path))
            if 0<=now-1<100000 and arr[now-1] > cnt+1:
                que.append((now-1,cnt+1,[now-1]+path))
            if 0<=now//2<100000 and now%2 == 0 and arr[now//2] > cnt +1:
                que.append((now//2,cnt+1,[now//2]+path))
