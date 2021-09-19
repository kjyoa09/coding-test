from sys import stdin,stdout
stdin = open('in.txt',"r")
input = stdin.readline

n = int(input())
ans = [0] * 10001

for i in range(n):
    ans[int(input())] += 1
for i in range(10001):
    for _ in range(ans[i]):
        stdout.write(str(i)+'\n')