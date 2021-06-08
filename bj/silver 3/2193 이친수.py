import sys
n = int(input())
a,b = 0,1
for _ in range(2,n+1):
    b,a = a+b,b
print(b)
