# combinations로 모든 경우의 수 확인
import sys
from itertools import combinations
sys.stdin = open("in.txt","r")
N,M = map(int,sys.stdin.readline().rstrip().split())

dic = {1:[],2:[]}

for r in range(N):
    tmp = list(map(int,sys.stdin.readline().rstrip().split()))
    for c,v in enumerate(tmp):
        if v == 1:
            dic[1].append((r,c))
        if v == 2:
            dic[2].append((r,c))
arr = list(combinations(dic[2],M))

ans = float("INF")
for ar in arr:
    tmp = 0
    for hos in dic[1]:
        tmp += min([abs(x[0]-hos[0])+abs(x[1]-hos[1]) for x in ar])
    
    if tmp < ans:
        ans = tmp
print(ans)