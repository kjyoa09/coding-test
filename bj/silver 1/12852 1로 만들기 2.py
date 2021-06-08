# N이 1일 때 생각
# 1 찾으면 Flag 로 탈출
# dfs 로 ans 만들기.
import sys
from collections import deque
sys.stdin = open("in.txt","r")
N = int(input())

inf = float("INF")
ans = [[0,inf]] * (N+1)
ans[N] = [0,0]
flag = False
que = deque([[N,0]])
while que:
    num,cnt = que.popleft()
    if num%3 == 0 and ans[num//3][1] > cnt +1:
        ans[num//3] = [num,cnt+1]
        que.append((num//3,cnt +1 ))
        if num//3 == 1:
            flag = True
    if num%2 == 0 and ans[num//2][1] > cnt +1:
        ans[num//2] = [num,cnt+1]
        que.append((num//2,cnt +1 ))  
        if num//2 == 1:
            flag = True          
    if num-1 >=1 and ans[num-1][1] > cnt +1:
        ans[num-1] = [num,cnt+1]
        que.append((num-1,cnt +1))   
        if num-1 == 1:
            flag = True
    if flag:
        break
print(ans[1][1])
def dfs(n):
    if ans[n][0]==0:
        return str(N)
    return dfs(ans[n][0]) +  " " + str(n)
print(dfs(1))