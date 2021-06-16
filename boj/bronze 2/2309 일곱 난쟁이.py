import sys
from itertools import combinations
input = sys.stdin.readline
arr = []
for _ in range(9):
    arr += [int(input())]
arr = list(combinations(arr,7))
for i in arr:
    if sum(i) == 100:
        tmp = list(i)
        tmp.sort()
        for s in tmp:
            print(s)
        break