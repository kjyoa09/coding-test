import sys
input = sys.stdin.readline
a,b = map(int,input().split())
ans = a*b
arr = list(map(int,input().split()))
for i in arr:
    print(i-ans,end = " ")
