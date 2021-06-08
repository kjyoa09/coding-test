import sys
arr = list(map(int,sys.stdin.readline().strip().split()))


if sorted(arr,reverse = True) == arr:
    print("descending")
elif sorted(arr) == arr:
    print("ascending")
else:
    print("mixed")