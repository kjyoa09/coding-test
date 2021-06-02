import sys

n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

if n <= 2:
    print(sum(arr))
else:
    dic = {2:[arr[0]+arr[1],arr[1]]}
    dic[3] = [dic[2][1] + arr[2],arr[0]+arr[2]]

    for i in range(4,n+1):
        a = dic[i-1][1]+ arr[i-1]
        b = max(dic[i-2]) + arr[i-1]
        dic[i] = [a,b]
    print(max(dic[n]))
