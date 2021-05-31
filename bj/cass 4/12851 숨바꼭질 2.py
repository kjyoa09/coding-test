# visit[i] > time 이면 다른 방법으로 왔지만 같은 거리인 경우 없어짐
# k-n : 음수..

import sys
from collections import deque
sys.stdin = open("in.txt","r")
n,k = map(int,sys.stdin.readline().strip().split())

if k <= n:
    print(n-k)
    print(1)

else:
    inf = float("INF")
    ans = inf
    visit = [inf] * 100001
    que = deque([(n,0)])
    while que:
        now,t = que.popleft()
        post = [(now - 1,t + 1),(now + 1,t + 1),(now*2 ,t + 1)]
        for i,time in post:
            if 0<=i<=100000 and time <= ans and visit[i] >= time:
                if i == k:
                    if time < ans:
                        ans = time
                        cnt = 1
                    elif time == ans:
                        cnt +=1
                else:
                    que.append((i,time))
                    visit[i] = time
    print(ans)
    print(cnt)
