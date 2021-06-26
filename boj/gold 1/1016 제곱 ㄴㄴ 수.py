# 에라토스테네스의 체 응용
# 2 ~ max**(1/2)까지 진행
from sys import stdin
stdin = open("in.txt","r")
input = stdin.readline
s,e = map(int,input().rstrip().split())
ans = [True] * (e-s+1)
f = int(e**(1/2)//1)
for i in range(2,f+1):
    tmp = i**2
    tmp = (s//tmp+1) * tmp if s%tmp else s
    for tt in range(tmp,e+1,i**2):
        ans[tt-s] = False
print(sum(ans))
