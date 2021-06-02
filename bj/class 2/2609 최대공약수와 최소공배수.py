import sys
import math

input = sys.stdin.readline

n,m = map(int,input().split())

lcm = math.lcm(n,m)
print(n*m//lcm,lcm,sep = "\n")
