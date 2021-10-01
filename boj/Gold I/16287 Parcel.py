from sys import stdin,exit
stdin = open('in.txt','r')
input = stdin.readline

w,n = map(int,input().strip().split(' '))
arr = list(map(int,input().strip().split(' ')))
ans = [False] * (w+1)

for i in range(n):
    for j in range(i+1,n):
        if arr[i] + arr[j] <= w and ans[w-(arr[i] + arr[j])]:
            print('YES')
            exit()

    for j in range(i):
        if arr[i] + arr[j] < w:
            ans[arr[i] + arr[j]] = True
print('NO')