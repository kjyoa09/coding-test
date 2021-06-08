import sys

n = int(input())
stack = []

for _ in range(n):
    tmp = int(sys.stdin.readline())

    if tmp == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack += [tmp]
print(sum(stack))
