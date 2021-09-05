def check(arr,tmp,n):
    lt = 0; rt = n - 1
    
    while lt <= rt:
        mid = (lt + rt)//2

        if arr[mid] == tmp:
            return True
        elif tmp < arr[mid]:
            rt = mid - 1
        else:
            lt = mid + 1
    return False


import sys
n = int(input())
arr = list(map(int,input().split()))
arr.sort()

_ = input()
arr1 = list(map(int,input().split()))

for i in arr1:
    if check(arr,i,n):
           print(1)
    else:
        print(0)
