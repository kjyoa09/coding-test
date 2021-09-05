import sys

n = int(sys.stdin.readline())

arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

def div(arr):
    length = len(arr)
    re = [[],[],[],[]]

    for i in range(length):
        if i < length//2:
            re[0] += [arr[i][:length//2]]
            re[1] += [arr[i][length//2:]]
        else:
            re[2] += [arr[i][:length//2]]
            re[3] += [arr[i][length//2:]]
    return re

def check(arr):
    tmp = [x for y in arr for x in y]
    if all(x == "1" for x in tmp) or all(x == "0" for x in tmp):
        return tmp[0]
    else:
        re = div(arr)
        return "(" + check(re[0])+ check(re[1])+ check(re[2])+ check(re[3]) + ")"

print(check(arr))
