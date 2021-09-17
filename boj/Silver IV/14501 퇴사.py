from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline
N,arr = int(input()),[]

for n in range(N):
    t,p = map(int,input().strip().split(' '))
    arr.append((t+n,n+1,p))
arr.sort(key = lambda x:(x[0],-x[-1],x[1]))
li = [0] * (N+1)

for a in arr:
    e,s,p = a
    if e > N:
        continue
    else:
        li[e] = max(max(li[:s])+p,li[e])
print(max(li))