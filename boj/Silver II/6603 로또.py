from sys import stdin
from itertools import combinations

stdin = open('in.txt','r')
input = stdin.readline

while 1:
    A = list(map(int,input().strip().split(' ')))
    if A[0] == 0:
        break
    else:
        for a in combinations(A[1:],6):
            print(*a)
        print()