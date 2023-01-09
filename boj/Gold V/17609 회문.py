import sys

sys.stdin = open('in.txt')
input = sys.stdin.readline

def ftn(st):
    # print(st)
    r,l = 0,len(st)-1
    while r<=l:
        if st[r] == st[l]:
            r+=1
            l-=1
        else:
            return (False,r,l)
    return (True,r,l)
    
n = int(input())

for _ in range(n):
    s = input().strip()
    res,r,l = ftn(s)
    if res:
        print(0)
    else:
        if any((ftn(s[r+1:l+1])[0],ftn(s[r:l])[0])):
            print(1)
        else:
            print(2)