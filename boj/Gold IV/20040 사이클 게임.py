# 크루스칼 알고리즘.
# find한 값이 같으면 사이클 생성 >> break

from sys import stdin
stdin = open("in.txt")
N,M = map(int,stdin.readline().rstrip().split())

def find(idx):
    if arr[idx] != idx:
        arr[idx] = find(arr[idx])
    return arr[idx]
def union(idx1,idx2):
    ro1 = arr[idx1];ro2 = arr[idx2]
    arr[max(ro1,ro2)] = min(ro1,ro2)
    find(min(ro2,ro1))
arr = list(range(N))

for i in range(M):
    a,b = map(int,stdin.readline().rstrip().split())
    if find(a) != find(b):
        union(a,b)
    else:
        print(i+1)
        break
else:
    print(0)
print(arr)