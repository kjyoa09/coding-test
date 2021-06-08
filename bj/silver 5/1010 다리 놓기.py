import math,sys
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    a = math.factorial(b)//math.factorial(a)//math.factorial(b-a)
    print(a)
