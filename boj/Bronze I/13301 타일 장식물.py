import sys
sys.stdin = open("in.txt","r")
n = int(sys.stdin.readline())
a,b = 1,1
if n == 1:
    print(4)
else :
    for i in range(n-2):
        a,b = a+b,a
    print(2*(a+b)+2*a)