# https://www.acmicpc.net/problem/13699

import sys

# sys.stdin = open('in.txt')
# n = int(sys.stdin.readline())

input = sys.stdin.readline
n = int(input())
t = [1]+[0] * 35

for tt in range(1,36):
    for i in range(tt):
        t[tt] += t[i] * t[tt-1-i]

print(t[n])