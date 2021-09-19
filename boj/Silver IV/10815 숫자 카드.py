from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
input()
dic = {k:True for k in map(int,input().strip().split(' '))}
input()
print(*[1 if k in dic else 0 for k in map(int,input().strip().split(' '))])