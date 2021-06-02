import sys

n = int(input())
arr = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr += [(a,b)]

for tu in arr:
    tmp = [x for x in arr if x[0] > tu[0] and x[1] > tu[1]]
    print(len(tmp) + 1,end = " ")
