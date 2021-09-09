from sys import stdin
from bisect import bisect_right
stdin = open('in.txt')
input = stdin.readline
N,M,K = map(int,input().strip().split(' '))

arr = list(map(int,input().strip().split(' ')))
arr.sort()

ll = list(range(M+1))
def find(idx):
    if ll[idx] != idx:
        ll[idx] = find(ll[idx])
    return ll[idx]

def union(idx1,idx2):
    idx2 = find(idx2)
    ll[idx1] = idx2

for num in map(int,input().strip().split(' ')):
    idx = find(bisect_right(arr,num))
    print(arr[idx])
    union(idx,idx+1)
