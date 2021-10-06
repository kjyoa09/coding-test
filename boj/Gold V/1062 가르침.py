from sys import stdin
from itertools import combinations
stdin = open('in.txt','r')
input = stdin.readline

N,K = map(int,input().strip().split(' '))
arr,pos = [],{}

for _ in range(N):
    tmp = ['0']*26
    for r in input().strip():
        tmp[ord(r)-97] = '1'
        if r not in ['a','n','t','i','c']:
            pos[ord(r)-97] = 1
    arr.append(int(''.join(tmp),2))
ans = 0

if len(pos) <= K-5:
    print(N)
elif K < 5:
    print(0)
else:
    for pp in combinations(pos.keys(),K-5):
        tmp = ['1','0','1','0','0',
               '0','0','0','1','0',
               '0','0','0','1','0',
               '0','0','0','0','1',
               '0','0','0','0','0','0']
        for p in pp:
            tmp[p] = '1'
        tmp = int(''.join(tmp),2)
        cnt = 0
        for ar in arr:
            if tmp & ar == ar:
                cnt+=1
        if ans < cnt:
            ans = cnt
    print(ans)    
