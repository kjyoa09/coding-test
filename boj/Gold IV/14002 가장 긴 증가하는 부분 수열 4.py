from sys import stdin
stdin = open('in.txt')
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
for i in range(len(ans)):
    if i == 0:
        re = str(arr[la])
    else:
        re = str(arr[la]) + ' ' + re
    la = bf[la]
print(re)