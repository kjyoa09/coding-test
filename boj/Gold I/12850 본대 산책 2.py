# 피보나치 수열 행렬 곱 이용
# ditctionary에 저장하면서 해야 시간 초과 안걸림
# 행렬 곱 할 때 마다 %1_000_000_007

#0 : 정보 과학관
#1 : 전산관
#2 : 미래관
#3 : 신앙관
#4 : 한경직 기념관
#5 : 진리관
#6 : 학생회관
#7 : 형남 공학관
from sys import stdin
from collections import defaultdict
stdin = open("in.txt")
input = stdin.readline
N = int(input())
maps = [[0,1,1,0,0,0,0,0],
        [1,0,1,1,0,0,0,0],
        [1,1,0,1,1,0,0,0],
        [0,1,1,0,1,1,0,0],
        [0,0,1,1,0,1,0,1],
        [0,0,0,1,1,0,1,0],
        [0,0,0,0,0,1,0,1],
        [0,0,0,0,1,0,1,0]]
def matmul(maps1,maps2):
    arr = []
    for i in maps1:
        tmp = []
        for j in zip(*maps2):
            tmp.append(sum(x*y for x,y in zip(i,j))%1_000_000_007)
        arr.append(tmp)
    return arr
fib = defaultdict(list)
fib[1] = maps
def dfs(N):
    if N == 1:
        return fib[1]
    else:
        if fib[N]:
            return fib[N]
        else:
            tmp = matmul(dfs(N//2),dfs(N//2))
            if N%2:#홀수
                fib[N] = matmul(tmp,maps)
            else:
                fib[N] = tmp
            return fib[N]
dfs(N)
print(fib[N][0][0]%1_000_000_007)
