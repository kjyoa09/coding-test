import sys
n = int(input())
ans = []

for _ in range(n):
    tmp = sys.stdin.readline().split()
    if tmp[0] == "push":
        ans.append(tmp[1])
    elif tmp[0] == "pop":
        if len(ans) == 0:
            print(-1)
        else:
            print(ans.pop())
    elif tmp[0] == "size":
        print(len(ans))
    elif tmp[0] == "empty":
        if len(ans) == 0:
            print(1)
        else:print(0)
    else:
        if len(ans) == 0:
            print(-1)
        else:
            print(ans[-1])
