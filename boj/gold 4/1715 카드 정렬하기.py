import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    hq.heappush(arr,num)
if n == 1:
    print(0)
else:
    cnt = 0
    while 1:
        a = hq.heappop(arr)
        b = hq.heappop(arr)

        if len(arr) == 0:
            print(a+b + cnt)
            break
        else:
            cnt += a + b
            hq.heappush(arr,a+b)
