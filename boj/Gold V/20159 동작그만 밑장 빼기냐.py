# https://www.acmicpc.net/problem/20159

import sys

sys.stdin = open('in.txt')
input = sys.stdin.readline

n = int(input())
arr = [int(x) for x in input().split(' ')]

a = [0]
b = [0]
ans = -float('INF')
for i in range(n//2):
    a.append(a[-1] + arr[2*i]) 
    b.append(b[-1] + arr[2*i+1]) 

for i in range(n//2):
    ans = max([ans,b[-1]-b[i]+a[i],b[-2]-b[i]+a[i+1]])
print(ans)