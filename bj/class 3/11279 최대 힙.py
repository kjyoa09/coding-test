import sys
import heapq as hq

n = int(sys.stdin.readline())

stack = []

for i in range(n):
    tmp = int(sys.stdin.readline())
    if tmp == 0:
        if len(stack) == 0:
            print(0)
        else:
            print(-hq.heappop(stack))
    else:
        hq.heappush(stack,-tmp)
