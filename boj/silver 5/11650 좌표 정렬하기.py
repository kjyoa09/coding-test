import re,sys


n = int(input())

arr = []

for i in range(n):
    a,b = map(int,input().split())
    arr += [[a,b]]

arr.sort(key = lambda x:(x[0],x[1]))

for a,b in arr:
    print(a,b)
