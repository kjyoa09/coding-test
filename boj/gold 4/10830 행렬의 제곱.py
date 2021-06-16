# 11444 피보나치 수 6이랑 비슷한 문제
import sys
sys.stdin = open("in.txt","r")
N,B = map(int,sys.stdin.readline().rstrip().split())
arr = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
T_arr = list(map(list,zip(*arr)))

def matmul(arr,T_arr):
#    T_arr = list(map(list,zip(*arr)))
    re = []
    for tmp in arr:
        Tmp = []
        for tt in T_arr:
            v = sum([x*y for x,y in zip(tmp,tt)]) % 1000
            Tmp.append(v)
        re.append(Tmp)
    return re


def dfs(B):
    if B == 1:
        return arr
    else:
        a,b = divmod(B,2)
        T = dfs(a)
        trans = list(map(list,zip(*T)))
        tmp = matmul(T,trans)
        if b == 1:
            tmp = matmul(tmp,T_arr)
        return tmp

A = dfs(B)

for tmp in A:
    B = [str(x % 1000) for x in tmp]
    print(" ".join(B))