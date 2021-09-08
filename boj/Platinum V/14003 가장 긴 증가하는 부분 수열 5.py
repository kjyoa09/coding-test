from sys import stdin
input = stdin.readline

N = int(input().strip())
arr = list(map(int,input().strip().split(' ')))


def binary(arr,tg):
    lt,rt=0,len(arr)-1
    
    while lt<=rt:
        mid = (lt+rt)//2
        if arr[mid] < tg :
            lt = mid + 1 
        else:
            rt = mid - 1
    return rt + 1

la = -1
for idx,num in enumerate(arr):
    if idx == 0:
        ans,val,bf = [num],[0],[-1]
    else:
        if ans[-1] < num:
            ans.append(num)
            bf.append(val[-1])
            val.append(idx)
            if la < idx:
                la = idx
        else:
            tg = binary(ans,num)
            ans[tg] = num
            val[tg] = idx
            if tg == 0:
                bf.append(-1)
            else:
                bf.append(val[tg-1])

print(len(ans))    
re = []
for i in range(len(ans)):
    re.append(arr[la])
    la = bf[la]
re.reverse()
print(*re)


import bisect
from sys import stdin
stdin = open('in.txt')
input = stdin.readline

N = int(input().strip())
arr = list(map(int,input().strip().split(' ')))
ans,val,bf,la = [arr[0]],[0],[-1],-1

for i in range(1,N):
    idx = bisect.bisect_left(ans,arr[i])
    if len(ans) == idx:
        ans.append(arr[i])
        bf.append(val[-1])
        val.append(i)
        if la < i:
            la = i
    else:
        ans[idx] = arr[i]
        val[idx] = i
        if idx == 0:
            bf.append(-1)
        else:
            bf.append(val[idx-1])

print(len(ans))
re = []
for i in range(len(ans)):
    re.append(arr[la])
    la = bf[la]
re.reverse()
print(*re)


