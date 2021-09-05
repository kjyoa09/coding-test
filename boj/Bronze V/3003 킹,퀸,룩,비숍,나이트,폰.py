import sys
input = sys.stdin.readline
a = list(map(int,input().split()))
b = [1,1,2,2,2,8]
for A,B in zip(a,b):
    print(B-A,end= " ")
