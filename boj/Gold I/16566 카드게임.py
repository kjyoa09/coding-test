# bisect + union find
# 단, 민수가 카드를 내지 못하는 경우는 없다고 가정한다. >> ll = list(range(M+1)) >> 다른 조건 추가 안함

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
