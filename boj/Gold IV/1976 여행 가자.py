# Union find
from sys import stdin,setrecursionlimit
setrecursionlimit(10**8)

stdin = open('in.txt','r')
input = stdin.readline

n,m = int(input()),int(input())
arr = list(range(n))
maps = [list(map(int,input().strip().split(' '))) for _ in range(n)]
def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx])
    return arr[idx]

def union(idx1,idx2):
    if idx1 > idx2:
        arr[idx1] = idx2
    else:
        arr[idx2] = idx1

for idx1 in range(n):
    for idx2 in range(idx1+1,n):
        if maps[idx1][idx2]:
            union(find(idx1),find(idx2))

print('YES' if len(set(find(mm-1) for mm in map(int,input().strip().split(' ')))) == 1 else 'NO')