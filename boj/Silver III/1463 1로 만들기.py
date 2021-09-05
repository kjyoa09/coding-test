import sys
n = int(sys.stdin.readline())
ans = [0,0,1,1]


if n < 4:
    print(ans[n])
else:
    for i in range(4,n+1):
        tmp = ans[i-1] + 1
        
        if i % 2 == 0:
            if ans[i//2] + 1 < tmp:
                tmp = ans[i//2] + 1
        if i % 3 == 0:
            if ans[i//3] + 1 < tmp:
                tmp = ans[i//3] +1
        ans += [tmp]
        
    print(ans[-1])
            
