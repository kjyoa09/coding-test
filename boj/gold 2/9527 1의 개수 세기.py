from sys import stdin
stdin = open("in.txt")
input = stdin.readline
a,b = map(int,input().rstrip().split())
fac = [1]
for i in range(1,56):
    fac += [fac[-1]*i]
def co(a):
    a = list(map(int,list(bin(a)[2:])))
    tot = sum(a)
    re = sum(a)
    cnt = 0
    while a:
        tmp = a.pop()
        if tmp == 0:
            cnt += 1
        else:
            tot -= 1
            for i in range(cnt+1):
                re += (tot+i) * fac[cnt]//fac[cnt-i]//fac[i]
            cnt += 1
    return re
print(co(b)-co(a-1))
