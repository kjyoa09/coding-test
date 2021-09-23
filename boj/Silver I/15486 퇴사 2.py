from sys import stdin
stdin = open('in.txt')
input = stdin.readline
N,arr = int(input()),[]

for n in range(N):
    t,p = map(int,input().strip().split(' '))
    arr.append((t+n,n+1,p))
arr.sort(key = lambda x:(x[0],-x[-1],x[1]))

ans = 0
li = [0] * (N+1)
for a in arr:
    e,s,p = a
    if e > N:
        continue
    else:
        if li[s-1] == 0:
            li[e] = max(max(li[:s])+p,li[e])
        else:
            li[e] = max(li[s-1]+p,li[e])
print(max(li))
