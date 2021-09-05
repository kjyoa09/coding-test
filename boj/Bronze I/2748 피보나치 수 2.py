import sys
sys.stdin = open("in.txt","r")
n = int(sys.stdin.readline())
a,b = 1,1
for _ in range(n-2):
    a,b = a+b,a
print(a)