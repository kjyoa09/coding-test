import sys
input = sys.stdin.readline
a,b = map(int, input().split())
c,d = divmod(a,b)
print(c,d,sep = "\n")
