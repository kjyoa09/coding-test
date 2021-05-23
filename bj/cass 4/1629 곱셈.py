import sys,math

sys.stdin = open("in.txt","r")

a,b,c = map(int,sys.stdin.readline().rstrip().split())
print(pow(a,b,c))

