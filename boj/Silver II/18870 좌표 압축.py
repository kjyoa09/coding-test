import sys

n = int(input())
arr = list(map(int,sys.stdin.readline().split()))

dic = list(set(arr))
dic.sort()
dic = {k:idx for idx,k in enumerate(dic)}

for i in arr:
    print(dic[i],end = " ")
