from collections import Counter 
from sys import stdin
stdin = open("in.txt","r")

T = int(stdin.readline())
n = int(stdin.readline())
A = list(map(int,stdin.readline().rstrip().split()))
m = int(stdin.readline())
B = list(map(int,stdin.readline().rstrip().split()))

for idx,v in enumerate(A):
    if idx == 0:
        Sa = [v]
    else:
        tmp = Sa[-idx:]
        Sa += [v] + [x+v for x in tmp]
for idx,v in enumerate(B):
    if idx == 0:
        Sb = [v]
    else:
        tmp = Sb[-idx:]
        Sb += [v] + [x+v for x in tmp]

Sa.sort()
Sb.sort()
BC = Counter(Sb)
def binS(find):
    lt=0
    rt=len(Sb)-1
    while lt<=rt:
        mid=(lt+rt)//2
        if Sb[mid]==find:
            return mid
        if Sb[mid]>find:
            rt=mid-1
            continue
        if Sb[mid]<find:
            lt=mid+1
            continue
    return -1
ans = 0
for sa in Sa:
    find=T-sa
    tmp=binS(find)
    if tmp!=-1:
        ans+=BC[Sb[tmp]]
print(ans)