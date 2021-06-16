import sys
n = int(input())
t = 64
cnt = 0
while n != 0:
    if t > n:
        t = t//2
    else:
        n -= t
        cnt += 1
print(cnt)
