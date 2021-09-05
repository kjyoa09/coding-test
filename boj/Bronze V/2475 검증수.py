import sys


input = sys.stdin.readline


A = list(map(int,input().strip().split()))
ans = 0
for i in A:
    ans += i**2
print(ans%10)


