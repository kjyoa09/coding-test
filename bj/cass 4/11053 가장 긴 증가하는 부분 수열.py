import sys

sys.stdin = open("in.txt","r")

N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

stack = []
for num in arr:
    stack.append([num])
    for idx,i in enumerate(stack):
        if i[-1] < num:
            stack.append(stack[idx]+[num])
    

stack.sort(key = lambda x: -len(x))
print(stack)

print(len(stack[0]))