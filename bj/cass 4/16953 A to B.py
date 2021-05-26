# Flag : 원하는 것 찾으면 반복문 Break하는 도구 설정
import sys
from collections import deque
sys.stdin = open("in.txt")
N,M = map(int,sys.stdin.readline().rstrip().split())
que = deque([(N,0)])
flag = False
while que:
    num,cnt = que.popleft()
    tmp = [num * 2, num * 10 + 1]

    for i in tmp:
        if i == M:
            flag = True
            print(cnt + 2)
            break
        
        elif i < M:
            que.append((i,cnt + 1))
    
    if flag :
        break

if not flag:
    print(-1)