# https://www.acmicpc.net/problem/20159

import sys
from heapq import *

sys.stdin = open('in.txt')
input = sys.stdin.readline

n = int(input())
arr = [int(x) for x in input().split(' ')]

a = 0
b = 0
diff = -float('INF')
for i in range(n//2):
    a += arr[2*i]
    b += arr[2*i+1]
    diff = max(diff,arr[2*i+1]-arr[2*i])
print(a + diff if diff > 0 else a)