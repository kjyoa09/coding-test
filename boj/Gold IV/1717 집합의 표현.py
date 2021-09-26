# Union find
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)
stdin = open('in.txt','r')
input = stdin.readline

n,m = map(int,input().strip().split(' '))
arr = list(range(n+1))

def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx])
    return arr[idx]

def union(idx1,idx2):
    if idx1 > idx2:
        arr[idx1] = idx2
        find(idx1)
    else:
        arr[idx2] = idx1
        find(idx2)

for _ in range(m):
    c,a,b = map(int,input().strip().split(' '))

    if c:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(find(a),find(b))
