import sys

sys.stdin = open('in.txt')
input = sys.stdin.readline

n = int(input())
arr = [x for x in input().strip().split(' ')]
mat = [[0]*n for _ in range(n)]

for i in range(n):
    mat[i][i] += 1
for i in range(n-1):
    if arr[i] == arr[i+1]:
        mat[i][i+1]+=1
        
for i in range(1,n):
    for c in range(i,n):
        r = c-i
        if mat[max(0,r+1)][max(0,c-1)] and (arr[r] == arr[c]):
            mat[r][c] += 1

n = int(input())

for _ in range(n):
    a,b = map(int,input().split(' '))
    print(mat[a-1][b-1])