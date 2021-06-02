import sys

arr = [list(range(1,15))]

for i in range(14):
    tmp = [sum(arr[-1][:i]) for i in range(1,15)]
    arr += [tmp]

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    print(arr[k][n-1])
