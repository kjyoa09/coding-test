import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = deque([(x,idx) for idx,x in enumerate(arr)])

    cnt = 0
    while arr:
        x,idx = arr.popleft()
        if all(x >= i[0] for i in arr):
            cnt += 1
            if idx == m :
                print(cnt)
                break
        else:
            arr.append((x,idx))
            
    
    
