import sys


n = int(sys.stdin.readline())

a=1;b=3
if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    for i in range(n-2):
        b,a = 2*a+b,b
    print(b %10007)
