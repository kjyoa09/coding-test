from sys import stdin
from math import ceil
stdin = open('in.txt','r')
input = stdin.readline

N = int(input())
arr = list(map(int,input().strip().split(' ')))
B,C = map(int,input().strip().split(' '))
ans = 0

for a in arr:
    a -= B
    ans += 1
    if a > 0 :
        ans += ceil(a/C)
print(ans)