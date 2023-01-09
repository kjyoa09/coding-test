import sys
from collections import defaultdict

sys.stdin = open('in.txt')
input = sys.stdin.readline

n,m = map(int,input().split(' '))
dic = defaultdict(lambda:0)

for _ in range(n):
    dic[int(input())] += 1

ans,v = {},0
for num in sorted(dic.keys()):
    ans[num] = v
    v+=dic[num]
    
for _ in range(m):
    print(ans.get(int(input()),-1))
