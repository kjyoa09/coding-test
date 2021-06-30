# 1182 부분 수열의 합 그대로 풀면 시간초과
# 앞부분 뒷부분 나눠서 풀면 시간초과 X
# O(2**N) >> O(2**(N//2))+O(2**(N//2))
from sys import stdin
from collections import defaultdict
stdin = open("in.txt")
input = stdin.readline
N,S = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
ldic = defaultdict(int)
tmp = []
for a in arr[:N//2]:
    ldic[a] += 1
    if len(tmp):
        for i in range(len(tmp)):
            ldic[tmp[i]+a] += 1
            tmp.append(tmp[i]+a)
    tmp.append(a)
rdic = defaultdict(int)
tmp = []
for a in arr[N//2:]:
    rdic[a] += 1
    if len(tmp):
        for i in range(len(tmp)):
            rdic[tmp[i]+a] += 1
            tmp.append(tmp[i]+a)
    tmp.append(a)
ans = ldic[S] + rdic[S]
for lk in ldic.keys():
    ans += ldic[lk] * rdic[S-lk]   
print(ans)