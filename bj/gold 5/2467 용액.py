from sys import stdin
stdin = open("in.txt")
N = int(stdin.readline())
arr = list(map(int,stdin.readline().rstrip().split()))
lt = 0; rt= N-1
v = float("INF")
while lt<rt:
    tmp = arr[lt] + arr[rt]
    if abs(tmp) < v:
        v = abs(tmp)
        ans = str(arr[lt]) + " " + str(arr[rt])    
    if tmp < 0:
        lt +=1
    else:
        rt -=1
print(ans)