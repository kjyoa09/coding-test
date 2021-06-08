import sys
a = int(input())
b = int(input())
ch = [False,False] + [True] * (b - 1)
for i in range(2,b+1):
    if ch[i]:
        for n in range(i+i,b+1,i):
            ch[n] = False
ans = 10000
tot = 0
for i in ch[a:]:
    if i:
        tot += a

        if ans > a:
            ans = a
    a += 1
if tot == 0:
    print(-1)
else:    
    print(tot)
    print(ans)
