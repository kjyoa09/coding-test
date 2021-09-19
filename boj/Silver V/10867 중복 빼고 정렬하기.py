from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
input()
print(*sorted(set(map(int,input().strip().split(' ')))))