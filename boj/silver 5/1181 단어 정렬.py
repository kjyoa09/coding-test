import sys
from collections import defaultdict


_ = int(input())
arr = defaultdict(int)
for i in range(_):
    tmp = sys.stdin.readline().split()
    arr[tmp[0]] = 1
A = sorted(arr.keys(),key = lambda x:(len(x),x))
for i in A:
    print(i)