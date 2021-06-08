import sys
n = sys.stdin.readline().rstrip()
b = int(sys.stdin.readline())
l_stack = list(n)
r_stack = []
for s in range(b):
    x = sys.stdin.readline().rstrip() 
    if x == "L" and l_stack:
        r_stack.append(l_stack.pop())
    elif x == "D" and r_stack:
        l_stack.append(r_stack.pop())
    elif x == "B" and l_stack:
        l_stack.pop()
    else:
        if x[0] == "P":
            l_stack.append(x[2])

print(''.join(l_stack + r_stack[::-1]))
