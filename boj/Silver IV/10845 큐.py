import sys

n = int(input())
stack = []

for _ in range(n):
    tmp = sys.stdin.readline().split()

    if len(tmp) == 2:
        stack += [tmp[1]]

    elif tmp[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))

    elif tmp[0] == "size":
        print(len(stack))

    elif tmp[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        elif tmp[0] == "front":
            print(stack[0])
        else:
            print(stack[-1])
