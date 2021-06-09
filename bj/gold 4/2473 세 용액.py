# 2467 용액과 비슷한 문제
# 하나 잡고 이분탐색 수행.
from sys import stdin
stdin = open("in.txt")
n = int(stdin.readline())
arr = list(map(int,stdin.readline().rstrip().split()))
arr.sort()
ans = []
cnt = float("INF")
def binary(num):
    global cnt,ans
    std = arr[num]
    lt = num +1;rt = n-1
    while lt < rt < n:
#        print(std,arr[lt], arr[rt])
        tmp = std + arr[lt] + arr[rt]
        if abs(tmp) < cnt:
            ans = [std,arr[lt],arr[rt]]
            cnt = abs(tmp)
        if tmp < 0:
            lt +=1
        else:
            rt -= 1
for i in range(n-2):
    binary(i)
for i in ans:
    print(i,end=" ")