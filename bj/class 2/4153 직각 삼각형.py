import sys

while 1:
    arr = list(map(int,sys.stdin.readline().split()))
    
    if arr[0]==arr[1]==arr[2]==0:
        break
    else:
        Max = max(arr)
        e = [x for x in arr if x != Max]
        if Max**2 == e[0]**2 + e[1]**2:
            print("right")
        else:
            print("wrong")
