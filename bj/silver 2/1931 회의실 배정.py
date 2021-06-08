import sys
n = int(sys.stdin.readline().strip())
arr = []
for i in range(n):
    s,e = map(int,sys.stdin.readline().strip().split())
    arr += [(s,e)]

arr.sort(key = lambda x: (x[1],x[0]))


cnt = 0
end = -1

while arr:
    s,e = arr.pop(0)

    if s >= end:
        end = e
        cnt += 1
print(cnt)
