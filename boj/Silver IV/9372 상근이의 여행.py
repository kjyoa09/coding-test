from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

for _ in range(int(input())):
    N,M = map(int,input().strip().split(' '))
    print(N-1)