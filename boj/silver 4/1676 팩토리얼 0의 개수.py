import sys
import math

input = sys.stdin.readline

n = int(input())

n = str(math.factorial(n))

cnt = 0

for i in n[::-1]:
    if i == "0":
        cnt += 1
    else:
        print(cnt)
        break
