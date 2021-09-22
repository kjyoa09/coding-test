from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

N = int(input())
arr = list(map(int,input().strip().split(' ')))
ans = [0]+[-1]*(N-1)
cnt = 0

for idx,a in enumerate(arr):
    if ans[idx] == -1:
        continue
    for nn in range(a):
        if idx+nn+1 < N and (ans[idx+nn+1] == -1 or min(ans[idx+nn+1],ans[idx]+1) == ans[idx]+1):
            ans[idx+nn+1] = ans[idx]+1
print(ans[-1])
