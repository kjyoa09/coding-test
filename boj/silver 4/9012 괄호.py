def check(arr):
    lt = rt = 0
    
    while arr:
        tmp = arr.pop(0)
        if tmp == ")":
            rt += 1
        else:
            lt += 1

        if rt > lt:
            return False
    if rt == lt:
        return True
    else:
        return False
import sys
n = int(sys.stdin.readline())

for i in range(n):
    tmp = list(sys.stdin.readline())[:-1]    
    if len(tmp) % 2 == 1:
        print("NO")
        continue
    else:
        if check(tmp):
            print("YES")
        else:
            print("NO")
