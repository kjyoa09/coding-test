n = int(input())
if n < 2:
    print(n)
else:
    a,b = 0,1
    for i in range(n-1):
        b,a = a+b,b
    print(b)
