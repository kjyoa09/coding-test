import sys
def re(h,w,n):
    a,b = divmod(n,h)
    if b == 0:
        return str(h) + "0" * (2-len(str(a))) + str(a)
    else:
        return str(b) + "0" * (2-len(str(a+1))) + str(a+1)

n = int(input())
for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    print(re(a,b,c))
