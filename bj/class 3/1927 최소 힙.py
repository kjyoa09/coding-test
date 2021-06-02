import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    n = int(input())

    if n == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(hq.heappop(arr))
    else:
        hq.heappush(arr,n)
