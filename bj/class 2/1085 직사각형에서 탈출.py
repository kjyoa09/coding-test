import sys
a,b,c,d = map(int,sys.stdin.readline().strip().split())

print(min(c-a,a,d-b,b))
