import sys

sys.stdin = open('in.txt')
input = sys.stdin.readline

while 1:
    n = int(input())
    if n == 0 : break
    
    lis = []
    for _ in range(n):
        lis.append(input().strip())
    lis.sort(key = lambda x:x.lower())
    print(lis[0])
