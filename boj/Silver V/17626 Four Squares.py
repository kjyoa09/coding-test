# DP활용 
import sys
from math import ceil, sqrt
sys.stdin = open("C:\\Users\\LYJ_lab\\Desktop\\동현\\coding-test\\bj\\class 3\\in.txt","r")

n = int(sys.stdin.readline())

inf = float("INF")
arr = [0,1]
for i in range(2,n+1):
    cnt = inf
    if i == ceil(sqrt(i))**2:
        arr += [1]
    else:
        for num in range(1,ceil(sqrt(i))):
            tmp = i - num**2
            if cnt > arr[tmp] + 1:
                cnt = arr[tmp] + 1
        arr += [cnt]
print(arr[-1])