# 냅색알고리즘.. :  문제보고 떠올리지 못함.. 
# >> 단순하게 작은 것만 가져가지 못할 때..
# >> 가져가거나 가져가지 못하는 경우로 나눠 생각할 때 고려.

# 1부터 N개의 모든 물건들을 살펴보고, 
# 배낭 용량이 K였을 때 이 배낭에 들어가 있는 물건들의 가치합의 최댓값
from sys import stdin
stdin = open("in.txt","r")
N,M = map(int,stdin.readline().rstrip().split())
A = list(map(int,stdin.readline().rstrip().split()))
C = list(map(int,stdin.readline().rstrip().split()))
Sc = sum(C)
maps = [[0] * (Sc+1) for _ in range(N)] 

for i in range(N):
    for j in range(Sc+1):
        if i == 0:
            if j >= C[i]:
                maps[i][j] = A[i]
        else:
            if j-C[i] >= 0:
                maps[i][j] = max(maps[i-1][j],maps[i-1][j-C[i]] +A[i])
            else:
                maps[i][j] = maps[i-1][j]
for idx,v in enumerate(maps[-1]):
    if v >= M:
        print(idx)
        break
