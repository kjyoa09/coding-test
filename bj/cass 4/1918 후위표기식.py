# stack
import sys
sys.stdin = open("in.txt","r")
S = list(sys.stdin.readline().rstrip())

dic = {"+" : 1, "-" : 1,"*" : 2, "/" : 2,"(": -1}
ans = ""

stack = []
while S:
    tmp = S.pop(0)

    if tmp == "(":
        stack.append(tmp)
    elif tmp == ")":
        while stack[-1] != "(":
            ans += stack.pop()
        stack.pop()
    elif tmp in dic:
        if len(stack) != 0 and dic[stack[-1]] >= dic[tmp] :
            while len(stack) != 0 and dic[stack[-1]] >= dic[tmp]:
                ans += stack.pop()
        stack.append(tmp)
    else:
        ans += tmp
    print(stack,tmp)
if len(stack) != 0:
    ans += ''.join(stack[::-1])
print(ans)