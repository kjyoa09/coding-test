import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
lt = rt = 0
tmp = arr[0]
cnt = 0
while lt <= rt :
#    print(lt,rt,tmp)
    if tmp >= m:
        if tmp == m:
            cnt += 1
        
        if lt == rt:          
            if rt + 1 != n:
                rt += 1
                tmp += arr[rt]
            else:
                break
        else:
            tmp -= arr[lt]
            lt += 1
            

    else:
        if rt + 1 == n:
            break
        else:
            rt += 1
            tmp += arr[rt]
print(cnt)
