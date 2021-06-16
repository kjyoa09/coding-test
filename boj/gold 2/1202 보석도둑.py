from sys import stdin
import heapq as hq
stdin = open("in.txt","r")
N,K = map(int,stdin.readline().rstrip().split())
M = []
B = []
for _ in range(N):
    m,v = map(int,stdin.readline().rstrip().split())
    hq.heappush(M,(m,v))
for _ in range(K):
    hq.heappush(B,int(stdin.readline()))
ans = 0
print(ans)
print(M,B)


'''
from sys import stdin
stdin = open("in.txt","r")
N,K = map(int,stdin.readline().rstrip().split())
M = []
B = []
for _ in range(N):
    m,v = map(int,stdin.readline().rstrip().split())
    M.append((m,v))
for _ in range(K):
    B.append(int(stdin.readline()))
B.sort()
M.sort(key=lambda x:-x[1])
ans = 0
while M:
    m,v = M.pop(0)
    lt = 0;rt = len(B)-1
    tmp = float("INF")
    while lt<=rt:
        mid = (lt + rt)//2
        if B[mid] > m:
            if mid < tmp:
                tmp = mid
            rt = mid - 1
        elif B[mid] == m:
            tmp = mid
            break
        else:
            lt = mid + 1
    if tmp != float("INF"):
        ans += v
        del B[tmp]
print(ans)
'''