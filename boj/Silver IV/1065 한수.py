def f(n):
    tmp = list(str(n))
    tmp = [int(tmp[i]) - int(tmp[i-1])for i in range(1,len(tmp))]
    if len(set(tmp))==1:
        return 1
    else:
        return 0
   
n = int(input())
if n < 100:
    print(n)
else:
    ans = 99
    for i in range(100,n+1):
        a = f(i)
        ans += a
    print(ans)
