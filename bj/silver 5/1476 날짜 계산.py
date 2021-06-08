import sys
arr = list(map(int,sys.stdin.readline().strip().split()))
for i in range(1,15*28*19+1):
    if i %15 == arr[0]%15 and i %28 == arr[1]%28 and i %19 == arr[2]%19   :
        print(i)
        break
