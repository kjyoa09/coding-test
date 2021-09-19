from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

k,m = map(int,input().strip().split(' '))
dic = {}
for _ in range(k):
    num = input().strip()
    dic[num] = dic.get(num,0) + 1

def st(s):
    tmp = s * 10
    return int(tmp[:10])

arr = sorted(dic.keys(), key = lambda x:(-st(x),-len(x)))
re,TF,maxL,ans = m - sum(dic.values()),True,max(len(x) for x in dic.keys()),''

for a in arr:
    ans += a*dic[a] 
    if TF and len(a) == maxL:
        ans += a*re
        TF = False
print(ans)