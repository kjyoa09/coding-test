import sys,math

a,b = map(int,sys.stdin.readline().strip().split())


print(math.factorial(a)//math.factorial(b)//math.factorial(a-b))
