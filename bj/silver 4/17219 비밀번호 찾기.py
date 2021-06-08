import sys

n,m = map(int,sys.stdin.readline().split())
dic = {}

for i in range(n):
    a,b = sys.stdin.readline().split()
    dic[a] = b

for i in range(m):
    a = sys.stdin.readline().split()
    print(dic[a[0]])
