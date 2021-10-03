from sys import stdin,setrecursionlimit,stdout
setrecursionlimit(10**5)
stdin = open('in.txt','r')
input = stdin.readline

N = int(input())
maps = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().strip().split(' '))
    maps[a].append(b)
    maps[b].append(a)

pr = [0] * (N+1) 
dg = [0] * (N+1)
def mk(pre,now,cnt):
    dg[now] = cnt
    for c in maps[now]:
        if c != pre:
            pr[c] = now
            mk(now,c,cnt+1)
mk(0,1,0)
dic = {}
def ftn(a,b):
    while dg[a] != dg[b]:
        if dg[a] > dg[b] : 
            a = pr[a]
        else:
            b = pr[b]
    while a != b:
        a = pr[a]
        b = pr[b]
    return str(a)

for _ in range(int(input())):
    a,b = map(int,input().split(' '))
    if (a,b) in dic:
        stdout.write(dic[(a,b)] + '\n')
    else:
        tmp = ftn(a,b)
        stdout.write(tmp + '\n')
        dic[(a,b)] = tmp
        dic[(b,a)] = tmp
