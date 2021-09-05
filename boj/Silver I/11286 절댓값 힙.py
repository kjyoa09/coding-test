import sys
import heapq as hq

n = int(sys.stdin.readline())

Heap = []

for i in range(n):
    tmp = int(sys.stdin.readline())

    if tmp != 0:
        if tmp < 0:
            hq.heappush(Heap,(-tmp,-1))
        else:
            hq.heappush(Heap,(tmp,1))
    else:
        if len(Heap) == 0:
            print(0)
        else:
            a,b = hq.heappop(Heap)
            print(a*b)

