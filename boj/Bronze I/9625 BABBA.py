import sys
sys.stdin = open("in.txt","r")
n = int(sys.stdin.readline())
a,b =1,0
for _ in range(n):
    a,b = b,a+b
print(str(a),str(b),sep = " ")