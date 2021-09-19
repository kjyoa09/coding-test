from sys import stdin
from math import gcd
stdin = open('in.txt','r')
input = stdin.readline
arr = []
N = int(input().strip())
for _ in range(N):
    arr.append(int(input().strip()))
arr.sort()

for i in range(N-1):
    if i == 0:
        g = gcd(arr[i+1] - arr[i],arr[i+2]-arr[i+1])
    else:
        g = gcd(g,arr[i+1]-arr[i])
ans = 0
for i in range(N-1):
    ans += (arr[i+1]-arr[i])//g -1
print(ans)