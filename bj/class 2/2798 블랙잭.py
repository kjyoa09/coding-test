from itertools import combinations
import sys
n,m = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr = list(combinations(arr,3))
arr = [sum(x) for x in arr if sum(x) <= m]
print(max(arr))