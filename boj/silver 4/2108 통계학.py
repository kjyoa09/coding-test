import sys
from collections import Counter

n = int(input())
arr = []

a = 0
for _ in range(n):
    tmp = int(sys.stdin.readline())
    arr += [tmp]
    a += tmp

arr.sort()
dic = Counter(arr)

dic = dic.most_common()


print(int(round(a/n,0)))
print(arr[n//2])
if len(dic) != 1 and dic[0][1] == dic[1][1]:
    print(dic[1][0])
else:
    print(dic[0][0])
print(arr[-1]-arr[0])
