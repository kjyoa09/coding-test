# 1 : row 마다 확인
# 2 : row의 0의 짝 홀 여부와 K의 짝 홀 여부가 같지 않으면 그 행은 전부 켤 수 없음 
#     and 0의 개수가 K 보다 작아야함
# 3 : 2번 조건이 만족하면 행마다 같은 패턴인 행 개수 파악 >> ans
from sys import stdin
stdin = open("in.txt")
input = stdin.readline
N,M = map(int,input().rstrip().split())
maps = [list(map(int,list(input().rstrip())))for _ in range(N)]
K = int(input())
ans = 0
for nn in range(N):
    zero = sum(1 for x in maps[nn] if x == 0)
    if zero <= K and zero%2 == K%2:
        tmp = 0
        for r in range(N):
            if maps[nn] == maps[r]:
                tmp +=1
        if ans < tmp:
            ans = tmp
print(ans)