import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    arr += [[a,b]]
arr.sort(key = lambda x:(x[1],x[0]))

for a,b in arr:
    print(a,b,sep = " ")
