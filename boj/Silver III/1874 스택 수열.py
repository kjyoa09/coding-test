import sys
n = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for _ in range(n)]

li = list(range(1,n+1))

tmp_arr = []
ans = []
while li:
    tmp_arr.append(li.pop(0))
    ans += ["+"]
    if tmp_arr[-1] == arr[0]:
        while tmp_arr[-1] == arr[0]:
            tmp_arr.pop()
            arr.pop(0)
            ans += ["-"]
            if len(arr) == 0 or len(tmp_arr) == 0:
                break
if len(arr) == 0:
    for i in ans:
        print(i)
else:
    print("NO")
    
