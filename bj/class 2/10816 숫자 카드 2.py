from collections import Counter
import sys

_ = int(input())
arr = list(map(int,sys.stdin.readline().split()))
dic = Counter(arr)

_ = int(input())

arr = list(map(int,sys.stdin.readline().split()))

for i in arr:
    if i in dic:
        print(dic[i],end = " ")
    else:
        print(0, end = " ")