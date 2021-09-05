import sys,math
sys.stdin = open("in.txt","r")
A,B,C = map(int,sys.stdin.readline().rstrip().split())
A %= B
A *= 10
for i in range(C):
    tm1,tm2 = divmod(A,B)
    A = tm2 * 10
print(tm1)